from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


from django.http import JsonResponse
from feasto_core.models import Order, OrderItem, Item, User

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    items = kwargs['request_data']['items']
    user_id = kwargs['user'].user_id
    user = User.objects.get(id=user_id)

    for item_data in items:
        item = Item.objects.get(id=item_data['item_id'])
        qty = item.available_quantity
        order_quantity = item_data['order_quantity']

        if qty < order_quantity:
            return JsonResponse(
                data={"message": f"Order cannot be placed. Insufficient inventory for item {item.name}."},
                status=400
            )

    order = Order.objects.create(user=user)

    for item_data in items:
        item = Item.objects.get(id=item_data['item_id'])  # Fetch the Item again
        order_quantity = item_data['order_quantity']


        OrderItem.objects.create(
            order=order,
            item=item,
            order_quantity=order_quantity
        )

        item.available_quantity -= order_quantity
        item.save()

    return JsonResponse(
        data={
            "order_id": order.id,
            "user_id": user_id,
            "items": [{"item_id": i['item_id'], "quantity": i['order_quantity']} for i in items]
        },
        status=201
    )

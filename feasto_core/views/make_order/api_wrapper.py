from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


from django.http import JsonResponse
from feasto_core.models import Order, OrderItem, Item, User, Restaurant


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    items = kwargs['request_data']['items']
    user_id = kwargs['user'].user_id
    user = User.objects.get(id=user_id)
    rest = Restaurant.objects.filter(id= items[0]['restaurant_id']).first()
    if rest is None:
        return JsonResponse(
            data={"message": f"Restaurant with id {items[0]['restaurant_id']} does not exist."},
            status=404
        )
    for item_data in items:
        try:
            # Fetch the item using filter().first(), which can return None
            item = Item.objects.filter(id=item_data['item_id']).first()

            if item is None:
                return JsonResponse(
                    data={"message": f"Item with id {item_data['item_id']} does not exist."},
                    status=404
                )

            qty = item.available_quantity
            order_quantity = item_data['order_quantity']

            if qty < order_quantity:
                return JsonResponse(
                    data={"message": f"Order cannot be placed. Insufficient inventory for item {item.name}."},
                    status=400
                )

        except Exception as e:
            return JsonResponse(
                data={"message": f"An error occurred while processing item {item_data['item_id']}: {str(e)}"},
                status=500
            )

    # Create the order if all items are valid
    order = Order.objects.create(user=user)

    for item_data in items:
        item = Item.objects.get(id=item_data['item_id'])  # Fetch the item again
        order_quantity = item_data['order_quantity']

        # Create order item and update the inventory
        OrderItem.objects.create(
            order=order,
            item=item,
            order_quantity=order_quantity
        )

        item.available_quantity -= order_quantity
        item.save()

    # Construct the order response data
    order_data = {
        "order_id": order.id,
        "user_id": user_id,
        "items": [{"item_id": i['item_id'], "quantity": i['order_quantity']} for i in items]
    }

    return JsonResponse(
        data={"order": order_data},
        status=201
    )
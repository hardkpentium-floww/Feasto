from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from ...models import Order  # Import Order and OrderItem models

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id  # Get the user_id from the request

    # Fetch all orders for the user
    orders = Order.objects.filter(user_id=user_id)

    # Initialize order_data with the user's id and an empty list for orders
    order_data = {
        "user_id": user_id,
        "orders": []
    }

    # Iterate through each order
    for order in orders:
        # For each order, fetch the associated items (OrderItem)
        order_items = order.items.all()  # Assuming 'items' is the related_name for OrderItem

        # Prepare the items list for this order
        items_list = []
        for item in order_items:
            items_list.append({
                "item_id": item.item.id,  # Assuming item is a ForeignKey in OrderItem
                "item_name": item.item.name,  # Assuming item has a name field
                "order_quantity": item.order_quantity
            })

        # Append the order details with its items to the orders list in order_data
        order_data["orders"].append({
            "order_id": order.id,
            "items": items_list
        })

    # Return the response with the order data
    return JsonResponse(data=order_data, status=200)

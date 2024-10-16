from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from ...models import Item


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    rest_id = kwargs['query_params']['restaurant_id']  # Get the restaurant ID from query params

    # Fetch all items for the restaurant
    items = Item.objects.filter(restaurant_id=rest_id)

    # Prepare items_data as a list to hold item details
    items_data = []

    # Iterate through each item and convert it to a dictionary
    for item in items:
        item_data = {
            "name": item.name,  # Assuming Item model has an 'id' field
            "available_quantity": item.available_quantity  # Assuming Item model has an 'available_quantity' field
        }
        # Append each item_data dictionary to items_data list
        items_data.append(item_data)

    # Return the items data in the response
    return JsonResponse({'items': items_data}, status=200)

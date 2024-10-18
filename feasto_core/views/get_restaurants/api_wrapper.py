from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...models import Restaurant
from django.http import JsonResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # Ensure 'query' key exists in kwargs
    query = kwargs.get('query_params', {})

    # Extract parameters with defaults
    status = query.get('status')
    location = query.get('location')
    offset = query.get('offset')
    limit = query.get('limit')


    # Fetch restaurants
    fetched_restaurants = Restaurant.objects.all()

    if status:
        fetched_restaurants = fetched_restaurants.filter(status=status.lower())

    if location:
        fetched_restaurants = fetched_restaurants.filter(location=location)

    # Apply offset and limit
    fetched_restaurants = fetched_restaurants[offset:offset + limit]

    # Handle empty result case
    if not fetched_restaurants:
        return JsonResponse({'message': 'No restaurants found'}, status=404)

    # Serialize restaurants (you will need a serializer or manual serialization)
    restaurants_data = [{'id': rest.id, 'name': rest.name, 'location': rest.location, 'status': rest.status.upper()} for rest in fetched_restaurants]

    return JsonResponse({'restaurants': restaurants_data}, status=200)

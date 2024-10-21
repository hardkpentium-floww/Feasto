from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from feasto_core.views.get_restaurants.get_restaurants import get_restaurants
from .validator_class import ValidatorClass
from ...interactors.get_restaurants_interactor import GetRestaurantsInteractor
from ...interactors.storage_interfaces.storage_interface import GetRestaurantDTO
from ...models import Restaurant
from django.http import JsonResponse, HttpResponse

from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # Ensure 'query' key exists in kwargs
    query = kwargs.get('query_params', {})

    # Extract parameters with defaults
    status = query.get('status')
    location = query.get('location')
    offset = query.get('offset')
    limit = query.get('limit')

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetRestaurantsInteractor(storage=storage)

    get_restaurant_dto = GetRestaurantDTO(
        status=status,
        location=location,
        offset=offset,
        limit=limit
    )
    return interactor.get_restaurants_wrapper(get_restaurant_dto=get_restaurant_dto, presenter= presenter)

    # return JsonResponse(data=restaurants_response, status=201)

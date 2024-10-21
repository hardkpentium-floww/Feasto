from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from feasto_core.views.add_restaurant.add_restaurant import add_restaurant
from .validator_class import ValidatorClass

from django.http import JsonResponse

from ...interactors.add_restaurant_interactor import AddItemInRestaurantMenuInteractor
from ...interactors.storage_interfaces.storage_interface import AddRestaurantDTO
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    rest_name = kwargs['request_data']['name']

    rest_status = kwargs['request_data']['status']
    rest_location = kwargs['request_data']['location']
    # return JsonResponse({"kwargs":kwargs}, 200)
    user_id = kwargs['user'].user_id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddItemInRestaurantMenuInteractor(storage=storage)
    add_restaurant_dto = AddRestaurantDTO(
        name=rest_name,
        location=rest_location,
        status=rest_status,
        user_id=user_id
    )
    restaurant_response = interactor.add_restaurant_wrapper(presenter=presenter,add_restaurant_dto=add_restaurant_dto)

    return restaurant_response


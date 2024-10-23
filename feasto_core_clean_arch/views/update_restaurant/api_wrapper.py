from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from feasto_core.views.update_restaurant.update_restaurant import update_restaurant
from .validator_class import ValidatorClass
from ...interactors.storage_interfaces.storage_interface import UpdateRestaurantDTO
from ...interactors.update_restaurant_interactor import UpdateRestaurantInteractor
from ...models import Restaurant
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    rest_name = kwargs['request_data']['name']
    rest_status = kwargs['request_data']['status']
    rest_id = kwargs['request_data']['id']
    user_id = str(kwargs['user'].user_id)

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateRestaurantInteractor(storage=storage)

    update_restaurant_dto = UpdateRestaurantDTO(rest_id=rest_id, name=rest_name, status=rest_status, user_id=user_id)
    return interactor.update_restaurant_wrapper(update_restaurant_dto=update_restaurant_dto, presenter=presenter)


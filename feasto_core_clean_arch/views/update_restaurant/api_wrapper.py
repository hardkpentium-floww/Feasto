from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
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

    return interactor.update_restaurant(name=rest_name, status=rest_status, user_id=user_id, rest_id=rest_id, presenter=presenter)


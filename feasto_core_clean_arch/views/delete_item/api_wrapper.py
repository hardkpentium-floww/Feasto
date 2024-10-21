from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.delete_item_interactor import DeleteItemInteractor
from ...models import Restaurant
from ...models import Item
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)

def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    restaurant_id = request_data['restaurant_id']
    item_id = request_data['item_id']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteItemInteractor(storage=storage)


    return interactor.delete_item(restaurant_id=restaurant_id, item_id=item_id,user_id=user_id, presenter=presenter)


from django.http import JsonResponse, HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from feasto_core.views.update_item.update_item import update_item
from .validator_class import ValidatorClass
from ...interactors.storage_interfaces.storage_interface import UpdateItemDTO
from ...interactors.update_item_interactor import UpdateItemInteractor
from ...models import Restaurant
from ...models import Item
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs.get('request_data', {})
    user_id = kwargs['user'].user_id
    name = request_data.get('name')
    available_quantity = request_data.get('available_quantity')
    restaurant_id = request_data.get('restaurant_id')
    item_id = request_data.get('item_id')


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateItemInteractor(storage=storage)
    update_item_dto = UpdateItemDTO(
        name=name,
        available_quantity=available_quantity,
        item_id=item_id,
        restaurant_id=restaurant_id,
        user_id=user_id
        )
    return interactor.update_item_wrapper(update_item_dto=update_item_dto, presenter=presenter)


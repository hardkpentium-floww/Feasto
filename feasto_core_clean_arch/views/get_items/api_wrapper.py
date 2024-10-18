from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_items_interactor import GetItemsInteractor

from ...models import Item
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    rest_id = kwargs['query_params']['restaurant_id']  # Get the restaurant ID from query params
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetItemsInteractor(storage=storage)
    # Fetch all items for the restaurant
    items_response = interactor.get_items(restaurant_id=rest_id, presenter=presenter)


    return JsonResponse(data=items_response, status=200)

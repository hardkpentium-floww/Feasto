from django.http import JsonResponse, HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.add_item_interactor import AddItemInteractor
from ...models import Restaurant
from ...models import Item
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs['user'].user_id
    name = kwargs['request_data']['name']
    available_quantity = kwargs['request_data']['available_quantity']
    restaurant_id =  kwargs['request_data']['restaurant_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddItemInteractor(storage=storage)

    # rest = Restaurant.objects.get(id = restaurant_id)
    item_dict = interactor.add_item(restaurant_id = restaurant_id, name= name, available_quantity=available_quantity, presenter=presenter)
    # check = rest.user_id == str(user_id)


    return JsonResponse(data=item_dict, status=201)


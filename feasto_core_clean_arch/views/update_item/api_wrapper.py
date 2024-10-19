from django.http import JsonResponse, HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
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

    return interactor.update_item(user_id=user_id, presenter=presenter, restaurant_id=restaurant_id, item_id=item_id, name=name, available_quantity=available_quantity)

    # return JsonResponse(data=updated_item, status=200)

    # check = Restaurant.objects.get(id=restaurant_id).user_id ==str(user_id)
    #
    # if check:
    #     updatated_item = Item.objects.get(id=item_id)
    #
    #     if name:
    #         updatated_item.name = name
    #
    #     if available_quantity:
    #         updatated_item.available_quantity = available_quantity
    #
    #     updatated_item.save()
    #
    #     response_data = {
    #         "item": {
    #             "name": updatated_item.name,
    #             "available_quantity": updatated_item.available_quantity,
    #             "restaurant_id": updatated_item.restaurant_id,
    #             "id": updatated_item.id
    #         }
    #     }
    #
    #     return JsonResponse(data=response_data, status=200)
    #
    # return JsonResponse(data={f'Invalid request,restaurant_id: {restaurant_id} is does not exists'}, status=400)
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


    # return JsonResponse(data={"message": "deleted the item"}, status=200)
    # try:
    #     restaurant = Restaurant.objects.get(id=restaurant_id)
    #
    #     if restaurant.user_id != str(user_id):
    #         return JsonResponse(data={"message": f"Unauthorized: You don't own the restaurant with id {restaurant_id}"},
    #                             status=403)
    #
    #     item = Item.objects.filter(id=item_id).first()
    #     if not item:
    #         return JsonResponse(data={"message": f"Item with id {item_id} does not exist"}, status=404)
    #
    #     item.delete()
    #     return JsonResponse(data={"message": "Item deleted successfully"}, status=200)
    #
    # except Restaurant.DoesNotExist:
    #     return JsonResponse(data={"message": f"Restaurant with id {restaurant_id} does not exist"}, status=404)
    #
    # except Exception as e:
    #     return JsonResponse(data={"message": f"An error occurred: {str(e)}"}, status=500)

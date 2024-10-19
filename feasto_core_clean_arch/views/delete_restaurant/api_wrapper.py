from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.delete_restaurant_interactor import DeleteRestaurantInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    restaurant_id = kwargs['request_data']['restaurant_id']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteRestaurantInteractor(storage=storage)

    return interactor.delete_restaurant(restaurant_id=restaurant_id, presenter=presenter, user_id=user_id)

    # return JsonResponse(status=200)

    # check = Restaurant.objects.get(id=restaurant_id).user_id == str(user_id)
    #
    # if check:
    #     rest = Restaurant.objects.filter(id=restaurant_id).first()
    #     rest.delete()
    #
    #     return JsonResponse(data={"message":"deleted the restaurant"}, status=200)
    #
    # return JsonResponse(data={"message":f'Invalid request,restaurant_id: {restaurant_id} is does not exists'}, status=400)
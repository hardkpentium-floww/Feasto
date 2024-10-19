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

    # return JsonResponse(data=updated_restaurant, status=200)

    # updatated_restaurant = Restaurant.objects.get(id = rest_id)
    #
    # if rest_name:
    #     updatated_restaurant.name = rest_name
    #
    # if rest_status:
    #     updatated_restaurant.status = rest_status
    #
    # updatated_restaurant.save()
    #
    # restaurant_data = {
    #     "id": updatated_restaurant.id,
    #     "name": updatated_restaurant.name,
    #     "owner": updatated_restaurant.user.name,
    #     "location": updatated_restaurant.location,
    #     "status": updatated_restaurant.status
    # }
    #
    # return JsonResponse(data={"restaurant": restaurant_data} , status=201)
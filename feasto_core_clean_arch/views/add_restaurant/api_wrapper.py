from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from django.http import JsonResponse

from ...interactors.add_restaurant_interactor import AddRestaurantInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    rest_name = kwargs['request_data']['name']

    rest_status = kwargs['request_data']['status']
    rest_location = kwargs['request_data']['location']
    # return JsonResponse({"kwargs":kwargs}, 200)
    user_id = kwargs['user'].user_id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddRestaurantInteractor(storage=storage)

    restaurant_response = interactor.add_restaurant(presenter=presenter, name=rest_name, location=rest_location, status=rest_status, user_id=user_id)

    return restaurant_response

    # restaurant = Restaurant.objects.create(
    #     name=rest_name,
    #     user=user,
    #     location=rest_location,
    #     status=rest_status.lower()
    # )
    #
    # restaurant_data = {
    #     "id": restaurant.id,
    #     "name": restaurant.name,
    #     "owner": restaurant.user.name,
    #     "location": restaurant.location,
    #     "status": restaurant.status.upper()
    # }
    #
    # return JsonResponse(data=restaurant_data, status=201)
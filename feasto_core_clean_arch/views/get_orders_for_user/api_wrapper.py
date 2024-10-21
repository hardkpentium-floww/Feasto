from django.http import JsonResponse, HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.get_orders_for_user_interactor import GetOrdersForUserInteractor

from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'].user_id)  # Get the user_id from the request


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetOrdersForUserInteractor(storage=storage)

    return interactor.get_orders_for_user(user_id=user_id, presenter=presenter)


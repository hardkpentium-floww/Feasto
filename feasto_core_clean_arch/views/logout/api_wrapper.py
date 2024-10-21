from debugpy.adapter import access_token
from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from oauth2_provider.models import RefreshToken

from .validator_class import ValidatorClass
from ...interactors.logout_interactor import LogoutInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = LogoutInteractor(storage=storage)

    return interactor.logout(user_id=user_id, presenter=presenter)



from django.http import HttpResponse, JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from feasto_core_clean_arch.views.login.validator_class import ValidatorClass
from feasto_core_clean_arch.models.user import  User


from feasto_core_clean_arch.interactors.login_interactor import LoginInteractor
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation
from feasto_core_clean_arch.storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    phone_no = kwargs['request_data']['phone_no']
    user_id = User.objects.get(phone_no = phone_no).id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = LoginInteractor(storage=storage)

    return interactor.login_wrapper(user_id=user_id, presenter=presenter)


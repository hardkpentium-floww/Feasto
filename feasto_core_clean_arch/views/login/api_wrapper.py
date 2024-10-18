
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

    login_response = interactor.login(user_id=user_id, presenter=presenter, phone_no=phone_no)

    return JsonResponse(data = login_response, status=200)

    # print(phone_no)
    #
    # user_id= User.objects.get(phone_no = phone_no).id
    #
    # user = UserAccount.objects.get(user_id=user_id)
    #
    #
    # application = Application.objects.create(
    #     name='feasto',
    #     user=user,  # The user associated with the application
    #     client_type=Application.CLIENT_CONFIDENTIAL,  # or Application.CLIENT_CONFIDENTIAL
    #     authorization_grant_type=Application.GRANT_PASSWORD,  # adjust as needed
    # )
    #
    # if not user:
    #     return HttpResponse("User Not Found", status=404)
    #
    # print(user, user.user_id, type(user.user_id))
    #
    # access_token_str = generate_token()
    #
    # # Generate a random refresh token
    # refresh_token_str = generate_token()
    #
    # # Token expiry time (set for 1 hour)
    # expires = timezone.now() + timedelta(hours=1)
    #
    # # Create the access token
    #
    #
    # access_token = AccessToken.objects.create(
    #     user=user,
    #     token=access_token_str,
    #     application=application,
    #     expires=expires,
    #     scope='read write',  # Define the scope based on your requirement
    #     source_refresh_token=None
    # )
    #
    #
    # # Create the refresh token
    # refresh_token = RefreshToken.objects.create(
    #     user_id=user.user_id,
    #     token=refresh_token_str,
    #     application=application,
    #     access_token=access_token
    # )
    #
    #
    #
    # response_data = {
    #     "access_token": access_token_str,
    #     "expires_in": expires,
    #     "token_type": "Bearer",
    #     "refresh_token": refresh_token_str
    # }
    # # print(user,phone_no,prev_refresh_token,access_token_str,refresh_token_str,access_token,refresh_token)
    #
    # return JsonResponse(response_data, status=202)

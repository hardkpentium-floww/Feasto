from datetime import timezone, timedelta
from oauthlib.common import generate_token


from feasto.wsgi import application
from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidUserId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, \
    AuthenticationTokensDTO, AccessTokenDTO, RefreshTokenDTO
from oauth2_provider.models import Application

from typing import List

class LoginInteractor:

    application = None
    user_id = None
    access_token_str = None
    refresh_token_str = None
    expires = None
    user = None

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    # login_dto = AuthenticationTokensDTO(
    #     access_token=access_token_str,
    #     expires_in=expires,
    #     token_type="Bearer",
    #     scope="read write",
    #     refresh_token=refresh_token_str
    # )

    def login(self,
                 user_id: str,
                 presenter: PresenterInterface
                 ) :
        user_id = user_id
        access_token_str = generate_token()
        refresh_token_str = generate_token()
        expires = timezone.now() + timedelta(hours=1)
        # user = UserAccount.objects.get(user_id=user_id)
        user = self.storage.get_user_account(user_id=user_id)
        access_token_dto = AccessTokenDTO(
            user_id=user_id,
            token=access_token_str,
            application_name="feasto",
            expires=expires,
            scope='read write',
            source_refresh_token=""
        )

        access_token = self.storage.create_access_token(
           access_token_dto=access_token_dto)

        refresh_token_dto = RefreshTokenDTO(
            user_id=user.user_id,
            token=refresh_token_str,
            application_name="feasto",
            access_token=access_token
        )
        refresh_token = self.storage.create_refresh_token(
            refresh_token_dto=refresh_token_dto
        )
        try:
            self.storage.validate_user_id(user_id=user_id)
        except InvalidUserId:
            presenter.get_error_response_for_invalid_user()
            return

        login_dto = AuthenticationTokensDTO(
            access_token=self.access_token_str,
            expires_in=self.expires,
            token_type="Bearer",
            scope="read write",
            refresh_token=self.refresh_token_str
        )


        return presenter.get_response_for_login(login_dto= login_dto)

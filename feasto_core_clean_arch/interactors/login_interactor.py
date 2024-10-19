from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidUserId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface

from typing import List

class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login(self,
                 user_id: int,
                 presenter: PresenterInterface,
                 phone_no: str
                 ) :
        try:
            self.storage.validate_user_id(user_id=user_id)
        except InvalidUserId:
            presenter.error_response_for_invalid_user()
            return

        login_dto = self.storage.login(
            user_id= user_id,
            phone_no= phone_no
        )


        return presenter.get_response_for_login(login_dto= login_dto)

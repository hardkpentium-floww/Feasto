from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface

from typing import List

class LogoutInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
    def logout_wrapper(self,
                 user_id: int,
                 presenter: PresenterInterface):

        self.logout(
            user_id= user_id
        )



    def logout(self,
                 user_id: int,
                 ) :

        self.storage.logout(
            user_id= user_id
        )

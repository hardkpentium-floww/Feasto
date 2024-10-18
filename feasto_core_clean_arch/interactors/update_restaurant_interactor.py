from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface

from typing import List

class UpdateRestaurantInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_restaurant(self,
                 rest_id: int,
                 presenter: PresenterInterface,
                 name: str,
                 status: str,
                 user_id: str
                 ) :

        rest_dto = self.storage.update_restaurant(
            user_id= user_id,
            name= name,
            status=status,
            rest_id= rest_id
        )

        return presenter.get_response_for_update_restaurant(restaurant_dto= rest_dto)

from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId, InvalidItemId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface

from typing import List

class UpdateItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_item(self,
                 user_id: int,
                 presenter: PresenterInterface,
                 name: str,
                 available_quantity: int,
                 item_id: int,
                 restaurant_id: int
                 ) :
        try:
            self.storage.validate_restaurant_id(restaurant_id=restaurant_id)
        except InvalidRestaurantId:
            presenter.error_response_for_restaurant_not_found()
            return

        try:
            self.storage.validate_item_id(item_id=item_id)
        except InvalidItemId:
            presenter.error_response_for_item_not_found()
            return

        item_dto = self.storage.update_item(
            user_id= user_id,
            name= name,
            available_quantity=available_quantity,
            item_id= item_id,
            restaurant_id= restaurant_id
        )

        return presenter.get_response_for_update_item(item_dto= item_dto)

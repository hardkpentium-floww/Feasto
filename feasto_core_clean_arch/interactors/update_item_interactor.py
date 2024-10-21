from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId, InvalidItemId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, UpdateItemDTO

from typing import List

class UpdateItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_item(self,
                 update_item_dto: UpdateItemDTO,
                 presenter: PresenterInterface
                 ) :

        user_id = update_item_dto.user_id
        item_id = update_item_dto.item_id
        restaurant_id = update_item_dto.restaurant_id
        name = update_item_dto.name
        available_quantity = update_item_dto.available_quantity

        try:
            self.storage.validate_restaurant_id(restaurant_id=restaurant_id)
        except InvalidRestaurantId:
            presenter.get_error_response_for_restaurant_not_found()
            return

        try:
            self.storage.validate_item_id(item_id=item_id)
        except InvalidItemId:
            presenter.get_error_response_for_item_not_found()
            return

        item_dto = self.storage.update_item(
            update_item_dto= update_item_dto
        )

        return presenter.get_response_for_update_item(item_dto= item_dto)

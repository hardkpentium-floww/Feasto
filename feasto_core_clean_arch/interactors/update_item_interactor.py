from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId, InvalidItemId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, UpdateItemDTO

from typing import List

class UpdateItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_item_wrapper(self,
                 update_item_dto: UpdateItemDTO,
                 presenter: PresenterInterface
                 ) :
        try:
            update_item_dto = self.update_item(
                update_item_dto= update_item_dto,
            )
        except InvalidRestaurantId:
            return presenter.get_error_response_for_restaurant_not_found()
        except InvalidItemId:
            return presenter.get_error_response_for_item_not_found()


        return update_item_dto
    def update_item(self,
                 update_item_dto: UpdateItemDTO
                 ) :

        item_id = update_item_dto.item_id
        restaurant_id = update_item_dto.restaurant_id

        self.storage.validate_restaurant_id(restaurant_id=restaurant_id)
        self.storage.validate_item_id(item_id=item_id)


        item_dto = self.storage.update_item(
            update_item_dto= update_item_dto
        )

        return item_dto

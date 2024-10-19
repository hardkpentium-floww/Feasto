from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidItemId, InvalidRestaurantId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface

from typing import List

class MakeOrderInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def make_order(self,
                 user_id: int,
                 presenter: PresenterInterface,
                 items: List[dict]
                 ) :
        for item in items:
            try:
                self.storage.validate_item_id(item_id=item["item_id"])
            except InvalidItemId:
                presenter.error_response_for_item_not_found()
                return

            try:
                self.storage.validate_restaurant_id(restaurant_id=item["restaurant_id"])
            except InvalidRestaurantId:
                presenter.error_response_for_restaurant_not_found()
                return

        order_dto = self.storage.make_order(
            user_id= user_id,
            items_data= items,
        )

        return presenter.get_response_for_make_order(order_dto= order_dto)

from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidItemId, InvalidRestaurantId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, OrderItemDTO

from typing import List

class MakeOrderInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def make_order_wrapper(self, user_id: str,
                 presenter: PresenterInterface,
                 items: List[dict]):
        try:
            order_dto = self.make_order(
                user_id=user_id,
                items=items
            )
        except InvalidItemId:
            return presenter.get_error_response_for_item_not_found()
        except InvalidRestaurantId:
            return presenter.get_error_response_for_restaurant_not_found()

        return presenter.get_response_for_make_order(order_dto=order_dto)


    def make_order(self,
                 user_id: str,
                 items: List[dict]
                 ) :
        item_ids = [item["item_id"] for item in items]
        restaurant_ids = [item["restaurant_id"] for item in items]


        self.storage.bulk_validate_items_ids(item_ids)
        self.storage.bulk_validate_restaurant_ids(restaurant_ids)

        items_data = []

        for item in items:
            order_item_dto = OrderItemDTO(
                item_id=item["item_id"],
                order_quantity=item["order_quantity"],
                order_id=item["order_id"]
            )
            items_data.append(
                order_item_dto
            )

        order_dto = self.storage.make_order(
            user_id= user_id,
            items_data= items_data,
        )
        return order_dto


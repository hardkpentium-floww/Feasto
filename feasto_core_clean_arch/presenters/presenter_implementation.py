from typing import List

from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import ItemDto, RestaurantDTO, OrderDto


class PresenterImplementation(PresenterInterface):

    def get_response_for_get_items(self, items_dto: List[ItemDto]):
        pass

    def get_response_for_get_restaurants(self, restaurants_dto: List[RestaurantDTO]):
        pass

    def get_response_for_get_orders_for_user(self, orders_dto: List[OrderDto]):
        pass


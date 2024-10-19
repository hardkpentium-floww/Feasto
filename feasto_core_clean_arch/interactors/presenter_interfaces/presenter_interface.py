from abc import abstractmethod
from typing import List

from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import ItemDTO, RestaurantDTO, OrderDTO, \
    LoginDTO


class PresenterInterface:

    @abstractmethod
    def error_response_for_invalid_user(self):
        pass

    @abstractmethod
    def error_response_for_restaurant_not_found(self):
        pass

    @abstractmethod
    def error_response_for_item_not_found(self):
        pass

    @abstractmethod
    def error_response_for_invalid_restaurant_owner(self):
        pass
    @abstractmethod
    def get_response_for_get_items(self, items_dto: List[ItemDTO]):
        pass

    @abstractmethod
    def get_response_for_get_restaurants(self, restaurants_dto: List[RestaurantDTO]):
        pass

    @abstractmethod
    def get_response_for_add_restaurant(self, restaurant_dto: RestaurantDTO):
        pass

    @abstractmethod
    def get_response_for_get_orders_for_user(self, orders_dto: List[OrderDTO]):
        pass

    @abstractmethod
    def get_response_for_add_item(self, item_dto: ItemDTO):
        pass

    @abstractmethod
    def get_response_for_make_order(self, order_dto:OrderDTO):
        pass

    @abstractmethod
    def get_response_for_update_item(self, item_dto: ItemDTO):
        pass

    @abstractmethod
    def get_response_for_update_restaurant(self, restaurant_dto: RestaurantDTO):
        pass

    @abstractmethod
    def get_response_for_login(self, login_dto: LoginDTO):
        pass
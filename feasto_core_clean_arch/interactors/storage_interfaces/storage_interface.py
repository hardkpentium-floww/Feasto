from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, List

from feasto_core_clean_arch.constants.enum import StatusType


@dataclass()
class UserDTO:
    id: str
    name: str
    phone_no: str

@dataclass()
class ItemDTO:
    name: str
    id: int
    available_quantity: int
    restaurant_id: int


@dataclass()
class RestaurantDTO:
    id: int
    name: str
    user: UserDTO
    location: str
    status: StatusType

@dataclass()
class OrderItemDTO:
    item_id: int
    order_quantity: int
    order_id: int



@dataclass()
class OrderDTO:
    id: int
    user_id: int
    items: List[OrderItemDTO]

@dataclass()
class LoginDTO:
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    token_type: str

class StorageInterface:

    @abstractmethod
    def get_user(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    def get_item(self, item_id: int,
                    restaurant_id: int) -> ItemDTO:
        pass

    @abstractmethod
    def add_item(self,
                    restaurant_id: int, name: str = None, available_quantity: int = None) -> ItemDTO:
        pass

    @abstractmethod
    def add_restaurant(self,
                 name: str, user_id: str, status: StatusType, location: str) -> RestaurantDTO:
        pass

    @abstractmethod
    def update_item(self, item_id: int, restaurant_id: int, user_id: int,
                    name: str = None, available_quantity: int = None) -> ItemDTO:
        pass

    @abstractmethod
    def update_restaurant(self,
                    name: str, status: StatusType , user_id: str, rest_id: int) -> RestaurantDTO:
        pass

    @abstractmethod
    def delete_restaurant(self,
                          restaurant_id: int, user_id: int):
        pass

    @abstractmethod
    def delete_item(self, item_id:int,
                          restaurant_id: int, user_id: str):
        pass

    @abstractmethod
    def get_items(self,
                 restaurant_id: int) -> List[ItemDTO]:
        pass

    @abstractmethod
    def get_restaurants(self, status: str, location: str, offset: int, limit: int) -> List[RestaurantDTO]:
        pass

    @abstractmethod
    def get_restaurant(self,
                        restaurant_id: int) -> RestaurantDTO:
        pass

    @abstractmethod
    def make_order(self, items_data: List[dict], user_id: int) -> OrderDTO:
        pass

    @abstractmethod
    def get_user_id(self) -> str:
        pass

    @abstractmethod
    def create_order_item(self,  item_id: int, order_quantity: int, restaurant_id: int):
        pass

    @abstractmethod
    def login(self, user_id: int, phone_no: str) -> LoginDTO:
        pass

    @abstractmethod
    def logout(self, user_id: int):
        pass

    @abstractmethod
    def get_orders_for_user(self, user_id: str) -> List[OrderDTO]:
        pass

    @abstractmethod
    def validate_restaurant_owner(self, restaurant_id:int, user_id:str):
        pass

    @abstractmethod
    def validate_restaurant_id(self, restaurant_id:int):
        pass

    @abstractmethod
    def validate_item_id(self, item_id:int):
        pass

    @abstractmethod
    def validate_user_id(self, user_id:str):
        pass
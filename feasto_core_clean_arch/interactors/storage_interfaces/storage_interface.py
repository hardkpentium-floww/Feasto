from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, List



@dataclass()
class UserDTO:
    id: int
    name: str
    phone_no: str

@dataclass()
class ItemDTO:
    name: str
    id: int
    available_quantity: int
    restaurant_id: str


@dataclass()
class RestaurantDTO:
    id: int
    name: str
    user: UserDTO
    location: str
    status: str

@dataclass()
class OrderItemDTO:
    item_id: int
    order_quantity: int
    restaurant_id: int



@dataclass()
class OrderDto:
    id: int
    user_id: int
    items: List[OrderItemDTO]
    location: str
    status: str



class StorageInterface:

    @abstractmethod
    def get_user(self, user_id: int,) -> UserDTO:
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
                 name: str, user_id: int, status: str, location: str) -> ItemDTO:
        pass

    @abstractmethod
    def update_item(self, item_id: int,
                  name: str= None, available_quantity:int= None) -> ItemDTO:
        pass

    @abstractmethod
    def update_restaurant(self,
                    name: str, status: str ) -> RestaurantDTO:
        pass

    @abstractmethod
    def delete_restaurant(self,
                          restaurant_id: int):
        pass

    @abstractmethod
    def delete_item(self, item_id:int,
                          restaurant_id: int):
        pass

    @abstractmethod
    def get_items(self,
                 restaurant_id: int) -> List[ItemDTO]:
        pass

    @abstractmethod
    def get_restaurants(self) -> List[RestaurantDTO]:
        pass

    @abstractmethod
    def get_restaurant(self,
                        restaurant_id: int) -> RestaurantDTO:
        pass

    @abstractmethod
    def make_order(self, order_items: List[OrderItemDTO],
                   restaurant_id: int) -> OrderDto:
        pass


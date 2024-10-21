from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, List

from feasto_core_clean_arch.constants.enum import RestaurantStatus
from oauth2_provider.models import Application

@dataclass()
class AddRestaurantDTO:
    name: str
    user_id: str
    location: str
    status: RestaurantStatus

@dataclass()
class AccessTokenDTO:
    user_id :str
    token :str
    application_name:str
    expires:int
    scope :str  # Define the scope based on your requirement
    source_refresh_token :str


@dataclass()
class RefreshTokenDTO:
    user_id :str
    token :str
    application_name:str
    access_token: str

@dataclass()
class UserDTO:
    id: str
    name: str
    phone_no: str

@dataclass()
class GetRestaurantDTO:
    offset: int
    limit: int
    location: str
    status: RestaurantStatus

@dataclass()
class UpdateItemDTO:
    name: str
    available_quantity: int
    user_id: str
    item_id: int
    restaurant_id: int

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
    status: RestaurantStatus

@dataclass()
class OrderItemDTO:
    item_id: int
    order_quantity: int
    order_id: int

@dataclass()
class UpdateRestaurantDTO:
    name: str
    status: RestaurantStatus
    user_id: str
    rest_id: int

@dataclass()
class OrderDTO:
    id: int
    user_id: str
    items: List[OrderItemDTO]

@dataclass()
class AuthenticationTokensDTO:
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    token_type: str

class StorageInterface:
    
    @abstractmethod
    def bulk_validate_items_ids(self, item_ids):
        pass
    
    @abstractmethod
    def bulk_validate_restaurant_ids(self, restaurant_ids):
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    def get_item(self, item_id: int,
                    restaurant_id: int) -> ItemDTO:
        pass

    @abstractmethod
    def add_item(self,
                    restaurant_id: int, name: str, available_quantity: int) -> ItemDTO:
        pass

    @abstractmethod
    def get_user_account(self, user_id: str) -> UserAccount:
        pass
    @abstractmethod
    def add_restaurant(self,
                       add_restaurant_dto: AddRestaurantDTO) -> RestaurantDTO:
        pass

    @abstractmethod
    def update_item(self,update_item_dto: UpdateItemDTO) -> ItemDTO:
        pass

    @abstractmethod
    def update_restaurant(self,
                          update_restaurant_dto: UpdateRestaurantDTO) -> RestaurantDTO:
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
    def get_restaurants(self, get_restaurant_dto: GetRestaurantDTO) -> List[RestaurantDTO]:
        pass

    @abstractmethod
    def get_restaurant(self,
                        restaurant_id: int) -> RestaurantDTO:
        pass

    @abstractmethod
    def make_order(self, items_data: List[OrderItemDTO], user_id: str) -> OrderDTO:
        pass

    @abstractmethod
    def get_user_id(self) -> str:
        pass

    @abstractmethod
    def create_order_item(self,  item_id: int, order_quantity: int, restaurant_id: int):
        pass


    @abstractmethod
    def create_refresh_token(self,
                             refresh_token_dto: RefreshTokenDTO):
        pass

    @abstractmethod
    def create_access_token(self,
                            access_token_dto: AccessTokenDTO):
        pass

    @abstractmethod
    def get_application_instance(self, application_name:str) -> Application:
        pass

    @abstractmethod
    def logout(self, user_id: int):
        pass

    @abstractmethod
    def get_orders_for_user(self, user_id: str) -> List[OrderDTO]:
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
from django.contrib.auth.middleware import get_user

from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, ItemDTO, \
    RestaurantDTO, UserDTO, OrderItemDTO, OrderDTO
from ..models import User,Item
from typing import List

from ..models.restaurant import Restaurant


class StorageImplementation(StorageInterface):
    def get_user(self, user_id: int,) -> UserDTO:
        user = User.objects.get(id=user_id)
        user_dto = UserDTO(
            id= user.id,
            name= user.name,
            phone_no= user.phone_no
        )
        return user_dto

    def get_user_id(self):


    def get_item(self, item_id: int) -> ItemDTO:
        item = Item.objects.get(id=item_id)

        item_dto = ItemDto(
            name=item.name,
            id=item.id,
            available_quantity=item.available_quantity,
            restaurant_id=item.restaurant_id
        )
        return item_dto

    def add_item(self,
                    restaurant_id: int, name: str = None, available_quantity: int = None) -> ItemDTO:
        item = Item.objects.create(
            name=name,
            available_quantity=available_quantity,
            restaurant_id=restaurant_id,
        )

        item_dto = ItemDto(
            name= item.name,
            id= item.id,
            available_quantity= item.available_quantity,
            restaurant_id= item.restaurant_id
        )

        return item_dto

    def add_restaurant(self,
                 name: str, user_id: int, status: str, location: str) -> ItemDTO:
        user = User.objects.get(id = user_id)
        restaurant = Restaurant.objects.create(
            name=name,
            user=user,
            location=location,
            status=status
        )

        user_dto = get_user(user_id)
        restaurant_dto = RestaurantDTO(
            id= restaurant.id,
            name= restaurant.name,
            user= user_dto,
            location=restaurant.location,
            status= restaurant.status

        )

        return restaurant_dto


    def update_item(self, item_id: int,
                name: str= None, available_quantity:int= None) -> ItemDTO:
        item = Item.objects.get(id=item_id)

        if name:
            item.name = name

        if available_quantity:
            item.available_quantity = available_quantity

        item.save()

        item_dto = ItemDto(
            id=item.id,
            name= item.name,
            available_quantity=item.available_quantity,
            restaurant_id=item.restaurant_id
        )

        return item_dto

    def update_restaurant(self,
                    name: str, status: str ) -> RestaurantDTO:
        updatated_restaurant = Restaurant.objects.get(id=rest_id)

        if name:
            updatated_restaurant.name = name

        if status:
            updatated_restaurant.status = status

        updatated_restaurant.save()
        user_dto = get_user(get_user_id())
        restaurant_data = RestaurantDTO(
            id= updatated_restaurant.id,
            name= updatated_restaurant.name,
            user= updatated_restaurant.user.name,
            location= updatated_restaurant.location,
            status= updatated_restaurant.status
        )

        return

    def delete_restaurant(self,
                          restaurant_id: int):
        pass

    def delete_item(self, item_id:int,
                          restaurant_id: int):
        pass

    def get_items(self,
                 restaurant_id: int) -> List[ItemDTO]:
        pass

    def get_restaurants(self) -> List[RestaurantDTO]:
        pass

    def get_restaurant(self,
                        restaurant_id: int) -> RestaurantDTO:
        pass

    def make_order(self, order_items: List[OrderItemDTO],
                   restaurant_id: int) -> OrderDTO:
        pass

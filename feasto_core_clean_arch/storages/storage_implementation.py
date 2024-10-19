from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.middleware import get_user
from future.backports.datetime import timedelta
from ib_users.models import UserAccount
from oauth2_provider.models import Application
from oauth2_provider.models import AccessToken, RefreshToken
from oauthlib.common import generate_token

from feasto_core_clean_arch.models import OrderItem, Order
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, ItemDTO, \
    RestaurantDTO, UserDTO, OrderItemDTO, OrderDTO, LoginDTO
from ..exceptions.custom_exceptions import InvalidRestaurantOwnerId, InvalidRestaurantId, InvalidItemId, InvalidUserId
from ..models import User,Item
from typing import List

from ..models import Restaurant


class StorageImplementation(StorageInterface):
    def get_user(self, user_id: str) -> UserDTO:
        user = User.objects.get(id=user_id)
        user_dto = UserDTO(
            id= user.id,
            name= user.name,
            phone_no= user.phone_no
        )
        return user_dto

    def validate_item_id(self, item_id:int):
        item = Item.objects.filter(id=item_id).exists()
        if not item:
            raise InvalidItemId

    def validate_restaurant_owner(self,restaurant_id:int, user_id:str):
        rest = Restaurant.objects.get(id=restaurant_id)
        if rest.user_id != user_id:
            raise InvalidRestaurantOwnerId
    def validate_user_id(self, user_id:str):
        user = User.objects.filter(id=user_id).exists()
        if not user:
            raise InvalidUserId


    def validate_restaurant_id(self, restaurant_id:int):
        rest = Restaurant.objects.filter(id=restaurant_id).exists()
        if not rest:
            raise InvalidRestaurantId

    def get_item(self, item_id: int, restaurant_id: int) -> ItemDTO:
        item = Item.objects.get(id=item_id)

        item_dto = ItemDTO(
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

        item_dto = ItemDTO(
            name= item.name,
            id= item.id,
            available_quantity= item.available_quantity,
            restaurant_id= item.restaurant_id
        )

        return item_dto

    def add_restaurant(self,
                 name: str, user_id: str, status: str, location: str) -> RestaurantDTO:
        user = User.objects.get(id = user_id)
        restaurant = Restaurant.objects.create(
            name=name,
            user=user,
            location=location,
            status=status
        )

        user_dto = self.get_user(user_id)
        restaurant_dto = RestaurantDTO(
            id= restaurant.id,
            name= restaurant.name,
            user= user_dto,
            location=restaurant.location,
            status= restaurant.status

        )

        return restaurant_dto


    def update_item(self, item_id: int, restaurant_id: int,user_id: int,
                name: str= None, available_quantity:int= None) -> ItemDTO:
        item = Item.objects.get(id=item_id)

        if name:
            item.name = name

        if available_quantity:
            item.available_quantity = available_quantity

        item.save()

        item_dto = ItemDTO(
            id=item.id,
            name= item.name,
            available_quantity=item.available_quantity,
            restaurant_id=item.restaurant_id
        )

        return item_dto

    def update_restaurant(self,
                    name: str, status: str, user_id: str, rest_id: int ) -> RestaurantDTO:
        updatated_restaurant = Restaurant.objects.get(id=rest_id)

        if name:
            updatated_restaurant.name = name

        if status:
            updatated_restaurant.status = status

        updatated_restaurant.save()
        user_dto = self.get_user(user_id)
        restaurant_data = RestaurantDTO(
            id= updatated_restaurant.id,
            name= updatated_restaurant.name,
            user= user_dto,
            location= updatated_restaurant.location,
            status= updatated_restaurant.status
        )

        return restaurant_data

    def delete_restaurant(self,
                          restaurant_id: int, user_id: int):
        rest = Restaurant.objects.get(id = restaurant_id)

        if rest.user_id == user_id:
            rest.delete()

        return



    def delete_item(self, item_id:int,
                          restaurant_id: int, user_id: str):
        rest = Restaurant.objects.get(id=restaurant_id)
        if rest.user.id == str(user_id):
            Item.objects.get(id = item_id).delete()
        items = Item.objects.all()
        return items
    def get_items(self,
                 restaurant_id: int) -> List[ItemDTO]:
        items_list = []
        items = Item.objects.filter(restaurant_id = restaurant_id)

        for item in items:
            item_dto = ItemDTO(
                name= item.name,
                id= item.id,
                available_quantity= item.available_quantity,
                restaurant_id= restaurant_id
            )

            items_list.append(item_dto)

        return items_list

    def get_restaurants(self, status: str, location: str, offset: int, limit: int) -> List[RestaurantDTO]:
        fetched_restaurants = Restaurant.objects.all()

        if status:
            fetched_restaurants = fetched_restaurants.filter(status=status)

        if location:
            fetched_restaurants = fetched_restaurants.filter(location=location)

        fetched_restaurants = fetched_restaurants[offset:offset + limit]

        rest_list = []
        for rest in fetched_restaurants:
            user_dto = self.get_user(rest.user_id)

            rest_dto = RestaurantDTO(
                id=rest.id,
                name=rest.name,
                user=user_dto,
                location=rest.location,
                status=rest.status
            )

            rest_list.append(rest_dto)

        return rest_list


    def get_restaurant(self,
                        restaurant_id: int) -> RestaurantDTO:
        rest = Restaurant.objects.get(id = restaurant_id)
        user_id = rest.user_id
        user_dto = get_user(user_id)
        rest_dto = RestaurantDTO(
            id= rest.id,
            name= rest.name,
            user= user_dto,
            location= rest.location,
            status= rest.status
        )

        return rest_dto

    def make_order(self, items_data: List[dict], user_id: int) -> OrderDTO:

        # Retrieve the user object from the database
        user = User.objects.get(id=user_id)

        # Create the order
        order = Order.objects.create(user=user)

        # Create order items and their DTOs within the method
        order_item_dtos = []
        for item_data in items_data:
            # Create an OrderItem in the database and get its corresponding DTO
            item = Item.objects.get(id=item_data['item_id'])

            order_item = self.create_order_item(
                item=item,
                order_quantity=item_data['order_quantity'],
                order=order
            )
            order_item_dtos.append(order_item)

        # Create and return the OrderDTO
        order_dto = OrderDTO(
            id=order.id,
            user_id=user_id,
            items=order_item_dtos
        )
        return order_dto

    def create_order_item(self, item: Item, order_quantity: int, order: Order) -> OrderItemDTO:

        # Create the order item using Django ORM
        order_item = OrderItem.objects.create(
            item=item,
            order_quantity=order_quantity,
            order=order
        )

        # Create and return the OrderItemDTO
        order_item_dto = OrderItemDTO(
            item_id=order_item.item_id,
            order_quantity=order_item.order_quantity,
            order_id=order.id
        )
        return order_item_dto

    def login(self, user_id: int, phone_no: str) -> LoginDTO:

        application = Application.objects.filter(name='feasto').first()
        access_token_str = generate_token()

        refresh_token_str = generate_token()

        expires = timezone.now() + timedelta(hours=1)
        user = UserAccount.objects.get(user_id=user_id)

        access_token = AccessToken.objects.create(
            user=user,
            token=access_token_str,
            application=application,
            expires=expires,
            scope='read write',  # Define the scope based on your requirement
            source_refresh_token=None
        )

        # Create the refresh token
        refresh_token = RefreshToken.objects.create(
            user_id=user.user_id,
            token=refresh_token_str,
            application=application,
            access_token=access_token
        )



        login_dto = LoginDTO(
            access_token=access_token_str,
            expires_in=expires,
            token_type="Bearer",
            scope="read write",
            refresh_token=refresh_token_str
        )

        return login_dto

    def get_orders_for_user(self, user_id: str) -> List[OrderDTO]:

        orders = Order.objects.filter(user_id=user_id)

        order_dtos = []
        for order in orders:
            order_dto = OrderDTO(
                id=order.id,
                user_id=order.user_id,
                items= self._get_order_items_for_order(order.id)
            )
            order_dtos.append(order_dto)

        return order_dtos

    def logout(self, user_id: int):

        application = Application.objects.get(name='feasto')
        access_token = AccessToken.objects.get(user_id=user_id, application=application)

        access_token.delete()

        return

    def _get_order_items_for_order(self, order_id: int) -> List[OrderItemDTO]:
        order_items = OrderItem.objects.filter(order_id=order_id)

        order_item_dtos = []
        for order_item in order_items:
            order_item_dto = OrderItemDTO(
                item_id=order_item.item_id,
                order_quantity=order_item.order_quantity,
                order_id=order_item.order_id
            )
            order_item_dtos.append(order_item_dto)

        return order_item_dtos
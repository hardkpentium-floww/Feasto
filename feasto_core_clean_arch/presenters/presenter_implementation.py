from typing import List

from feasto_core_clean_arch.constants.exception_messages import RESTAURANT_NOT_FOUND, INVALID_USER, ITEM_NOT_FOUND, \
    NOT_RESTAURANT_OWNER
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import ItemDTO, RestaurantDTO, OrderDTO, \
    UserDTO, OrderItemDTO, AuthenticationTokensDTO
from django.http import JsonResponse, HttpResponse


class PresenterImplementation(PresenterInterface):

    def get_error_response_for_invalid_user(self, user_id:str):
        status, response = INVALID_USER
        data = {
            "status_code" : 401,
            "res_status": status,
            "response": response
        }

        return JsonResponse(data=data, status=status)

    def get_error_response_for_restaurant_not_found(self, restaurant_id:int):
        status, response = RESTAURANT_NOT_FOUND
        data = {
            "status_code": 401,
            "res_status": status,
            "response": response
        }

        return JsonResponse(data=data, status=status)

    def get_error_response_for_item_not_found(self, item_id:int):
        status, response = ITEM_NOT_FOUND
        data = {
            "status_code": 401,
            "res_status": status,
            "response": response
        }

        return JsonResponse(data=data, status=status)

    def get_error_response_for_invalid_restaurant_owner(self, user_id:str):
        status, response = NOT_RESTAURANT_OWNER
        data = {
            "status_code": 401,
            "res_status": status,
            "response": response
        }

        return JsonResponse(data=data, status=status)

    def get_response_for_get_items(self, items_dto: List[ItemDTO]):
        response_items = []
        for item in items_dto:
            response_item = self._get_item_dict(item)
            response_items.append(response_item)

        data = {
            "items" : response_items
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_get_restaurants(self, restaurants_dto: List[RestaurantDTO]):
        response_rest = []
        for rest_dto in restaurants_dto:
            rest_dict = self._get_restaurant_dict(rest_dto)
            response_rest.append(rest_dict)

        data= {
            "restaurants" : response_rest
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_add_item(self, item_dto: ItemDTO):
        data= {
            "item": self._get_item_dict(item_dto)
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_get_orders_for_user(self,orders_dto: List[OrderDTO]):
        order_response = []
        for order_dto in orders_dto:
            order_dict = self._get_order_dict(order_dto)
            order_response.append(order_dict)

        data= {
            "orders" : order_response
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_add_restaurant(self, restaurant_dto: RestaurantDTO):
        data = {
            "restaurant": self._get_restaurant_dict(restaurant_dto)
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_make_order(self, order_dto:OrderDTO):
        data = {
            "order": self._get_order_dict(order_dto)
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_update_item(self, item_dto: ItemDTO):
        data = {
            "item": self._get_item_dict(item_dto)
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_update_restaurant(self, restaurant_dto: RestaurantDTO):
        data = {
            "restaurant": self._get_restaurant_dict(restaurant_dto)
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_get_orders_for_user(self, orders_dto: List[OrderDTO]):
        response_orders = []
        for order_dto in orders_dto:
            order_dict = self._get_order_dict(order_dto)
            response_orders.append(order_dict)

        data= {
            "orders" : response_orders
        }

        return JsonResponse(data=data, status=200)

    def get_response_for_login(self, login_dto: AuthenticationTokensDTO):
        data = {
            "response" : self._get_login_dict(login_dto)
        }

        return JsonResponse(data=data, status=200)
    def _get_item_dict(self, item_dto: ItemDTO):
        return {
            "name": item_dto.name,
            "id": item_dto.id,
            "available_quantity": item_dto.available_quantity,
            "restaurant_id": item_dto.restaurant_id
        }

    def _get_restaurant_dict(self, rest_dto: RestaurantDTO):

        return {
            "name": rest_dto.name,
            "id": rest_dto.id,
            "user": self._get_user_dict(rest_dto.user),
            "location": rest_dto.location,
            "status": rest_dto.status
        }

    def _get_user_dict(self, user_dto: UserDTO):
        return {
            "name": user_dto.name,
            "id": user_dto.id,
            "phone_no": user_dto.phone_no
        }

    def _get_order_item_dict(self, order_item_dto: OrderItemDTO):
        return {
            "item_id": order_item_dto.item_id,
            "order_quantity": order_item_dto.order_quantity,
            "order_id": order_item_dto.order_id
        }

    def _get_order_items_dict(self, order_items_dto: list[OrderItemDTO]):
        items = []
        for order_item_dto in order_items_dto:
            item_dto = self._get_order_item_dict(order_item_dto)
            items.append(item_dto)

        return {
            "items": items
        }


    def _get_order_dict(self, order_dto: OrderDTO):
        return {
            "id": order_dto.id,
            "user_id": order_dto.user_id,
            "items": self._get_order_items_dict(order_dto.items)
        }

    def _get_login_dict(self, login_dto: AuthenticationTokensDTO):
        return {
              "access_token": login_dto.access_token,
              "expires_in": login_dto.expires_in,
              "token_type": login_dto.token_type,
              "scope": login_dto.scope,
              "refresh_token": login_dto.refresh_token
        }
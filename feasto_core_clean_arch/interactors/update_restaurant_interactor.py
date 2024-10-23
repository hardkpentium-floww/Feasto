from feasto_core_clean_arch.constants.enum import RestaurantStatus
from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, \
    UpdateRestaurantDTO

from typing import List

class UpdateRestaurantInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage
    def update_restaurant_wrapper(self,
                          update_restaurant_dto: UpdateRestaurantDTO,
                          presenter: PresenterInterface
                          ):

        restaurant_dto= self.update_restaurant(update_restaurant_dto=update_restaurant_dto)

        return restaurant_dto

    def update_restaurant(self,
                          update_restaurant_dto: UpdateRestaurantDTO,
                          ) :

        rest_id = update_restaurant_dto.rest_id
        self.storage.validate_restaurant_id(restaurant_id=rest_id)

        rest_dto = self.storage.update_restaurant(update_restaurant_dto=update_restaurant_dto)

        return rest_dto

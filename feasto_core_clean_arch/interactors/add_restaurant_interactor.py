from feasto_core.views.add_restaurant.add_restaurant import add_restaurant
from feasto_core_clean_arch.constants.enum import RestaurantStatus
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, AddRestaurantDTO
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class AddItemInRestaurantMenuInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_restaurant_wrapper(self, presenter: PresenterImplementation,
                       add_restaurant_dto: AddRestaurantDTO):


        restaurant_dto = self.add_restaurant(add_restaurant_dto)


        return restaurant_dto



    def add_restaurant(self,
                       add_restaurant_dto: AddRestaurantDTO
                       ) :

        restaurant_dto = self.storage.add_restaurant(
            add_restaurant_dto = add_restaurant_dto
        )

        return restaurant_dto

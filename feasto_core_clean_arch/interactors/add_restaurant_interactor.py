from feasto_core.views.add_restaurant.add_restaurant import add_restaurant
from feasto_core_clean_arch.constants.enum import RestaurantStatus
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class AddItemInRestaurantMenuInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_restaurant(self,
                       presenter: PresenterImplementation,
                       # name: str,
                       # location: str,
                       # status: RestaurantStatus,
                       # user_id: str
                       add_restaurant_dto: AddRestaurantDto
                       ) :

        restaurant_dto = self.storage.add_restaurant(
            # name= name,
            # location=location,
            # status=status,
            # user_id=user_id
            add_restaurant_dto = add_restaurant_dto
        )

        return presenter.get_response_for_add_restaurant(restaurant_dto=restaurant_dto)

from feasto_core.views.get_restaurants.get_restaurants import get_restaurants
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, GetRestaurantDTO
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class GetRestaurantsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_restaurants(self,
                 presenter: PresenterInterface,
                 get_restaurant_dto: GetRestaurantDTO
                 ) :

        restaurants_dto= self.storage.get_restaurants(
            get_restaurant_dto=get_restaurant_dto,
        )

        return presenter.get_response_for_get_restaurants(restaurants_dto=restaurants_dto)

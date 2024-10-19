from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class GetRestaurantsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_restaurants(self,
                 status: str,
                 presenter: PresenterInterface,
                 offset: int,
                 limit: int,
                 location: str
                 ) :

        restaurants_dto= self.storage.get_restaurants(
            status= status,
            offset= offset,
            limit=limit,
            location=location
        )

        return presenter.get_response_for_get_restaurants(restaurants_dto=restaurants_dto)

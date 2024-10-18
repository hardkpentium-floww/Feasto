from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class AddRestaurantInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_restaurant(self,
                 presenter: PresenterImplementation,
                 name: str,
                 location: str,
                 status: str,
                 user_id: int
                 ) :

        restaurant_dto = self.storage.add_restaurant(
            name= name,
            location=location,
            status=status,
            user_id=user_id
        )

        return presenter.get_response_for_add_restaurant(restaurant_dto=restaurant_dto)

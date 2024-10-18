from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class DeleteRestaurantInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_restaurant(self,
                 restaurant_id: int,
                 presenter: PresenterImplementation,
                 user_id: int
                 ) :

        restaurant_dto = self.storage.delete_restaurant(
            restaurant_id= restaurant_id,
            user_id = user_id,
        )


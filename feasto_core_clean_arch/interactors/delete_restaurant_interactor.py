from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId, InvalidRestaurantOwnerId
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
        restaurant_owner_id = self.storage.get_restaurant(restaurant_id=restaurant_id).id
        if restaurant_owner_id != user_id:
            raise InvalidRestaurantOwnerId

        try:
            self.storage.validate_restaurant_id(restaurant_id=restaurant_id)
        except InvalidRestaurantId:
            presenter.get_error_response_for_restaurant_not_found()
            return

        restaurant_dto = self.storage.delete_restaurant(
            restaurant_id= restaurant_id,
            user_id = user_id,
        )

        return
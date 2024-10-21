from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantOwnerId, InvalidRestaurantId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class AddItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_item_wrapper(self,
                         restaurant_id: int,
                         presenter: PresenterInterface,
                         user_id: str,
                         name: str,
                         available_quantity: int,
                         ) :

        restaurant_owner_id = self.storage.get_restaurant(restaurant_id=restaurant_id).id
        if restaurant_owner_id != user_id:
            raise InvalidRestaurantOwnerId

        try:
            item_dto = self.add_item(
                restaurant_id=restaurant_id,
                user_id=user_id,
                name=name,
                available_quantity=available_quantity
            )
        except InvalidRestaurantId:
            return presenter.get_error_response_for_restaurant_not_found()

    def add_item(self,
                 restaurant_id: int,
                 user_id: str,
                 name: str,
                 available_quantity: int,
                 ) :



        self.storage.validate_restaurant_id(restaurant_id=restaurant_id)


        item_dto = self.storage.add_item(
            restaurant_id= restaurant_id,
            name= name,
            available_quantity=available_quantity
        )

        return item_dto

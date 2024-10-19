from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId, InvalidItemId
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class DeleteItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_item(self,
                 restaurant_id: int,
                 presenter: PresenterImplementation,
                 item_id: int,
                 user_id: str
                 ) :
        try:
            self.storage.validate_restaurant_id(restaurant_id=restaurant_id)
        except InvalidRestaurantId:
            presenter.error_response_for_restaurant_not_found()
            return

        try:
            self.storage.validate_item_id(item_id=item_id)
        except InvalidItemId:
            presenter.error_response_for_item_not_found()
            return

        item_dto = self.storage.delete_item(
            item_id= item_id,
            restaurant_id= restaurant_id,
            user_id = user_id,
        )


        return
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class AddItemInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_item(self,
                 restaurant_id: int,
                 presenter: PresenterImplementation,
                 name: str = None,
                 available_quantity: int = None
                 ) :

        item_dto = self.storage.add_item(
            restaurant_id= restaurant_id,
            name= name,
            available_quantity=available_quantity
        )

        return presenter.get_response_for_add_item(item_dto=item_dto)

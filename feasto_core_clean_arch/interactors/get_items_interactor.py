from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class GetItemsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_items(self,
                 restaurant_id: int,
                 presenter: PresenterInterface,
                 ) :

        items_dto = self.storage.get_items(
            restaurant_id= restaurant_id
        )

        return presenter.get_response_for_get_items(items_dto=items_dto)

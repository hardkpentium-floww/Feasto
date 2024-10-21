from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation


class GetOrdersForUserInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_orders_for_user(self,
                 user_id: str,
                 presenter: PresenterImplementation,
                 ) :

        order_dtos = self.storage.get_orders_for_user(
            user_id= user_id
        )

        return presenter.get_response_for_get_orders_for_user(orders_dto=order_dtos)

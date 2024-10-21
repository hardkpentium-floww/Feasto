from feasto_core_clean_arch.constants.enum import RestaurantStatus
from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId
from feasto_core_clean_arch.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface, \
    UpdateRestaurantDTO

from typing import List

class UpdateRestaurantInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_restaurant(self,
                          update_restaurant_dto: UpdateRestaurantDTO,
                          presenter: PresenterInterface,

                          ) :

        rest_id = update_restaurant_dto.rest_id

        try:
            self.storage.validate_restaurant_id(restaurant_id=rest_id)
        except InvalidRestaurantId:
            presenter.get_error_response_for_restaurant_not_found()
            return

        rest_dto = self.storage.update_restaurant(update_restaurant_dto=
                                                  update_restaurant_dto
        )

        return presenter.get_response_for_update_restaurant(restaurant_dto= rest_dto)

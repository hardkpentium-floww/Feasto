
import  graphene

from feasto_core_clean_arch.exceptions.custom_exceptions import InvalidRestaurantId
from feasto_core_clean_arch.interactors.delete_restaurant_interactor import DeleteRestaurantInteractor
from feasto_core_clean_arch.models import Restaurant as RestaurantModel
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation
from feasto_core_clean_arch.storages.storage_implementation import StorageImplementation
from feasto_gql.restaurant.types.types import DeleteRestaurantParams, Restaurant, RestaurantResponse, RestaurantNotFound


class DeleteRestaurant(graphene.Mutation):
    class Arguments:
        params = DeleteRestaurantParams(required=True)

    restaurant = RestaurantResponse

    @staticmethod
    def mutate(root, info, params):

        storage = StorageImplementation()
        presenter = PresenterImplementation()
        interactor = DeleteRestaurantInteractor(storage=storage)
        try:
            rest = interactor.delete_restaurant_wrapper(restaurant_id=params.id, presenter=presenter, user_id=params.user_id)
        except InvalidRestaurantId:
            return RestaurantNotFound(restaurant_id = params.id)


        return Restaurant(
            id=str(rest.id),
            name=rest.name,
            location=rest.location,
            status=rest.status
        )
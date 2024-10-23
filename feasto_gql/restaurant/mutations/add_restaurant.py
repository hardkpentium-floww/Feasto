import graphene
from feasto_gql.restaurant.types.types import Restaurant, AddRestaurantParams, RestaurantResponse
from feasto_core_clean_arch.interactors.add_restaurant_interactor import AddItemInRestaurantMenuInteractor
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface import StorageInterface
from feasto_core_clean_arch.presenters.presenter_implementation import PresenterImplementation
from feasto_core_clean_arch.interactors.storage_interfaces.storage_interface  import AddRestaurantDTO


class AddRestaurant(graphene.Mutation):
    class Arguments:
        params = AddRestaurantParams(required=True)

    restaurant = graphene.Field(RestaurantResponse)  # Specify the return type

    @staticmethod
    def mutate(root, info, params):
        storage = StorageInterface()  # Replace with actual storage instance
        presenter = PresenterImplementation()  # Replace with actual presenter instance

        # Create the DTO from the parameters
        add_restaurant_dto = AddRestaurantDTO(
            name=params.name,
            location=params.location,
            status=params.status
        )

        interactor = AddItemInRestaurantMenuInteractor(storage=storage)

        # Call the wrapper method of the interactor
        restaurant_dto = interactor.add_restaurant_wrapper(
            presenter=presenter,
            add_restaurant_dto=add_restaurant_dto,

        )

        # Return the response
        if restaurant_dto:
            return Restaurant(
                    id=str(restaurant_dto.id),
                    name=restaurant_dto.name,
                    location=restaurant_dto.location,
                    status=restaurant_dto.status
                 )

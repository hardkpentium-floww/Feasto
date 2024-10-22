import graphene

from feasto_gql.restaurant.mutations.add_restaurant import AddRestaurant
from feasto_gql.restaurant.mutations.delete_restaurant import DeleteRestaurant
from feasto_gql.restaurant.mutations.update_restaurant import UpdateRestaurant
from feasto_gql.restaurant.resolvers.get_all_restaurants import resolve_all_restaurants
from feasto_gql.restaurant.resolvers.get_all_orders_for_all_users import resolve_get_all_orders_for_all_users
from feasto_gql.restaurant.types.types import GetRestaurantsResponse, GetOrdersResponse


class Query(graphene.ObjectType):

    get_restaurants = graphene.Field(
        GetRestaurantsResponse
    )

    get_orders_for_users = graphene.Field(
        GetOrdersResponse,
        resolver=resolve_get_all_orders_for_all_users
    )

    get_all_restaurants = graphene.Field(
        GetRestaurantsResponse,
        resolver=resolve_all_restaurants
    )


class Mutation(graphene.ObjectType):
    update_restaurant = UpdateRestaurant.Field(required=True)
    delete_restaurant =DeleteRestaurant.Field(required=True)
    add_restaurant = AddRestaurant.Field(required=True)

schema = graphene.Schema(query=Query, mutation=Mutation)

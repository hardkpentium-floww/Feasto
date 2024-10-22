from feasto_gql.restaurant.dataloaders.orders_for_users_loader import OrdersForUsersLoader
from graphql_service.crm_graphene import context


def resolve_get_orders_for_users(root, info, user_ids):
    user_loader = OrdersForUsersLoader(context= info.context)
    order_ids = user_loader.load(user_ids)
    return order_ids
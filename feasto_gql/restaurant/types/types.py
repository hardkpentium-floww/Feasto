import graphene



class Restaurant(graphene.ObjectType):
    id = graphene.String(required=True)
    name = graphene.String(required=True)
    location = graphene.String(required=True)
    status = graphene.String(required=True)


class AddRestaurantParams(graphene.InputObjectType):
    name = graphene.String(required=True)
    location = graphene.String(required=True)
    status = graphene.String(required=True)

class DeleteRestaurantParams(graphene.InputObjectType):
    id = graphene.String(required=True)
    user_id = graphene.String(required=True)

class GetOrdersResponse(graphene.ObjectType):
    orders = graphene.List(graphene.Int)

class UpdateRestaurantParams(graphene.InputObjectType):
    id = graphene.String(required=True)
    name = graphene.String()
    location = graphene.String()
    status = graphene.Enum()
    user_id = graphene.String()

class RestaurantNotFound(graphene.ObjectType):
    restaurant_id = graphene.String(graphene.String)

class GetRestaurantsParams(graphene.InputObjectType):
    limit = graphene.Int(required=True)
    offset = graphene.Int(required=True)
    status = graphene.Enum()
    location = graphene.String()

class GetRestaurantsResponse(graphene.ObjectType):
    restaurants = graphene.List(Restaurant)


#
# class RestaurantResponse(graphene.ObjectType):
#     class Meta:
#         types = (Restaurant|RestaurantNotFound)
#
#
#
# class GetRestaurantParams(graphene.InputObjectType):
#     id = graphene.String(required=True)
#
# class GetRestaurantResponse(graphene.ObjectType):
#     class Meta:
#         types = (Restaurant|RestaurantNotFound)




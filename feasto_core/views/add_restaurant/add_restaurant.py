from django.http import JsonResponse

from feasto_core.models import Restaurant
from feasto_core.models import User


def add_restaurant(*args, **kwargs):  # pylint: disable=invalid-name
    rest_name = kwargs['request_data']['name']

    rest_status = kwargs['request_data']['status']
    rest_location =  kwargs['request_data']['location']
    # return JsonResponse({"kwargs":kwargs}, 200)
    user_id = kwargs['user'].user_id
    user = User.objects.get(id=user_id)

    restaurant = Restaurant.objects.create(
        name = rest_name,
        user = user,
        location = rest_location,
        status = rest_status
    )

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "owner": restaurant.user.name,
        "location": restaurant.location,
        "status": restaurant.status
    }

    return JsonResponse(data=restaurant_data, status=201)

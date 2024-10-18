from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...models import Restaurant
from ...models import Item

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_id = kwargs['user'].user_id
    name = kwargs['request_data']['name']
    available_quantity = kwargs['request_data']['available_quantity']
    restaurant_id =  kwargs['request_data']['restaurant_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddItemInteractor(storage=storage)

    # rest = Restaurant.objects.get(id = restaurant_id)
    rest = interactor.get_restaurant(id = restaurant_id)
    check = rest.user_id == str(user_id)

    if check:
        item = Item.objects.create(
            name= name,
            available_quantity= available_quantity,
            restaurant_id= restaurant_id,
        )

        response_data = {
            "item": {
                "name": item.name,
                "available_quantity":item.available_quantity,
                "restaurant_id": item.restaurant_id,
                "id": item.id
            }
        }

        return JsonResponse(data=response_data, status=200)

    return JsonResponse(data={"message": f'Invalid request,restaurant_id: {restaurant_id} is does not exists'}, status=400)
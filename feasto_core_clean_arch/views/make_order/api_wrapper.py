from django.http import JsonResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


from django.http import JsonResponse
from feasto_core_clean_arch.models import Order, OrderItem, Item, User, Restaurant
from ...interactors.make_order_interactor import MakeOrderInteractor
from ...interactors.storage_interfaces.storage_interface import OrderItemDTO
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    items = kwargs['request_data']['items']
    user_id = str(kwargs['user'].user_id)

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = MakeOrderInteractor(storage=storage)

    items_data = []

    for item in items:
        order_item_dto = OrderItemDTO(
            item_id=item["item_id"],
            order_quantity=item["order_quantity"],
            order_id=item["order_id"]
        )
        items_data.append(
            order_item_dto
        )

    return interactor.make_order_wrapper(user_id=user_id, items=items, presenter=presenter)


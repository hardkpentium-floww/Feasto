from feasto_core_clean_arch.models import Order, OrderItem


def resolve_get_all_orders_for_all_users(root, info):
    order_ids = Order.objects.all().values('id')
    order_items_ids = OrderItem.objects.filter(order_id__in=order_ids).values('item_id')

    return order_items_ids
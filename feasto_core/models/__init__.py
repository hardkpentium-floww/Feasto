from feasto_core.models.item import Item
from feasto_core.models.order import Order , OrderItem
from feasto_core.models.restaurant import Restaurant
from feasto_core.models.user import User

__all__ = [
    'Item',
    'Order',
    'Restaurant',
    'User',
    'OrderItem'
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#

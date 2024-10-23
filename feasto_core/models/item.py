from django.db import models
from django.contrib.auth.models import AbstractUser
from . import restaurant
from .restaurant import Restaurant


class Item(models.Model):
    name = models.CharField(max_length=50)
    available_quantity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                             related_name="restaurantItems" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

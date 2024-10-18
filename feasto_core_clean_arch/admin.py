
from django.contrib import admin
from .models import Item, Order, Restaurant, User


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'location', 'status','created_at','updated_at')  # Specify the fields to display

# Register the model with the custom admin class
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(User)
from django.db import models
from django.contrib.auth.models import AbstractUser

from feasto_core.models.user import User


from django.db import models

class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('available', 'AVAILABLE'),
        ('unavailable', 'UNAVAILABLE')
    ]
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="available")
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name

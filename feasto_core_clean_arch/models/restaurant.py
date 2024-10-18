from django.db import models
from django.contrib.auth.models import AbstractUser

from feasto_core.models.user import User


from django.db import models

class Restaurant(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'AVAILABLE'),
        ('UNAVAILABLE', 'UNAVAILABLE')
    ]
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="AVAILABLE")
    location = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

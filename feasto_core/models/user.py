from django.db import models


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    phone_no = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
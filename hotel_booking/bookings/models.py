from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    rating = models.FloatField(default=0)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    free = models.BooleanField(default=True)
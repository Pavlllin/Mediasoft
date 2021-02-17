from django.db import models
from city.models import City,Street


class Shop(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey('city.City',on_delete = models.CASCADE)
    street = models.ForeignKey('city.Street',on_delete = models.CASCADE)
    house = models.CharField(max_length=128)
    open_time = models.TimeField()
    close_time = models.TimeField()

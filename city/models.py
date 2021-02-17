from django.db import models

class City(models.Model):
    title = models.CharField(max_length=128)

class Street(models.Model):
    city = models.ForeignKey('City',on_delete = models.CASCADE)
    title = models.CharField(max_length=128)

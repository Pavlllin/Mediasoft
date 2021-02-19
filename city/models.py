from django.db import models


class City(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='Название города')


class Street(models.Model):
    city = models.ForeignKey('city.City',
                             on_delete=models.CASCADE,
                             verbose_name='Город')
    title = models.CharField(max_length=128,
                             verbose_name='Название улицы')

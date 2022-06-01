from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=65)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.CharField(max_length=65)
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(
        upload_to='restaurant/covers/%Y/%m/%d/', blank=True, default='')

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

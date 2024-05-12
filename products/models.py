from django.db import models


# Create your models here.


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=3000)


class Offer(models.Model):
    code = models.TextField(max_length=10)
    description = models.TextField(max_length=255)
    discount = models.FloatField()


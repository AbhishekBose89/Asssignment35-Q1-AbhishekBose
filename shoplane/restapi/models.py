from django.db import models
from django.views import View

# Create your models here.


class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

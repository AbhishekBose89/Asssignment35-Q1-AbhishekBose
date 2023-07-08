from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.TextField(blank=True, null=True)
    category = models.IntegerField()
    ratings = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()

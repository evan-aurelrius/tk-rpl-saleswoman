from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    variant = models.CharField(max_length=50)
    price = models.BigIntegerField()
    stock = models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
from django.db import models
from clients.models import Client

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    product_list = models.JSONField(null=True)
    price = models.BigIntegerField(default=0)

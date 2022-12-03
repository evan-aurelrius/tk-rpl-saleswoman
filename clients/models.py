from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    information = models.TextField()
    sales = models.ForeignKey(to='account.Sales', on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.name


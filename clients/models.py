from django.db import models


class MockSales(models.Model):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    information = models.TextField()
    sales = models.ForeignKey(MockSales, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.name


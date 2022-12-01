from django.contrib import admin
from .models import Client, MockSales

admin.site.register(Client)
admin.site.register(MockSales)

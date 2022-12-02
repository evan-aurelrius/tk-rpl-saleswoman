from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('json', product_JSON, name='json'),
    path('create/', createOrder, name='create-order'),
    path('show/', showOrders, name='show-orders'),
    path('get/<id>', getOrder, name='get-order')
]
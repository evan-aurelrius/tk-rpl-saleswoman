from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('create/', views.create, name='create'),
    path('details/<int:id>', views.getDetailJson, name='details'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='client_index'),
    path('create-client/', views.create_client, name='client_create'),
    path('details/', views.get_details, name='client_details'),
]

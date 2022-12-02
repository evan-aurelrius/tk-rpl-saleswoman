from django.urls import path
from . import views

urlpatterns = [
    path('create-highlight/', views.create_highlight, name='create-highlight'),
    path('show-highlight/', views.show_highlight, name='show-highlight')

]
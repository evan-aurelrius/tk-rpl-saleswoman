from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/search/', views.catalogSearch, name='catalogSearch'),
    path('catalog/search/<str:searchText>', views.catalogSearch, name='catalogSearch'),
    path('catalog/<str:field>/<str:by>', views.catalogSort, name='catalogSort'),
    path('create/', views.create, name='create'),
    path('details/<int:id>', views.getDetailJson, name='details'),
]

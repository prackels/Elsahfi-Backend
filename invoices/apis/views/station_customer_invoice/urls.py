from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_station_customer_invoice),
    path('delete/<int:pk>/', delete.delete_station_customer_invoice),
    path('get/', get.get_station_customer_invoice),
    path('update/<int:pk>/', update.update_station_customer_invoice),
]

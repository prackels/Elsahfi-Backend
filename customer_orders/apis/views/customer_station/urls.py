from . import get, create, update, delete
from django.urls import path

urlpatterns = [
    path('get/', get.get_customer_station),
    path('get-for/<str:customer_name>/', get.get_customer_orders_byname),
    path('create/', create.create_customer_station),
    path('delete/<int:pk>/', delete.delete_customer_station),
    path('update/<int:pk>/', update.update_customer_station),
    
]
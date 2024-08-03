from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_new_purchasing_clients_invoice),
    path('delete/<int:pk>/', delete.delete_new_purchasing_clients_invoice),
    path('get/', get.get_new_purchasing_clients_invoice),
    path('update/<int:pk>/', update.update_new_purchasing_clients_invoice),
]


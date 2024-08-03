from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_deianna_customer_invoice),
    path('delete/<int:pk>/', delete.delete_deianna_customer_invoice),
    path('get/', get.get_deianna_customer_invoice),
    path('update/<int:pk>/', update.update_deianna_customer_invoice),
]

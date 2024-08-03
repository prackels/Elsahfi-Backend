from . import get, create, update, delete
from django.urls import path

urlpatterns = [
    path('get/', get.get_deianna_customer),
    path('create/', create.create_deianna_customer),
    path('delete/<int:pk>/', delete.delete_deianna_customer),
    path('update/<int:pk>/', update.update_deianna_customer),
]
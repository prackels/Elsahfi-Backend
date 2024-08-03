from . import get, create, update, delete
from django.urls import path

urlpatterns = [
    path('get/', get.get_trilla_customer),
    path('create/', create.create_trilla_customer),
    path('delete/<int:pk>/', delete.delete_trilla_customer),
    path('update/<int:pk>/', update.update_trilla_customer),
]
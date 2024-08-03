from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_trilla_customers),
    path('delete/<int:pk>/', delete.delete_trilla_customers),
    path('get/', get.get_trilla_customers),
    path('update/<int:pk>/', update.update_trilla_customers),
]

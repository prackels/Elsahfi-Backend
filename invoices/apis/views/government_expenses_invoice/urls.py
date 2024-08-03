from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_government_expenses_invoice),
    path('delete/<int:pk>/', delete.delete_government_expenses_invoice),
    path('get/', get.get_government_expenses_invoice),
    path('update/<int:pk>/', update.update_government_expenses_invoice),
]

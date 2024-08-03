from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_deposit_cash_to_the_station),
    path('delete/<int:pk>/', delete.delete_deposit_cash_to_the_station),
    path('get/', get.get_deposit_cash_to_the_station),
    path('update/<int:pk>/', update.update_deposit_cash_to_the_station),
]
from django.urls import path
from .create import create_payment_of_the_dead_line
from .delete import delete_payment_of_the_dead_line
from .get import get_payment_of_the_dead_line, get_cash_with_customer_name
from .update import update_payment_of_the_dead_line, update_cash
urlpatterns = [
    path('create/', create_payment_of_the_dead_line),
    path('delete/<int:pk>/', delete_payment_of_the_dead_line),
    path('get/', get_payment_of_the_dead_line),
    path('get-cash/', get_cash_with_customer_name),
    path('update/<int:pk>/', update_payment_of_the_dead_line),
    path('update-cash/<int:pk>/', update_cash)
]

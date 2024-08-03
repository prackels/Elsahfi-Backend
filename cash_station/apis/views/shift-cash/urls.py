from django.urls import path
from .create import create_shift_cash
from .delete import delete_shift_cash
from .get import get_shift_cash
from .update import update_shift_cash

urlpatterns = [
    path('create/', create_shift_cash),
    path('delete/<int:pk>/', delete_shift_cash),
    path('get/', get_shift_cash),
    path('update/<int:pk>/', update_shift_cash),
]

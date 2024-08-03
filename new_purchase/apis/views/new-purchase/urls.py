from .create import create_new_purchase
from .delete import delete_new_purchase
from .get import get_new_purchase, get_purchase_count
from .update import update_new_purchase
from django.urls import path

urlpatterns = [
    path('create/', create_new_purchase),
    path('delete/<int:pk>/', delete_new_purchase),
    path('update/<int:pk>/', update_new_purchase),
    path('get/', get_new_purchase),
    path('new-purchase-count/', get_purchase_count),
]

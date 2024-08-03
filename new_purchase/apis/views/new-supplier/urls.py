from .create import create_new_supplier
from .delete import delete_new_supplier
from .get import get_new_supplier, get_new_supplier_byname
from .update import update_new_supplier
from django.urls import path

urlpatterns = [
    path('create/', create_new_supplier),
    path('delete/<int:pk>/', delete_new_supplier),
    path('update/<int:pk>/', update_new_supplier),
    path('get/', get_new_supplier),
    path('get-byname/<str:supplier_name>/', get_new_supplier_byname),
]
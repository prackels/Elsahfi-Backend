from .apis.views.create import create_codes, create_encrypted_codes
from .apis.views.delete import delete_codes, delete_encrypted_codes
from .apis.views.update import update_codes, update_encrypted_codes
from .apis.views.get import get_codes, get_encrypted_codes, get_codes_by, get_encrypted_employee_codes, get_encrypted_private_codes
from django.urls import path

urlpatterns = [
    path('code/create/', create_codes),
    path('code/delete/<int:pk>/', delete_codes),
    path('code/update/<int:pk>/', update_codes),
    path('code/get/', get_codes),
    path('code/get-byname/<str:code>/', get_codes_by),
    
    path('encrypted-codes/create/', create_encrypted_codes),
    path('encrypted-codes/delete/<int:pk>/', delete_encrypted_codes),
    path('encrypted-codes/get-employee/', get_encrypted_employee_codes),
    path('encrypted-codes/get-private/', get_encrypted_private_codes),
    path('encrypted-codes/update/<int:pk>/', update_encrypted_codes),
    path('encrypted-codes/get/<str:codes_type>/', get_encrypted_codes),

]
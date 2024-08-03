from django.urls import path, include
from . import create, delete, get, update

urlpatterns = [
    path('create/', create.create_official_papers_of_employees_invoice),
    path('delete/<int:pk>/', delete.delete_official_papers_of_employees_invoice),
    path('get/', get.get_official_papers_of_employees_invoice),
    path('update/<int:pk>/', update.update_official_papers_of_employees_invoice),
]

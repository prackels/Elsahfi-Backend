from django.urls import path
from ..apis.views.get import get_repositories
from ..apis.views.delete import delete_repository
from ..apis.views.update import update_repository
from ..apis.views.create import create_repository

urlpatterns = [
    path('get/', get_repositories),
    path('create/', create_repository),
    path('delete/<int:pk>/', delete_repository),
    path('update/<int:pk>/', update_repository),
]

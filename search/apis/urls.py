from django.urls import path
from .views.search import SearchView

urlpatterns = [
    path('',SearchView)
]
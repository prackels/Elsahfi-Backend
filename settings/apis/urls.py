from django.urls import path
from .views import get, create, delete, update

urlpatterns = [
    path('station-information/get/', get.get_basic_information_about_the_station),
    path('station-information/create/', create.create_basic_information_about_the_station),
    path('station-information/update/<int:pk>/', update.update_basic_information_about_the_station),
    path('station-information/delete/<int:pk>/', delete.delete_basic_information_about_the_station),

    path('branch-information/get/', get.get_branches_information),
    path('branch-information/create/', create.create_branches_information),
    path('branch-information/update/<int:pk>/', update.update_branches_information),
    path('branch-information/delete/<int:pk>/', delete.delete_branches_information),

    path('shifts/get/', get.get_shift_details),
    path('shifts/create/', create.create_shift_details),
    path('shifts/update/<int:pk>/', update.update_shift_details),
    path('shifts/delete/<int:pk>/', delete.delete_shift_details),
]
from django.urls import path
from .views.shift.create import CreateShift
from .views.shift.delete import DeleteShift
from .views.shift.get import GetShift, get_last_shift_id

urlpatterns = [
    path('create/',CreateShift),
    path('delete/<str:shift_uid>/',DeleteShift),
    path('get/<str:shift_uid>/',GetShift),
    path("get-last-id/", get_last_shift_id)
]
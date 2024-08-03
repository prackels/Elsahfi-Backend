from django.urls import path
from .views.get import get_all_notifications
from .views.update import read_notification

urlpatterns = [
    path("get-all/", get_all_notifications),
    path("read-notification/<int:noti_id>/", read_notification)
]
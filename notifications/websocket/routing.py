from django.urls import path
from .consumers import NotificationConsumer


websocket_urlpatterns = [
    path('notifications/',NotificationConsumer.as_asgi()),
]
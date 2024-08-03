from rest_framework import serializers
from .models import Notification
from users.models import User


class FromUserSerialzier (serializers.ModelSerializer) : 
    class Meta :
        model = User
        fields = ("id","full_name","email",)

class NotificationSerializer (serializers.ModelSerializer) :
    # from_user = FromUserSerialzier()
    class Meta:
        model = Notification
        fields = "__all__" 
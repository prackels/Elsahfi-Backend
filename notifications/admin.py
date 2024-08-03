from django.contrib import admin
from .models import Notification


class NotiPanel (admin.ModelAdmin) : 
    list_display = ('to_user','from_user','content','read',)

admin.site.register(Notification, NotiPanel)
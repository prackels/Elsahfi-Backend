from django.contrib import admin

from .models import Code, EncryptedCodes

admin.site.register([Code,EncryptedCodes])
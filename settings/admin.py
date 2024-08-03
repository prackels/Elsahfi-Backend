from django.contrib import admin
from .models import ShiftDetails, BranchesInformation, BasicInformationAboutTheStation

admin.site.register(ShiftDetails)
admin.site.register(BranchesInformation)
admin.site.register(BasicInformationAboutTheStation)

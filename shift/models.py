from django.db import models
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
# from globals.invoices_signals import CreateInvoice
# from invoices import models as invoice_models
from settings.models import BranchesInformation
shift_times= (
    ('Morning', 'Morning'),
    ('Evening', 'Evening')
)
class Shift (models.Model):
    branch_number = models.ForeignKey(BranchesInformation, on_delete= models.SET)
    shift_series = models.CharField(max_length=100)
    responsible_series = models.CharField(max_length=100)
    uid = models.UUIDField(null=True,blank=True)
    user = models.CharField(max_length=100)
    date = models.DateField(auto_now_add= True)
    shift_time = models.CharField(max_length=100, choices= shift_times)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.shift_series}, Active : {self.is_active}'

@receiver(post_save,sender=Shift)
def CreateShiftUid (created,instance,**kwargs) : 
    if created:
        instance.uid = uuid4()
        instance.is_active = True
        instance.save()
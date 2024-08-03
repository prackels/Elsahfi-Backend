from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from globals.real_time_activity import SendRealTimeActivity as SendNotification
from shift.models import Shift

### عميل المحطة ###
class StationCustomerInvoice(models.Model):
    sequance= models.AutoField(primary_key= True) # التسلسل
    concernedperson= models.CharField(max_length=100) # صاحب الشأن
    invoice= models.ImageField(upload_to='invoices', null= True, blank= True) # الفاتورة
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'

@receiver(post_save,sender=StationCustomerInvoice)
def send_notification_station(created,instance,**kwargs) : 
    if created : 
        SendNotification(
            noti_type = "receive",
            content="Received new invoices from station section"
        )



### عميل التريلا ###
class TrillaCustomers(models.Model):
    sequance= models.AutoField(primary_key= True) # التسلسل
    concernedperson= models.CharField(max_length=20) # صاحب الشأن
    invoice= models.ImageField(upload_to='invoices', null= True, blank= True) # الفاتورة
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'

@receiver(post_save,sender=TrillaCustomers)
def send_notification_trilla(created,instance,**kwargs) : 
    if created : 
        SendNotification(
            noti_type = "receive",
            content="Received new invoices from treilla section"
        )


### شراء عميل جديد ###
class NewPurchasingClientsInvoice(models.Model):
    sequance= models.AutoField(primary_key= True) # التسلسل
    concernedperson= models.CharField(max_length=20) # صاحب الشأن
    invoice= models.ImageField(upload_to='invoices', null= True, blank= True) # الفاتورة
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'

### عميل الدينا ###
class DeiannaCustomerInvoice(models.Model):
    sequance= models.AutoField(primary_key= True) # التسلسل
    concernedperson= models.CharField(max_length=20) # صاحب الشأن
    invoice= models.ImageField(upload_to='invoices', null= True, blank= True) # الفاتورة
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'

@receiver(post_save,sender=DeiannaCustomerInvoice)
def send_notification_dienna(created,**kwargs) : 
    if created : 
        SendNotification(
            noti_type = "receive",
            content="Received new invoices from dienna section"
        )



### فواتير مصروفات المحطة ###
class StationExpenseInvoice(models.Model):
    sequance= models.AutoField(primary_key= True)
    concernedperson= models.CharField(max_length=20)
    invoice= models.ImageField(upload_to='invoices/station', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'


### مصروفات حكوميه ###
class GovernmentExpensesInvoice(models.Model):
    sequance= models.AutoField(primary_key= True)
    concernedperson= models.CharField(max_length=20)
    renew_the_form= models.ImageField(upload_to='invoices/government/', null= True, blank= True)
    cost_of_license = models.ImageField(upload_to='invoices/government', null= True, blank= True) 
    employee_insurance= models.ImageField(upload_to='invoices/government', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'
    


### الاوراق الرسمية للموظفين ###
class OfficialPapersOfEmployeesInvoice(models.Model):
    sequance= models.AutoField(primary_key= True)
    concernedperson= models.CharField(max_length=20) 
    residence= models.ImageField(upload_to='invoices/official-paper', null= True, blank= True)
    job_contract= models.ImageField(upload_to='invoices/official-paper', null= True, blank= True)
    insurance= models.ImageField(upload_to='invoices/official-paper', null= True, blank= True)
    passport= models.ImageField(upload_to='invoices/official-paper', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.concernedperson}'
        
### فواتير ايداع نقدي المحطة ###
class DepositCashToTheStation(models.Model):
    sequance= models.AutoField(primary_key= True)
    concernedperson= models.CharField(max_length=100)
    invoice= models.ImageField(upload_to='invoices/deposit-cash', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.concernedperson}'
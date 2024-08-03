from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from clients_.models import NewCustomer
from shift.models import Shift
from invoices.models import DepositCashToTheStation
from django.db.models.signals import post_save
class Cash(models.Model):
    customer= models.ForeignKey(NewCustomer, on_delete= models.CASCADE)
    financial_advance= models.FloatField()
    the_amount_required= models.FloatField()
    def __str__(self):
        return f'{self.customer}'
class PaymentOfTheDeadLine(models.Model):
    sequence= models.AutoField(primary_key= True)
    invoice_sequence= models.IntegerField()
    customer_name= models.ForeignKey(NewCustomer, on_delete= models.CASCADE)
    date_of_payment= models.DateField()
    payment_amount= models.FloatField()
    remaining_for_the_station= models.FloatField()
    remaining_for_the_client= models.FloatField()
    payment_method= models.CharField(max_length= 50)
    receipt_img= models.ImageField(upload_to= 'car-cash/payment-of-the-deadline', null= True, blank= True)
    payment_date= models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.SET, blank= True, null= True)
    edited = models.BooleanField(default=False)
    cash= models.ForeignKey(Cash, on_delete= models.CASCADE, null= True, blank= True)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
                
    def __str__(self):
        return f'{self.sequence}- {self.customer_name}'
    
class ShiftCash(models.Model):
    sequence= models.AutoField(primary_key= True)
    shift_sequence= models.IntegerField()
    petty_cash= models.FloatField()
    shift_cash= models.FloatField()
    net_total= models.FloatField()
    total= models.FloatField()
    additions= models.FloatField()
    reason= models.CharField(max_length= 150)
    total_amount= models.FloatField()
    deposit_amount= models.FloatField()
    deposit_officer= models.CharField(max_length= 100)
    receipt_img= models.ImageField(upload_to= 'cash-station/shift-cash', null= True, blank= True)
    payment_date= models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.total}'

@receiver(post_save, sender=ShiftCash)
def create_shift_cash(sender, instance, created, **kwargs):
    if created:
        DepositCashToTheStation.objects.create(
            concernedperson= instance.deposit_officer,
            invoice= instance.receipt_img
        )
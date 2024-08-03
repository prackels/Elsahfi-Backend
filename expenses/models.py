from django.db import models
from django.utils import timezone
from employee.models import Car
from codes.models import Code
from shift.models import Shift
from django.db.models.signals import post_save
from django.dispatch import receiver
from globals.invoices_signals import CreateInvoice
from invoices import models as invoice_models


class StationExpense (models.Model):
    sequence = models.AutoField(primary_key=True)
    invoice_sequence = models.BigIntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_price = models.FloatField()
    quantity = models.IntegerField()
    expense_code = models.ForeignKey(Code, on_delete= models.SET)
    expense_type = models.CharField(max_length=250)
    photo_of_invoice = models.ImageField(upload_to='Photo_of_invoice/', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    notes = models.TextField(null=True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def __str__(self) : 
        return f'{self.name}'
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
                
@receiver(post_save,sender=StationExpense)
def create_invoice_for_station_expenses(created, instance, **kwargs):
    if created :
        CreateInvoice(
            model_class=invoice_models.StationExpenseInvoice,
            concernedperson = str(instance.name),
            invoice = instance.photo_of_invoice
        )

class GovernmentExpense (models.Model):
    sequence = models.AutoField(primary_key=True)
    invoice_number = models.BigIntegerField()
    name = models.CharField(max_length=100)
    expense_code= models.ForeignKey(Code, on_delete= models.SET)
    profession = models.CharField(max_length=100)
    cost_of_license = models.FloatField()
    license_cost_photo = models.ImageField(upload_to='Photo_of_invoice/', null= True, blank= True)
    employee_insurance = models.FloatField()
    employee_insurance_photo = models.ImageField(upload_to='Photo_of_invoice/', null= True, blank= True)
    car_insurance = models.FloatField()
    car_insurance_photo = models.ImageField(upload_to='Photo_of_invoice/', null= True, blank= True)
    renwal_of_form_photo = models.ImageField(upload_to='Renwal_of_form/', null= True, blank= True)
    renwal_of_form = models.FloatField()
    date = models.DateField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    time = models.TimeField(auto_now_add=True)
    notes = models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)

@receiver(post_save,sender=GovernmentExpense)
def create_invoice_for_government_expenses(created, instance, **kwargs):
    if created :
        CreateInvoice(
            model_class=invoice_models.GovernmentExpensesInvoice,
            concernedperson = str(instance.name),
            renew_the_form= instance.renwal_of_form_photo,
            cost_of_license= instance.license_cost_photo,
            employee_insurance= instance.employee_insurance_photo
        )

class CarsExpenses(models.Model):
    sequence = models.AutoField(primary_key=True)
    invoice_sequence = models.BigIntegerField()
    car_type= models.ForeignKey(Car, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    total_price = models.FloatField()
    quantity = models.IntegerField()
    photo_of_invoice = models.ImageField(upload_to='Photo_of_invoice/', null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments = models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)

@receiver(post_save,sender=CarsExpenses)
def create_invoice_for_car_expenses (created, instance, **kwargs) : 
    if created :
        CreateInvoice(
            model_class=invoice_models.StationExpenseInvoice,
            concernedperson = str(instance.name),
            invoice = instance.photo_of_invoice,
        )
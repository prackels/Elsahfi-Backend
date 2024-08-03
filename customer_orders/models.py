from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from invoices import models as invoice_models
from globals.invoices_signals import CreateInvoice
from clients_.models import NewCustomer
from employee.models import Car
from shift.models import Shift
from invoices.models import TrillaCustomers as trilla, DeiannaCustomerInvoice, StationCustomerInvoice
payment_methods= (
    ('Cash', 'Cash'),
    ('Visa', 'Visa'),
    ('Deposit', 'Deposit')

)
subject_names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
)

class CustomerStation(models.Model):
    sequence= models.AutoField(primary_key=True)
    customer_name= models.ForeignKey(NewCustomer, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    previous_quantity= models.FloatField()
    subject_name= models.CharField(max_length= 50, choices= subject_names)
    quantity= models.FloatField()
    price_per_litre= models.FloatField()
    total= models.FloatField()
    packing_method= models.CharField(max_length= 50)
    payment_method= models.CharField(max_length= 50, choices= payment_methods)
    car_type= models.CharField(max_length=100)
    car_plate= models.CharField(max_length=50)
    driver= models.CharField(max_length=100)
    car_photo= models.ImageField(upload_to= 'customer-orders/customer-station/car-photo', null= True, blank= True)
    invoice_photo= models.ImageField(upload_to= 'customer-orders/customer-station/invoice_photo', null= True, blank= True)
    invoice_number = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    invoice_sequence = models.IntegerField()
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, null= True, blank= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.customer_name}'
    
@receiver(post_save,sender=CustomerStation)
def create_invoice_for_customer_station (created, instance, **kwargs) : 
    if created:
        StationCustomerInvoice.objects.create(
            concernedperson = str(instance.customer_name),
            invoice = instance.invoice_photo,
        )

class TrillaCustomer(models.Model):
    sequence= models.AutoField(primary_key=True)
    customer_name= models.ForeignKey(NewCustomer, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    subject_name= models.CharField(max_length= 50, choices= subject_names)
    previous_quantity= models.FloatField()
    quantity= models.FloatField()
    secret_counter= models.FloatField()
    price_per_litre= models.FloatField()
    total= models.FloatField()
    payment_method= models.CharField(max_length= 50, choices= payment_methods)
    packing_method= models.CharField(max_length= 50)
    checkout_counter= models.IntegerField()
    time_to_go_out= models.TimeField()
    client_station_name= models.CharField(max_length=50)
    its_location= models.CharField(max_length=50)
    coordinates= models.TextField()
    car_type= models.ForeignKey(Car, on_delete= models.SET)
    car_plate= models.CharField(max_length=50)
    driver_name= models.CharField(max_length=50)
    tips= models.FloatField()
    value_rent= models.FloatField()
    total_trip= models.FloatField()
    entry_counter= models.IntegerField()
    entry_time= models.TimeField()
    invoice = models.ImageField(upload_to="customer-orders/trilla-customers/", null= True, blank= True)
    invoice_number = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    invoice_sequence = models.IntegerField()
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.customer_name}'

@receiver(post_save,sender=TrillaCustomer)
def create_invoice_for_customer_trilla (created, instance, **kwargs) : 
    if created :
            trilla.objects.create(
            concernedperson = instance.customer_name,
            invoice = instance.invoice
            )

class DeiannaCustomer(models.Model):
    sequence= models.AutoField(primary_key=True)
    customer_name= models.ForeignKey(NewCustomer, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    subject_name= models.CharField(max_length= 50, choices= subject_names)
    previous_quantity= models.FloatField()
    quantity= models.FloatField()
    secret_counter= models.FloatField()
    price_per_litre= models.FloatField()
    total= models.FloatField()
    payment_method= models.CharField(max_length= 50, choices= payment_methods)
    packing_method= models.CharField(max_length= 50)
    checkout_counter= models.IntegerField()
    time_to_go_out= models.TimeField()
    client_station_name= models.CharField(max_length=50)
    its_location= models.CharField(max_length=50)
    coordinates= models.TextField()
    car_type= models.ForeignKey(Car, on_delete= models.SET)
    car_plate= models.CharField(max_length=50)
    driver_name= models.CharField(max_length=50)
    tips= models.FloatField()
    value_rent= models.FloatField()
    total_trip= models.FloatField()
    entry_counter= models.IntegerField()
    entry_time= models.TimeField()
    invoice = models.ImageField(upload_to="customer-orders/deianna-customers/", null= True, blank= True)
    invoice_number = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    invoice_sequence = models.IntegerField()
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.customer_name}'
    
@receiver(post_save,sender=DeiannaCustomer)
def create_invoice_for_customer_dienna (created, instance, **kwargs) : 
    if created :
        DeiannaCustomerInvoice.objects.create(
            concernedperson = instance.customer_name,
            invoice = instance.invoice
            )
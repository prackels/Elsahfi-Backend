from django.db import models
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# from invoices import models as invoice_models
# from globals.invoices_signals import CreateInvoice
from django.db.models.signals import post_save
from shift.models import Shift
from django.core.validators import MinValueValidator, MaxValueValidator
subject_names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
)
class NewSupplier(models.Model):
    sequence= models.AutoField(primary_key=True)
    supplier_name= models.CharField(max_length=100)
    supplier_location= models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    purchase_tax= models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    premium_gasoline_91= models.CharField(max_length= 50, null= True, blank= True)
    purchase_price_per_litre_91= models.FloatField(null= True, blank= True)
    liter_selling_price_91= models.FloatField(null= True, blank= True)
    premium_gasoline_95= models.CharField(max_length= 50, null= True, blank= True)
    purchase_price_per_litre_95= models.FloatField(null= True, blank= True)
    liter_selling_price_95= models.FloatField(null= True, blank= True)
    diesel= models.CharField(max_length= 50, null= True, blank= True)
    purchase_price_per_litre_diesel= models.FloatField(null= True, blank= True)
    liter_selling_price_diesel= models.FloatField(null= True, blank= True)
    sales_tax= models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def _str_(self) : 
        return f'{self.supplier_name}'
    
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)

class NewPurchase(models.Model):
    sequence= models.AutoField(primary_key=True)
    invoice_sequence= models.IntegerField()
    supplier_name= models.ForeignKey(NewSupplier, on_delete= models.SET)
    supplier_location= models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    order_number= models.IntegerField()
    order_date= models.DateField()
    order_time= models.TimeField()
    subject_name= models.CharField(max_length= 50, choices= subject_names)
    price_per_litre= models.FloatField()
    required_quantity= models.FloatField()
    quantity_received= models.FloatField()
    actual_quantity= models.FloatField()
    trumpet_t= models.FloatField()
    actual_quantity_price= models.FloatField()
    the_difference_per_quantity= models.FloatField()
    the_amount_of_evaporation= models.FloatField()
    car_type= models.CharField(max_length=100)
    car_plate= models.CharField(max_length=50)
    driver_name= models.CharField(max_length=100)
    checkout_counter= models.IntegerField()
    time_to_go_out= models.TimeField()
    delivery_location= models.CharField(max_length=200)
    receiving_location= models.CharField(max_length=200)
    entry_counter= models.IntegerField()
    entry_time= models.TimeField()
    tips= models.FloatField()
    value_rent= models.FloatField()
    total_trip= models.FloatField()
    invoice = models.ImageField(upload_to="new-purchase/new-purchase/", null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank= True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def __str__(self) : 
        return f'{self.supplier_name}'
    
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)

from invoices import models as invoice_models
from globals.invoices_signals import CreateInvoice

@receiver(post_save,sender=NewPurchase)
def create_invoice_for_new_sale (created, instance, **kwargs) : 
    if created:
        CreateInvoice(
            model_class=invoice_models.NewPurchasingClientsInvoice,
            concernedperson = instance.supplier_name,
            invoice = instance.invoice)

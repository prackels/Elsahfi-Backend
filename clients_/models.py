from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from shift.models import Shift
subject_names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
    ('Gas', 'Gas'),
    ('Petrol Gas', 'Petrol Gas'),
)

class NewCustomer(models.Model):
    sequence= models.AutoField(primary_key= True)
    customer_name= models.CharField(max_length= 100)
    phone_number = PhoneNumberField()
    financial_advance= models.FloatField()
    payment_date= models.DateField()
    date_of_payment= models.DateField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments= models.TextField(null= True, blank=True)
    blocked= models.BooleanField(default= False, null= True, blank=True)
    pending= models.BooleanField(default= False, null= True, blank=True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.customer_name}'
    
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)

class Cars(models.Model):
    customer= models.ForeignKey(NewCustomer, on_delete= models.CASCADE)
    car_photo= models.ImageField(upload_to= 'cars', null= True, blank= True)
    car_type= models.CharField(max_length= 100, null= True, blank= True)
    car_plate= models.CharField(max_length= 50, null= True, blank= True)
    comments= models.TextField(null= True, blank=True)
    def __str__(self):
        return f"{self.customer} - {self.car_type}"

class Subjects(models.Model):
    customer= models.ForeignKey(NewCustomer, on_delete= models.CASCADE)
    subject_name= models.CharField(max_length= 50, choices= subject_names, null= True, blank= True)
    price_per_liter= models.FloatField(null= True, blank= True)
    comments= models.TextField(null= True, blank=True)
    def __str__(self):
        return f"{self.customer} - {self.subject_name}"

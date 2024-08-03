from django.db import models
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from codes.models import Code, EmployeesCodes
from invoices.models import OfficialPapersOfEmployeesInvoice
from shift.models import Shift
from django.db.models.signals import post_save
class Employee (models.Model) : 
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    phone_number = PhoneNumberField()
    profession = models.CharField(max_length=100)
    driving_license = models.ImageField(upload_to='driving-license-imgs/', null= True, blank= True)
    salary = models.FloatField()
    marital_status = models.CharField(max_length=100, null=True,blank=True)
    type_of_residence = models.CharField(max_length=100)
    beginning_of_residence = models.CharField(max_length=100)
    end_of_residence = models.CharField(max_length=100)
    renewal_of_residence = models.CharField(max_length=100)
    photo_of_residence = models.ImageField(upload_to='photo_of_residence/', null= True, blank= True)
    beginning_of_the_employment_contract = models.DateField()
    end_of_the_employment_contract = models.DateField()
    photo_of_contract = models.ImageField(upload_to='photo_of_contract/', null= True, blank= True)
    insurance_number = models.CharField(max_length=100)
    beginning_of_insurance = models.DateField()
    end_of_insurance = models.DateField()
    photo_of_insurance = models.ImageField(upload_to='Photo_of_insurance/', null= True, blank= True)
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    photo_of_passport = models.ImageField(upload_to='Photo_of_passport/', null= True, blank= True)
    company_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments = models.TextField(null= True, blank= True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.name}'
    
    
@receiver(post_save, sender=Employee)
def create_official_paper_invoice(sender, instance, created,  **kwargs):
    if created:
        OfficialPapersOfEmployeesInvoice.objects.create(
            concernedperson= instance.name,
            residence= instance.photo_of_residence,
            job_contract= instance.photo_of_contract,
            insurance= instance.photo_of_insurance,
            passport= instance.photo_of_passport,
        )
        EmployeesCodes.objects.create(
            name= instance.name
        )
        Code.objects.create(
             name = "موظفين",
             code = instance.code,
             type = "Employee"
        )

class Car(models.Model) : 
    sequence = models.AutoField(primary_key=True)
    type_of_car = models.CharField(max_length=100)
    runnig_cost = models.FloatField()
    car_code = models.CharField(max_length=100, unique= True)
    structure_number = models.FloatField()
    plate_number = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100, unique= True)
    model = models.CharField(max_length=100)
    car_owner = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    comments = models.TextField(null= True, blank= True)
    created_at = models.DateField(auto_now_add=True)
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) : 
        return f'{self.type_of_car} - {self.car_name}'
    

@receiver(post_save, sender=Car)
def create_official_paper_invoice(sender, instance, created,  **kwargs):
    if created:
        Code.objects.create(
            category= instance.car_name,
            code= instance.car_code
        )
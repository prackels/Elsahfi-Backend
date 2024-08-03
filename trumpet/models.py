from django.db import models
from django.dispatch import receiver
from shift.models import Shift
from tank.models import Tank
from django.utils import timezone
from django.db.models.signals import post_save

subjects_names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
)

Subjects_Names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
    ('Gas', 'Gas'),
    ('Liquefied Petroleum Gas', 'Liquefied Petroleum Gas'),
)


class Trumpet(models.Model):
    trumpet_number= models.AutoField(primary_key= True) # التسلسل
    name = models.CharField(max_length=100)
    tank= models.ForeignKey(Tank,on_delete= models.CASCADE)
    subject_name= models.CharField(max_length= 20, choices= subjects_names) # اسم الماده
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))

@receiver(post_save, sender=Tank)
def create_trumpet(sender, created, instance, **kwargs):
    if created:
        for x in range(1, instance.trumpets_count + 1):
            Trumpet.objects.create(
                name= f'الطرومبه {x}',
                tank= instance,
                subject_name= instance.material,
            )

class ReadingTrumpet(models.Model):
    id= models.AutoField(primary_key=True)
    subject_name= models.CharField(max_length= 20, choices= subjects_names) # اسم الماده
    trumpet_number = models.ForeignKey(Trumpet, on_delete=models.CASCADE)
    trumpet_caliber= models.FloatField() # عيار الطرومبه
    receiving_counter= models.FloatField() # عداد الاستلام
    delivery_counter= models.FloatField() # عداد التسليم
    quantity_sold= models.FloatField() # الكميه  المباعه باللتر
    price_per_litre= models.FloatField() # السعر باللتر
    total= models.FloatField() # اجمالي باللتر
    comments= models.TextField(null= True, blank= True) # ملاحظات
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) -> str :
        return f"{self.trumpet_number}"

class ReadingTrumpet_K(models.Model):
    id= models.AutoField(primary_key=True)
    subject_name= models.CharField(max_length= 50, choices= Subjects_Names) # اسم الماده
    trumpet_number = models.ForeignKey(Trumpet, on_delete=models.CASCADE)
    trumpet_caliber= models.FloatField() # عيار الطرومبه
    receiving_counter= models.FloatField() # عداد الاستلام
    delivery_counter= models.FloatField() # عداد التسليم
    quantity_sold= models.FloatField() # الكميه  المباعه باللتر
    price_per_litre= models.FloatField() # السعر باللتر
    total= models.FloatField() # اجمالي باللتر
    comments= models.TextField(null= True, blank= True) # ملاحظات
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) -> str :
        return f"{self.trumpet_number}"
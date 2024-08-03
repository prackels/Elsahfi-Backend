from django.db import models
from shift.models import Shift

subject_names= (
    ('Premium Gasoline 91', 'Premium Gasoline 91'),
    ('Premium Gasoline 95', 'Premium Gasoline 95'),
    ('Diesel', 'Diesel'),
)
class Tank(models.Model):
    tank_name = models.CharField(max_length=100,unique=True)
    tank_quantity= models.FloatField(default=0)
    tank_height = models.FloatField(default=0)
    tank_width = models.FloatField(default=0)
    tank_color = models.CharField(max_length=200, null=True, blank=True)
    material = models.CharField(max_length=100, choices= subject_names)
    tank_caliber = models.FloatField()
    shift= models.ForeignKey(Shift, on_delete= models.CASCADE, blank= True, null= True)
    trumpets_count= models.IntegerField(default= 0)
    edited = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
                self.shift = Shift.objects.filter(is_active=True).last()
                super().save(*args, **kwargs)
    def __str__(self) -> str :
        return f"{self.tank_name}"
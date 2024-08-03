from django.db import models
from django.utils import timezone

class Repository(models.Model):
    sequence = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    comments = models.TextField(null= True, blank= True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    day = models.CharField(max_length=20, default=timezone.now().strftime('%A'))
    created_at = models.DateField(auto_now_add=True)
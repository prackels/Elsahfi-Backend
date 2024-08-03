from django.db import models

CODE_TYPES = (
    ("Private", "Private"),
    ("Employee", "Employee"),
)

class Code(models.Model):
    sequence = models.AutoField(primary_key=True)
    category = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return f'{self.category} - {self.code}'


class EncryptedCodes(models.Model):
    sequence = models.AutoField(primary_key=True)
    category = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    type = models.CharField(max_length=50, choices=CODE_TYPES)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return f'{self.category} - {self.code}'
    
class EmployeesCodes(models.Model):
    code = models.AutoField(primary_key=True)
    name= models.CharField(max_length= 200)
    password= models.CharField(max_length= 200, default= 0)
from django.db import models
from phonenumber_field.modelfields import PhoneNumber

class BasicInformationAboutTheStation(models.Model):
    id= models.AutoField(primary_key=True)
    station_name = models.CharField(max_length= 50)
    def __str__(self):
        return self.station_name

class BranchesInformation(models.Model):
    id= models.AutoField(primary_key=True)
    # station= models.ForeignKey(BasicInformationAboutTheStation, on_delete= models.CASCADE)
    # station= models.CharField(max_length=250)
    branch_number= models.IntegerField()
    license_number= models.CharField(max_length= 100)
    owner_name= models.CharField(max_length= 100)
    commercial_register= models.IntegerField()
    tax_number= models.CharField(max_length= 50)
    phone_number = PhoneNumber()
    def __str__(self):
        return f'{self.branch_number}'

class ShiftDetails(models.Model):
    id= models.AutoField(primary_key= True)
    shift_name= models.CharField(max_length= 100)
    shift_time_from= models.TimeField()
    shift_time_to= models.TimeField()
from django.db import models


# Create your models here.

class PatientInfo(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PatientName = models.CharField(max_length=500)
    DateOfBirth = models.CharField(max_length=500)
    BloodGroup = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    InsuranceID = models.CharField(max_length=100)

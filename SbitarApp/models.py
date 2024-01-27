from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    specialty = models.CharField(max_length=255,null=True)
    experience = models.CharField(max_length=3,null=True)  
    email = models.CharField(max_length=50,null=True)  
    gender = models.CharField(max_length=15,null=True)  
    phone_number = models.CharField(max_length=15,null=True)  
    dob = models.DateField(null=True) 

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=50,null=True)  
    gender = models.CharField(max_length=15,null=True)  
    phone_number = models.CharField(max_length=15,null=True)  
    dob = models.DateField(null=True) 

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=10)
    hospitalization = models.CharField(max_length=3)
    problem = models.TextField()
    status = models.CharField(max_length=15,default='pending')



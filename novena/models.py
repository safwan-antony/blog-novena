from django.db import models
from django.contrib.auth.models import AbstractUser 
from a_users.models import User
from novena_dash.models import Departement , Doctor , My_Educational

# Create your models here.
class Patient(User):
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50 ,null=True , blank=True)
    country = models.CharField(max_length=50 ,null=True)
    medical_history = models.TextField(max_length=500, blank=True , null=True)
    patient_pic=models.ImageField(upload_to='patient_pics', blank=True, null=True)
    
    def __str__(self):
        return self.last_name
    class Meta:
        managed = True

class Appoinment(models.Model):
    department = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE , null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    day = models.DateField(null=True)
    time = models.TimeField(null=True)
    full_name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=100,null=True,default='pending')
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
       
class Message(models.Model):
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE , null=True , related_name='patient_message')
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE , null=True , related_name='doctor_message')
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:10]


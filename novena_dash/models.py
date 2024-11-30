from django.db import models
from a_users.models import User


# Create your models here.

class Departement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500 , null=True , blank=True)

    def __str__(self):
        return self.name

class Doctor(User): 
    doctor_pic= models.ImageField(upload_to='patient_pic',null=True , blank=False)
    departement = models.ForeignKey(Departement,on_delete=models.SET_NULL,null=True)
    certificate = models.FileField(upload_to='certificate',null=True , blank=True)
    descriptions = models.TextField(null=True )
    skills = models.CharField(max_length=400,null=True , blank=True)
    expertise_area=models.CharField(max_length=200,null=True)

    class Meta :
        managed = True

class My_Educational(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100,null=True)
    expertise_area=models.CharField(max_length=200,null=True)
    year = models.CharField(max_length=100,null=True)
    descript = models.TextField(null=True,blank=True) 

    def __str__(self):
        return self.degree
    

    

    




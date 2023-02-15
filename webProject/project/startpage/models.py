from datetime import datetime
from django.db import models
from django import forms

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    gpa=models.DecimalField(max_digits=3,decimal_places=2)
    birth=models.DateField(default=datetime.now)
    email=models.EmailField(blank=True,null=True)
    mobNum=models.PositiveBigIntegerField(blank=True,null=True)
    level=models.IntegerField(null=True)
    active=models.BooleanField(default=True)
    department=models.CharField(max_length=3,blank=True,null=True)
    gender=models.CharField(max_length=6,default='Male')
    #complaint=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class Complaints(models.Model):
    type=models.CharField(max_length=12)
    stuID=models.IntegerField(default=0)
    content=models.TextField()
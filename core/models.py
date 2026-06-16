from django.db import models

class student(models.Model):
    Id=models.IntegerField
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
 
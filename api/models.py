# from django.db import models
from rest_framework import serializers
from django.db import models
import json


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    # class Meta:
    #     abstract = True

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
   
    # hobbies = models.ArrayField(model_container=Author,
    #     blank=True,
    #     null=True
    # )
    





# Create your models here.
# class Employee(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=30)
#     # phone = models.CharField(max_length=20 ,default='')
#     address = jsonfield.JSONField()

#     class Meta:
#         db_table="employee_tbl"
        
#  git branch -M main
# git remote add origin https://github.com/divyeshpandav/Broadview.git
# git push -u origin main
from django.db import models
from django.contrib import auth

# Create your models here.
class subscriptions(models.Model):
    # id=models.IntegerField()
    businessid=models.CharField(max_length=50)

class admin_access(models.Model):
    # id=models.IntegerField(primary_key=True)
    gstin=models.CharField(max_length=15)
    owner=models.CharField(max_length=70)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    businessname=models.CharField(max_length=70)
    businessid=models.OneToOneField(on_delete=models.CASCADE, to='subscriptions')

# class User(auth.models):
#     email=models.EmailField()
    

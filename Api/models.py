from asyncio.windows_events import NULL
from sqlite3 import Timestamp
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    #------------Customer Suppot -----------
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=14)
    desc = models.TextField()
    def __str__(self):
        return self.email
class Customer(models.Model):
    #-----------User Details ---------------------
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=40,unique=True)
    password=models.CharField(max_length=40)
    phone = models.CharField(max_length=14,unique=True)
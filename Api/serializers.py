# from datetime import timezone
from django.db import models
from django.utils.translation import check_for_language
from rest_framework import fields, serializers
from .models import Contact
from .models import Customer

class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','name','email','phone','desc']


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','username','email','password','phone',]


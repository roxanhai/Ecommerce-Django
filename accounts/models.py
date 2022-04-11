from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.
# class Staff(models.Model):

#CUSTOMER => Processing
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer',null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True) 
    totalPay = models.FloatField(default=0)
    active_status = models.BooleanField(default=False)
    fullName = models.CharField(max_length=255)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'staff',null=True, blank=True)
    fullName = models.CharField(max_length=255)
    yearExp = models.IntegerField(default=0)
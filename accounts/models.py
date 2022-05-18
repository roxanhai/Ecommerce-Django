from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# from orderCart.models import Order
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
    
    class Meta:
        verbose_name_plural= 'Customer'
        
    def __str__(self):
        return str(self.id) +"."+self.fullName
    
    @property
    def get_cart_total_quantity(self):
        for temp_order in self.order_set.all():
            if temp_order.completedStatus == False:
                return temp_order.get_cart_total_quantity
        return 0
    

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'staff',null=True, blank=True)
    fullName = models.CharField(max_length=255)
    yearExp = models.IntegerField(default=0)
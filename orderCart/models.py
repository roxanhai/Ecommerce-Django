from django.db import models
from product.models import *
from accounts.models import *

#ORDER => Done
class Order(models.Model):
    STATUS_CHOICE =[
        ('True','True'), ('False','False')
    ]
    PAYMENT_CHOICE = [
        ('Online','Online'), ('Offline','Offline')
    ]
    date_ordered = models.DateTimeField(auto_now_add=True)
    shippingStatus = models.CharField(choices=STATUS_CHOICE,max_length=5)
    paymentMethod =  models.CharField(choices=PAYMENT_CHOICE,max_length=20,null=True)
    paymentStatus = models.CharField(choices=STATUS_CHOICE,max_length=5)
    completedStatus = models.BooleanField(default=False,null=True, blank=True)

class OrderItem(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True) 

#SHIP => DONE
class AddressShip(models.Model):
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    
class Shipment(models.Model):
    TRANSPORST_CHOICE = [
        ('GHTK','GIAO HANG TIET KIEM'), ('J&T','J&T'), ('VNPT','VNPT')
    ]
    shipmentID = models.ForeignKey(AddressShip, on_delete=models.SET_NULL,null=True)
    transportationType =  models.CharField(choices=TRANSPORST_CHOICE,max_length=50,null=True)
    shipFee = models.FloatField(default=0)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(default=None)
    orderID = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)

    

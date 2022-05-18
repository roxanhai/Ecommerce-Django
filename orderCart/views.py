from django.shortcuts import render
from ctypes import addressof
from email.headerregistry import Address
import json
import json.decoder
from sre_parse import State
from types import CoroutineType
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def addToCart(request): 
    #Request.body trả về dưới dạng byte 
    if request.user.is_authenticated:
        responseJson = request.body.decode('utf-8')
        data = json.loads(responseJson)
        productId = data['productId']
        action = data['actions']
        quantity_select = int(data['quantity'])
        print('Action: ',action)
        print('Product: ', productId)
        print("Quantity: ", quantity_select)
        customer = request.user.customer
        print("Customer: ", customer)
        product = Item.objects.get(id = productId)
        print(product)
        order , created = Order.objects.get_or_create(customer=customer,completedStatus = False)
        order_item, created = OrderItem.objects.get_or_create(orderID=order,itemID=product)
        

        if action=='add':
            order_item.quantity += quantity_select
        elif action=='remove':
            order_item.quantity -=1
        
        order_item.save()
        if(order_item.quantity<=0):
            order_item.delete()
    return JsonResponse('Item was added to cart', safe=False)

def cart(request):
    customer = request.user.customer
    order,created = Order.objects.get_or_create(customer=customer, completedStatus = False)
    list_order_item = order.orderitem_set.all()
    context = {
        "order": order,
        "order_list": list_order_item,
    }
    return render(request,"orderCart/cart.html", context)

def checkout(request):
    context = {
    }
    return render(request,"orderCart/checkout.html", context)
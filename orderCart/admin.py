from django.contrib import admin
from orderCart.models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(AddressShip)
admin.site.register(Shipment)
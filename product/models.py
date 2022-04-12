from email.policy import default
from random import choices
from django.db import models
from accounts.models import *
from django.forms import CharField, IntegerField
from django.forms import ImageField, DateTimeField
# ITEM => DONE
class Item(models.Model):
    name = models.CharField(max_length=255)
    outPrice = models.FloatField()
    state = models.CharField(max_length=255)
    storage_quantity = models.IntegerField(default=0)
    available_status = models.BooleanField(default=False)
    imageItem = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True) 
    description = models.CharField(max_length=255)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url 
    
class FeedBack(models.Model):
    content = models.CharField(max_length=255)
    star_rate = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 5)])
    date_added = models.DateTimeField(auto_now_add=True) 
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True) 
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

# BOOK  => DONE
class Publisher(models.Model):
    license = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)
    yearExp = models.IntegerField()

class CategoryBook(models.Model):
    name = models.CharField(max_length=255)
    ageLimit = models.IntegerField(default=0)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    inPrice = models.FloatField(default=0)
    publishYear = models.IntegerField()
    publisher = models.CharField(max_length=255)
    itemID = models.OneToOneField(Item, on_delete=models.CASCADE)
    publisherID = models.ForeignKey(Publisher, on_delete=models.SET_NULL, unique=False,null=True)
    CategoryBookID = models.ForeignKey(CategoryBook, on_delete=models.SET_NULL, unique=False, null=True)
    authorID = models.ForeignKey(Author,on_delete=models.SET_NULL, unique=False,null=True)

#ELECTRONIC (Mobile, TV, Laptop) => DONE
class Brand(models.Model):
    name = models.CharField(max_length=255)
    description =  models.CharField(max_length=255)
    area =  models.CharField(max_length=255)

class Electronic(models.Model):
    CATEGORY_CHOICE = [
        ('MB','MobliePhone'),('TV','Television'),('Clothes','Clothes')
    ]
    guarantee = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    Category = models.CharField(choices=CATEGORY_CHOICE,max_length=20)
    itemID = models.OneToOneField(Item, on_delete=models.CASCADE)
    
class MobilePhone(models.Model): 
    name =  models.CharField(max_length=255)
    screenSize = models.FloatField(default=0)
    ram = models.IntegerField(default=4)
    memory = models.IntegerField(default=64)
    color =  models.CharField(max_length=255)
    
    inPrice = models.FloatField(default=0)
    brandID= models.ForeignKey(Brand,on_delete=models.SET_NULL, unique=False, null=True)
    electronicID = models.OneToOneField(Electronic, on_delete=models.CASCADE)

class Television (models.Model): 
    
    SCREEN_SOLUTION_CHOICE =[
        ("HD","HD") ,("HD_PLUS","HD+"),("FHD","FullHD") ,("QHD","2K") ,("UHD","4K"),
    ]
    
    screenSize = models.FloatField(default=0)
    screenResolution = models.CharField(choices=SCREEN_SOLUTION_CHOICE, max_length=10)
    
    name =  models.CharField(max_length=255)
    
    inPrice = models.FloatField(default=0)
    brandID = models.ForeignKey(Brand,on_delete=models.SET_NULL, unique=False, null=True)
    electronicID = models.OneToOneField(Electronic, on_delete=models.CASCADE)

class Laptop (models.Model):
    HARDWARE_CHOICE = [
        ("HDD","HDD"),("SDD","SDD")
    ]
    
    SCREEN_SOLUTION_CHOICE =[
        ("HD","HD") ,("HD_PLUS","HD+"),("FHD","FullHD") ,("QHD","2K") ,("UHD","4K"),
    ]
    hardWareSize = models.IntegerField(default=128)
    hardWareType = models.CharField(choices=HARDWARE_CHOICE, max_length=3)

    screenSize = models.FloatField(default=0)
    screenResolution = models.CharField(choices=SCREEN_SOLUTION_CHOICE, max_length=10)
   
    cpu = models.CharField(max_length=255)
    ram = models.IntegerField(default=8)
    name = models.CharField(max_length=255)
    
    inPrice = models.FloatField(default=0)
    brandID = models.ForeignKey(Brand,on_delete=models.SET_NULL, unique=False, null = True)
    electronicID = models.OneToOneField(Electronic, on_delete=models.CASCADE)
    
# CLOTHES => DONE
class CategoryClothes(models.Model):
    GENDER_CHOICE = [
        ('Male','Male'), ('Female','Female'), ('Unisex','Unisex')
    ]
    category_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICE,max_length=10)
    
class Clothes(models.Model):
    SIZE_CHOICE =[
         ('S','S'), ('M','M'), ('L','L'),  ('XL','XL'),  ('M','M'),  ('XL','XL'),
         ('2XL','2XL'),  ('3XL','3XL'),
         
    ]
    size = models.CharField(choices=SIZE_CHOICE,max_length=5)
    
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
   
    color = models.CharField(max_length=255)
    inPrice = models.FloatField(default=0)




    
    
    
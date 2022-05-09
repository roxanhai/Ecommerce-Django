from django.shortcuts import render
from accounts.models import *
from product.models import *
from orderCart.models import *
# Create your views here.

def home(request):
    itemList = Item.objects.filter(is_Featured=True).order_by('-id')
    context = {
        "itemList" : itemList,
    }
    return render(request,'store/index.html',context)

def category_list(request):
    itemList = Item.objects.all().order_by('-id')
    context = {
        "itemList" : itemList,
    }
    return render(request, 'store/category_list.html', context)

def brand_list(request):
    brandList = Brand.objects.all().order_by('-id')
    context ={
        "brandList": brandList,
    }
    return render(request, 'store/brand_list.html',context)

def product_list(request):
    itemList = Item.objects.all().order_by('-id')
    brandList = Brand.objects.all().order_by('-id') 
    context = {
        "itemList" : itemList,
        "brandList": brandList,
    }
    return render(request, 'store/product_list.html', context)

#Product_list based on Category
def category_product_list(request, state_Id):
    state = CategoryItem.objects.get(id=state_Id)
    print(state)
    data = Item.objects.filter(state_Id=state).order_by("-id")
    context = {
        "data" : data,
    }
    return render(request,"store/category_product_list.html", context)
    
#Product Detail 
def product_detail(request, item_Id):
    data = Item.objects.get(id=item_Id)
    real_life_item = None
    if data.state_Id.name == "BOOK":
        real_life_item = Book.objects.get(itemID=data)
    elif data.state_Id.name == "ELECTRONIC":
        real_life_item = Electronic.objects.get(itemID=data)
    elif data.state_Id.name == "CLOTHES":
        real_life_item = Clothes.objects.get(itemID=data)
    context = {
       "data": data,
       "data_item": real_life_item
    }
    return render(request,"store/product_detail.html",context)

def search(request):
    searchProduct = request.GET['searchProduct']
    itemList = Item.objects.filter(name__icontains = searchProduct).order_by('-id')
    context = {
        "itemList" : itemList,
    }
    return render(request,'store/search.html',context)
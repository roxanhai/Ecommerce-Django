from ctypes import addressof
from email.headerregistry import Address
import json
import json.decoder
from sre_parse import State
from types import CoroutineType
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
# from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR Password is in corrrect')
        context={}
        return render(request,'accounts/login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('store')
    else: 
        # form = CreateUserForm()
        # if request.method == 'POST':
        #     # form = CreateUserForm(request.POST)
        #     # print(username)
        #     if form.is_valid():
        #         user = form.save()
        #         username = form.cleaned_data.get('username')
        #         email = form.cleaned_data.get('email')
        #         Customer.objects.create(name=username, email=email, user=user)
        #         messages.success(request,'Account was create for: ' + username)
        #         return redirect('login')
        
        # context={'form':form}
        context = {}
        return render(request,'accounts/register.html',context)
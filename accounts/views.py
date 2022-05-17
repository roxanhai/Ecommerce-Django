from ctypes import addressof
from email.headerregistry import Address
import json
import json.decoder
from sre_parse import State
from types import CoroutineType
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def loginPage(request):
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

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else: 
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                full_name = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
                print(full_name)
                Customer.objects.create(fullName=full_name, user=user)
                messages.success(request,'Account was create for: ' + full_name)
                return redirect('login')
        
        context={'form':form}
        return render(request,'accounts/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')
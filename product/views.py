import email
from pickletools import read_string1
from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Item
from . models import models
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import login,authenticate

from product import forms

# Create your views here.
def item(request):
    items=Item.objects.all()
    return render(request,'base.html',{'items':items})

# def login(request):
    # if request.method=='POST':
        # return render(request,'login.html')

    # else:
        # email=request.POST.get('email')
        # password=request.POST.get('password')

        # return render(request,'login.html')

def order(request):
    if request.method=='GET':
        return render(request,'order.html')

    else:
        return HttpResponse("Order Placed")

def item(request):
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})        

def home(request):
        return render(request,'home.html')

def contact(request):
        return render(request,'contact.html')

def about(request):
        return render(request,'about.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(username=username,password=pwd)
            login(request,user)
            return redirect('home.html')

    form=SignupForm
    return render(request, 'registration/signup.html',{'form':form})       
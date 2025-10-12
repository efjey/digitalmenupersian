from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def start(request):
    all_products = Product.objects.all()
    
    return render(request, 'index.html', {'products':all_products})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request, ("نام کاربری یا رمز عبور اشتباه است"))
            return redirect("login_user")

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "با موفیقت خارج شدید")
    return render(request, "index.html", {})
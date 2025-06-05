from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'usersapp/homepage.html')



def my_login_page(request):
     if request.method == "POST":
        usrname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=usrname, password=pwd)
        if user is not None:
            print(user.username)
            login(request, user)
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password")
     return render(request, 'usersapp/login.html')
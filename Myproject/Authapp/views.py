from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                messages.success(request,"User successfully registered")
                return redirect('login') 
            except:
                messages.error(request, "Username already exists")
        else:
            messages.error(request, "Passwords do not match")
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'registration/login.html') 

def logout_view(request):
    logout(request)
    return redirect('login')



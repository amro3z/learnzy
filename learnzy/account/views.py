from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')  
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'account/login.html')
        
    return render(request, 'account/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['name']
        
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name = full_name
        user.save()
        
        
        login(request, user)

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')  
    
    return render(request, 'account/register.html')

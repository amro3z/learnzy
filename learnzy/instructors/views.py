from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Profile, Courses

def instructor_register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(user=user, is_instructor=True)
        
        messages.success(request, 'Instructor account created successfully!')
        return redirect('instructor_login')
    
    return render(request, 'instructors/instructor_register.html')

def instructor_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.profile.is_instructor:
            auth_login(request, user)
            return redirect('instructor_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an instructor')
    
    return render(request, 'instructors/instructor_login.html')

@login_required
def instructor_dashboard_view(request):
    if not request.user.profile.is_instructor:
        return HttpResponseForbidden("You are not authorized to view this page")
    
    courses = Courses.objects.filter(instructor=request.user)
    return render(request, 'instructors/instructor_dashboard.html', {'courses': courses})
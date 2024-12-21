from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Profile, Courses
from .forms import CourseForm
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


@login_required
def add_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            messages.success(request, 'Course added successfully!')
            return redirect('instructor_dashboard')
    else:
        form = CourseForm()
    return render(request, 'instructors/add_course.html', {'form': form})

@login_required
def delete_course_view(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if course.instructor == request.user:
        course.delete()
        messages.success(request, 'Course deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this course')
    return redirect('instructor_dashboard')
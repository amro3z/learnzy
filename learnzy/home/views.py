from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .models import Courses, Enrollments
from django.core.mail import send_mail
from django.contrib import messages
from .models import Teacher


@login_required(login_url='/account/login/')
def index(requset):
    course = Courses.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'course':course ,
        'teacher':teacher
        }
    return render(requset ,'home/inedx.html', context)


def course_info(request, pk):
    course_info = get_object_or_404(Courses, id=pk)
    is_enrolled = False

    if request.user.is_authenticated:
        is_enrolled = Enrollments.objects.filter(username=request.user.id, course_id=pk).exists()

    return render(request, 'home/course.html', {'course_info': course_info, 'is_enrolled': is_enrolled})


def enroll_in_course(request, course_id):
    course = get_object_or_404(Courses, id=course_id)  # Get the course
    user_id = request.user.id  # Use user ID as `username` in the model

    # Check if the user is already enrolled
    if Enrollments.objects.filter(username=user_id, course_id=course_id).exists():
        return redirect('course', pk=course_id)  # Redirect if already enrolled

    # Add a new enrollment record
    Enrollments.objects.create(
        username=user_id,
        course_id=course_id,
        enrolled_at=now()
    )

    # Redirect to the course page
    return redirect('course', pk=course_id)

def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'home/profile.html', {'error': 'You need to log in to view this page.'})

   
    user = request.user

    
    enrollments = Enrollments.objects.filter(username=user.id) 
    enrolled_courses_ids = enrollments.values_list('course_id', flat=True)  
    enrolled_courses = Courses.objects.filter(id__in=enrolled_courses_ids)  

    
    context = {
        'user': user,  
        'enrolled_courses': enrolled_courses  
    }
    return render(request, 'home/profile.html', context)




def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send email (or save to database)
        send_mail(
            f'Message from {name}',  # Subject
            message,  # Message
            email,  # From email
            ['your_email@example.com'],  # To email
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')
    
    return render(request, 'home/inedx.html')





from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .models import Courses, Enrollments
# from .models import Courses
from .models import Teacher
# Create your views here.

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


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Courses
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


def course_info(requset, pk):

    course_info = Courses.objects.get(id=pk)


    return render(requset ,'home/course.html', {'course_info':course_info} )

from django.shortcuts import render
from .models import Courses
from .models import Teacher
# Create your views here.
def index(requset):
    course = Courses.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'course':course ,
        'teacher':teacher
        }
    return render(requset ,'home/inedx.html', context)
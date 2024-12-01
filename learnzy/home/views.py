from django.shortcuts import render
from .models import Courses
# Create your views here.
def index(requset):
    course = Courses.objects.all()
    x = {'course':course}
    return render(requset ,'home/inedx.html',x)
from django.contrib import admin
from .models import Courses
from .models import Teacher
from .models import Enrollments
# Register your models here.
admin.site.register(Courses)
admin.site.register(Teacher)
admin.site.register(Enrollments)

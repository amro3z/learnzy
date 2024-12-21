from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_courses')
    video_url = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'courses'


class Teacher(models.Model):
    name  = models.CharField(max_length=50)
    about = models.CharField(max_length=250)
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    course_id = models.IntegerField()
    enrolled_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollments'

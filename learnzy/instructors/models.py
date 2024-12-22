from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_courses')
    video_url = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'courses'
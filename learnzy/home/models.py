from django.db import models

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    instructor_id = models.IntegerField()
    category_id = models.IntegerField()
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
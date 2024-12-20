from django.urls import path

from . import views

urlpatterns= [
    
    path('',views.index, name ='index'),
    path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),
    path('course/<int:pk>' ,views.course_info, name='course'),
    path('profile/' ,views.profile, name='profile'),
]
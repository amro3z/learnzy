from django.urls import path

from . import views

urlpatterns= [
    
    path('',views.index, name ='index'),
    path('course/<int:pk>' ,views.course_info, name='course'),
]
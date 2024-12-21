from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.instructor_register_view, name='instructor_register'),
    path('login/', views.instructor_login_view, name='instructor_login'),
    path('dashboard/', views.instructor_dashboard_view, name='instructor_dashboard'),
    # path('add_course/', views.add_course_view, name='add_course'),
    # path('delete_course/<int:course_id>/', views.delete_course_view, name='delete_course'),
]
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Courses

class HomeViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_index_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome Back!")


    def test_enroll_in_course_view(self):
        course = Courses.objects.create(title="Test Course", instructor=self.user)
        response = self.client.get(reverse('enroll_in_course', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enroll in Test Course")

    def test_course_info_view(self):
        course = Courses.objects.create(title="Test Course", instructor=self.user)
        response = self.client.get(reverse('course', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Course")

    def test_profile_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Profile")

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Us")
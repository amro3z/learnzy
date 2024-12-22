from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Courses, Profile

class InstructorsViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, is_instructor=True)  # Ensure the user is an instructor
        self.client.login(username='testuser', password='12345')

    def test_instructor_register_view(self):
        response = self.client.get(reverse('instructor_register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instructor Register")

    def test_instructor_login_view(self):
        response = self.client.get(reverse('instructor_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instructor Login")

    def test_instructor_dashboard_view(self):
        response = self.client.get(reverse('instructor_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instructor Dashboard")

    def test_add_course_view(self):
        response = self.client.get(reverse('add_course'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Course")

    def test_delete_course_view(self):
        course = Courses.objects.create(title="Test Course", instructor=self.user)
        response = self.client.post(reverse('delete_course', args=[course.id]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after deletion
        self.assertRedirects(response, reverse('instructor_dashboard'))
        self.assertFalse(Courses.objects.filter(id=course.id).exists())
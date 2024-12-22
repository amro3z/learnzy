from django.test import TestCase
from django.urls import reverse
from .models import Courses

class InstructorsViewTests(TestCase):
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
        course = Courses.objects.create(name="Test Course")
        response = self.client.get(reverse('delete_course', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Delete Course")
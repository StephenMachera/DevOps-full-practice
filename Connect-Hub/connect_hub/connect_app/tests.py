from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class UserTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_signup_creates_user_and_profile(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after signup
        user = User.objects.get(username='testuser')
        profile = UserProfile.objects.get(user=user)
        self.assertIsNotNone(profile)
    def test_login_with_valid_credentials(self):
        User.objects.create_user(username='testuser', password='Testpass123!')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
    def test_login_with_invalid_credentials(self):
        User.objects.create_user(username='testuser', password='Testpass123!')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'WrongPass!'
        })
        self.assertEqual(response.status_code, 200)  # Stay on login page
        self.assertContains(response, "Invalid username or password.")
    def test_dashboard_access_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        User.objects.create_user(username='testuser', password='Testpass123!')
        self.client.login(username='testuser', password='Testpass123!')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)  # Access granted
    
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from .forms import SignUpForm, LoginForm

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpass", email="testuser@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpass"))

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class SignupViewTest(TestCase):
    def test_signup_view_renders_correct_template(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_signup_form_valid_submission(self):
        data = {
            "username": "newuser",
            "password1": "complexpassword123",
            "password2": "complexpassword123",
        }
        response = self.client.post(reverse("accounts:signup"), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(CustomUser.objects.filter(username="newuser").exists())

class LoginViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="testpass")

    def test_login_view_renders_correct_template(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_login_valid(self):
        response = self.client.post(reverse("accounts:login"), {"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 302)  # Redirect after login

class ChangePasswordViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_password_change(self):
        data = {
            "old_password": "testpass",
            "new_password1": "newpassword123",
            "new_password2": "newpassword123",
        }
        response = self.client.post(reverse("accounts:user_update"), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newpassword123"))

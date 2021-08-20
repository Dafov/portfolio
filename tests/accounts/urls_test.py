from portfolio.accounts.views import LoginUserView, RegisterView, logout_user
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    
    def test_login_url_is_resolved(self):
        url = reverse('log in user')
        self.assertEqual(resolve(url).func.view_class, LoginUserView)

    def test_logout_url_is_resolved(self):
        url = reverse('log out user')
        self.assertEqual(resolve(url).func, logout_user)

    def test_register_url_is_resolved(self):
        url = reverse('register user')
        self.assertEqual(resolve(url).func.view_class, RegisterView)
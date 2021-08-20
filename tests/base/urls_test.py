from portfolio.base.views import HomeView, ResumeView
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse('hero')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_resume_url_is_resolved(self):
        url = reverse('resume')
        self.assertEqual(resolve(url).func.view_class, ResumeView)

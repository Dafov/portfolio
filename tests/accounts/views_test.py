import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase, Client
from django.urls.base import reverse


class TestView(TestCase):
    
    def test_home_view_after_successful_login_template(self):
        client = Client()
        response = client.get(reverse('hero'))
        self.assertEqual(response.status_code, 200)
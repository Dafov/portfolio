import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase


class SampleTest(TestCase):
    
    def test_true(self):
        self.assertTrue(True)
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from portfolio.contact.forms import MessageForm
from django.test import TestCase



class TestForms(TestCase):
    def test_comment_form_valid_data(self):
        form = MessageForm({
            'name': 'Test',
            'email': 'test@test.test',
            'subject': 'Test',
            'body': 'Test',
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_has_no_data(self):
        form = MessageForm({})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
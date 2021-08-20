import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase, Client
from portfolio.accounts.forms import  LoginForm, RegisterForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TestRegisterForms(TestCase):
    def test_comment_form_valid_data(self):
        form = RegisterForm({
            'email': 'test@test.test',
            'password1': '12345asdf',
            'password2': '12345asdf',
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_has_no_data(self):
        form = RegisterForm({})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


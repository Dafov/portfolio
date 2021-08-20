from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class PortfolioTestCase(TestCase):
    logged_in_user_email = 'test@test.test'
    logged_in_user_password = 'test1234test'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
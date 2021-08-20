from django.urls.base import reverse
from portfolio.contact.models import Message
from tests.common.mixins import UserTestUtils
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase, Client


class TestViews(TestCase, UserTestUtils):
    def setUp(self):
        self.client = Client()
        self.message_list = reverse('inbox')
        self.detail_message = reverse('message', args=['bd1f1eca-01f0-11ec-9a03-0242ac130003'])

        
        self.message1 = Message.objects.create(
            name = 'Georgi',
            email = 'test@gogo@test',
            subject = 'New Mail',
            body = 'Hello',
            id = 'bd1f1eca-01f0-11ec-9a03-0242ac130003',
        )

    def test_message_list_GET(self):
        response = self.client.get(self.message_list)
        self.assertEquals(response.status_code, 302)

    def test_message_details_GET(self):
        response = self.client.get(self.detail_message)
        self.assertEquals(response.status_code, 302)
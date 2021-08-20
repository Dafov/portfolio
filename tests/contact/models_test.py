from portfolio.contact.models import Message
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):

        self.message1 = Message.objects.create(
            name = 'Georgi',
            email = 'test@gogo@test',
            subject = 'New Mail',
            body = 'Hello',
            id = 'bd1f1eca-01f0-11ec-9a03-0242ac130003',
        )

    def test_message_is_created_properly(self):
        self.assertEquals(self.message1.name, 'Georgi')
        self.assertEquals(self.message1.email, 'test@gogo@test')
        self.assertEquals(self.message1.subject, 'New Mail')
        self.assertEquals(self.message1.body, 'Hello')
        self.assertEquals(self.message1.id, 'bd1f1eca-01f0-11ec-9a03-0242ac130003')

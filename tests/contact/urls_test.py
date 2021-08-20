from portfolio.contact.views import CreateMessageView, DeleteMessageView, InboxPageView, MessageDetailView 
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    
    def test_create_message_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, CreateMessageView)

    def test_inbox_url_is_resolved(self):
        url = reverse('inbox')
        self.assertEqual(resolve(url).func.view_class, InboxPageView)

    def test_message_view_url_is_resolved(self):
        url = reverse('message', args=['some-id'])
        self.assertEqual(resolve(url).func.view_class, MessageDetailView)

    def test_delete_message_view_url_is_resolved(self):
        url = reverse('delete message', args=['some-id'])
        self.assertEqual(resolve(url).func.view_class, DeleteMessageView)
        
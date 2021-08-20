from portfolio.portfolio_projects.views import CreateProjectView, ListProjectsView
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):
    
    def test_list_projects_url_is_resolved(self):
        url = reverse('list projects')
        self.assertEqual(resolve(url).func.view_class, ListProjectsView)

    def test_create_project_url_is_resolved(self):
        url = reverse('create project')
        self.assertEqual(resolve(url).func.view_class, CreateProjectView)

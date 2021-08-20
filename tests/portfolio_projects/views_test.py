from django.test.testcases import TestCase, Client
from portfolio.portfolio_projects.models import Project
from django.urls import reverse
from tests.common.mixins import UserTestUtils
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


class TestViews(TestCase, UserTestUtils):
    def setUp(self):
        self.client = Client()
        self.project_list = reverse('list projects')
        self.detail_project = reverse('details project', args=['1'])
        project_user = self.create_user(
            email='project@user.com', password='testproject')

        self.project1 = Project.objects.create(
            title='1',
            description='description',
            link='https://google.com',
            image='path/to/image.png',
            user=project_user,
            id='1',
        )

    def test_projects_list_GET(self):
        response = self.client.get(self.project_list)
        self.assertEquals(response.status_code, 200)

    def test_projects_details_GET(self):
        response = self.client.get(self.detail_project)
        self.assertEquals(response.status_code, 200)

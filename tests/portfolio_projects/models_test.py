from django.test.testcases import TestCase
from portfolio.portfolio_projects.models import Project, Comment
from tests.common.mixins import UserTestUtils
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()


class TestModels(TestCase, UserTestUtils):
    def setUp(self):
        project_user = self.create_user(
            email='project@user.com', password='testproject')

        self.project1 = Project.objects.create(
            title = 'Title',
            description = 'description',
            link = 'https://google.com',
            image = 'path/to/image.png',
            user = project_user,
            id = '2',
        )

        self.comment1 = Comment.objects.create(
            text = 'Text',
            project = self.project1,
            user = project_user,
        )

    def test_project_is_created_properly(self):
        self.assertEquals(self.project1.title, 'Title')
        self.assertEquals(self.project1.description, 'description')
        self.assertEquals(self.project1.link, 'https://google.com')
        self.assertEquals(self.project1.id, 2)

    def test_comment_is_created_properly(self):
        self.assertEquals(self.comment1.text, 'Text')
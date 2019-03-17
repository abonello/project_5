from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Issue, IssueComment
from django.contrib.auth.models import User


# class TestViews(TestCase):

    # def test_get_home_page(self):
        # # fake a request to the url we pass as an argument
        # page = self.client.get('/')
        # self.assertEqual(page.status_code, 200)
        # self.assertTemplateUsed(page, "index_home.html")

    # def test_get_issues_page(self):


    # def create_and_log_in_user(self):
    #     test_user = User.objects.create_user(
    #         username="test", email="test@example.com", password="testpword")
    #     self.client.login(username='test', password='testpword')

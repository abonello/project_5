from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestViews(TestCase):
        '''
                1 test: we are going to the correct location (correct url)
                2.test: status code
                3.test: correct template is used
        '''

        def test_get_home_page(self):
                # fake a request to the url we pass as an argument
                page = self.client.get('/')
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "index_home.html")

        def test_get_about_page(self):
                page = self.client.get('/about/')
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "about.html")

        def test_get_blog_page(self):
                page = self.client.get('/blog/')
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "blog.html")

        def test_get_uqc_app_page(self):
                page = self.client.get('/uqc_app/')
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "uqc-app.html")

        def test_get_contact_page(self):
                page = self.client.get('/contact/')
                self.assertEqual(page.status_code, 200)
                self.assertTemplateUsed(page, "contact.html")

from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item
from django.contrib.auth.models import User

class TestViews(TestCase):

    def create_and_log_in_user(self):
        test_user = User.objects.create_user(
            username="test", email="test@example.com", password="testpword")
        self.client.login(username='test', password='testpword')


    def test_get_test_page(self):
        # fake a request to the url we pass as an argument
        page = self.client.get('/test')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "test.html")


    def test_get_todo_list_page_logged_user(self):
        self.create_and_log_in_user()

        page = self.client.get('/todo')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")


    def test_get_todo_list_page_non_logged_user(self):
        page = self.client.get('/todo')
        self.assertEqual(page.status_code, 302)
    

    def test_get_add_page(self):
        self.create_and_log_in_user()

        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_form.html")


    def test_get_add_page_non_logged_user(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 302)


    def test_get_add_with_django_form_page(self):
        self.create_and_log_in_user()
        page = self.client.get('/add_django-form')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_django-form.html")

    def test_get_add_with_django_form_page_non_logged_user(self):
        page = self.client.get('/add_django-form')
        self.assertEqual(page.status_code, 302)


    def test_get_edit_item_page(self):
        self.create_and_log_in_user()
        item = Item(name="This is a test name")
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_django-form.html")

    def test_get_edit_item_page_non_logged_user(self):
        item = Item(name="This is a test name")
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 302)


    def test_get_edit_page_for_item_that_does_not_exist(self):
        self.create_and_log_in_user()
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 404)

    def test_get_edit_page_for_item_that_does_not_exist_non_logged_user(self):
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 302)


    def test_post_edit_an_item(self):
        self.create_and_log_in_user()
        item = Item(name = "Create an Name")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.name, "A different name")

    def test_post_edit_an_item_non_logged_user(self):
        item = Item(name="Create an Name")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        # item = get_object_or_404(Item, pk=id)
        self.assertEqual(response.status_code, 302)


    def test_toggle_status(self):
        self.create_and_log_in_user()
        item = Item(name="This is a test name")
        item.save()
        id = item.id
        self.assertFalse(item.done)
        page = self.client.post('/toggle/{0}'.format(id))
        self.assertEqual(page.status_code, 302)  # It redirects
        item = get_object_or_404(Item, pk=id)
        self.assertTrue(item.done)


    def test_toggle_status_non_logged_user(self):
        item = Item(name="This is a test name")
        item.save()
        id = item.id
        self.assertFalse(item.done)
        page = self.client.post('/toggle/{0}'.format(id))
        self.assertEqual(page.status_code, 302)
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(page.status_code, 302)


    def test_delete_item(self):
        self.create_and_log_in_user()
        item = Item(name="This is a test item")
        item.save()
        self.assertEqual(item.name, "This is a test item")
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 200) # Item exist
        page = self.client.get('/delete/{0}'.format(item.id))
        page = self.client.get('/edit/1') #Try to edit item which does not exist
        self.assertEqual(page.status_code, 404) # expect 404


    def test_delete_item_non_logged_user(self):
        item = Item(name="This is a test item")
        item.save()
        self.assertEqual(item.name, "This is a test item")
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 302)  # Item exist
        page = self.client.get('/delete/{0}'.format(item.id))
        # Try to edit item which does not exist when not logged in
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 302)


    def test_post_create_an_item(self):
        self.create_and_log_in_user()
        response = self.client.post("/add", {"name": "Create a Test Item"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_create_an_item_non_logged_user(self):
        response = self.client.post("/add", {"name": "Create a Test Item"})
        self.assertEqual(response.status_code, 302)


    def test_post_create_an_item_with_django_form(self):
        self.create_and_log_in_user()
        response = self.client.post("/add_django-form", {"name": "Create a Test Item"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_create_an_item_with_django_form_non_logged_user(self):
        response = self.client.post("/add_django-form", {"name": "Create a Test Item"})
        self.assertEqual(response.status_code, 302)


    # This does not exist anymore
    # def test_home_with_HttpResponse(self):
    #     page = self.client.get('/')
    #     self.assertEqual(page.status_code, 200)
    #     self.assertEqual(page.content, b"Hello World - This is a test")

    

    

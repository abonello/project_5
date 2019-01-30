from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

class TestViews(TestCase):
    def test_get_test_page(self):
        # fake a request to the url we pass as an argument
        page = self.client.get('/test')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "test.html")

    def test_get_todo_list_page(self):
        page = self.client.get('/todo')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
    
    def test_get_add_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_form.html")

    def test_get_add_with_django_form_page(self):
        page = self.client.get('/add_django-form')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_django-form.html")

    def test_get_edit_item_page(self):
        item = Item(name="This is a test name")
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_item_django-form.html")

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 404)

    def test_post_edit_an_item(self):
        item = Item(name = "Create an Name")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.name, "A different name")


    def test_toggle_status(self):
        item = Item(name="This is a test name")
        item.save()
        id = item.id
        self.assertFalse(item.done)
        page = self.client.post('/toggle/{0}'.format(id))
        self.assertEqual(page.status_code, 302) # It redirects
        item = get_object_or_404(Item, pk=id)
        self.assertTrue(item.done)


    def test_delete_item(self):
        item = Item(name="This is a test item")
        item.save()
        self.assertEqual(item.name, "This is a test item")
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 200) # Item exist
        page = self.client.get('/delete/{0}'.format(item.id))
        page = self.client.get('/edit/1') #Try to edit item which does not exist
        self.assertEqual(page.status_code, 404) # expect 404


    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test Item"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)


    def test_post_create_an_item_with_django_form(self):
        response = self.client.post("/add_django-form", {"name": "Create a Test Item"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)


    def test_home_with_HttpResponse(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.content, b"Hello World - This is a test")

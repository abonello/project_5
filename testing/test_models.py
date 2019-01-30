from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        item = Item(name="Test name")
        item.save()
        self.assertEqual(item.name, "Test name")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_name_and_status(self):
        item = Item(name="Test name", done=True)
        item.save()
        self.assertEqual(item.name, "Test name")
        self.assertTrue(item.done)

    def test_item_as_a_string(self):
        item = Item(name="Create a Test Item")
        item.save()
        self.assertEqual(str(item), "Create a Test Item")


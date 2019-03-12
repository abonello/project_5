from django.test import TestCase
from .models import Product

# Create your tests here.

class ProductTests(TestCase):
    """ Define tests that will be run against
    the Product model. """

    def est_str(self):
        test_product = Product(name="test name")
        self.assertEqual(str(test_product), "test name")
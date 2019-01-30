from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    def test_is_this_thing_on(self):
        # self.assertEqual(1, 0) # Step 1: This should fail - Red
        self.assertEqual(1, 1)  # Step 2: This should pass - Green

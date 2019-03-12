from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):
    '''
        Generic test to check that everything is working as it should.
    '''
    def test_is_this_thing_on(self):
        # Step 1: This should fail - Red
        # self.assertEqual(1, 0)

        # Step 2: This should pass - Green
        self.assertEqual(1, 1)

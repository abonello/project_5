from django.apps import apps
from django.test import TestCase
from .apps import TestingConfig

class TestTestingConfig(TestCase):
    def test_app(self):
        self.assertEqual(TestingConfig.name, "testing")
        self.assertEqual(apps.get_app_config("testing").name, "testing")

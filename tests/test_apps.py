from django.apps import apps as django_appsa
from django.test import TestCase
from url_shorter import apps


class TestUrlShorterConfig(TestCase):
    def test_apps(self):
        self.assertEqual(
            apps.UrlShorterConfig.name,
            'url_shorter'
        )
        self.assertEqual(
            apps.UrlShorterConfig.verbose_name,
            'url_shorters'
        )
        self.assertEqual(
            django_appsa.get_app_config('url_shorter').name,
            'url_shorter'
        )

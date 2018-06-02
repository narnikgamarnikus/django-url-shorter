from django.test import TestCase
from url_shorter import services
from url_shorter import models

from . import factories


class TestCreateNewURL(TestCase):

    @classmethod
    def setUpTestData(cls):
        #cls.new_url = factories.URLFactory()
        cls.user = factories.UserFactory()
        cls.new_url = services.create_new_url(
            'https://google.com/',
            cls.user
        )
        cls.new_short_url = services.generate_short_url()

    def setUp(self):
        pass

    def test_new_short_url_created(self):
        self.assertNotEqual(self.new_short_url, None)

    def test_new_short_url_is_string(self):
        self.assertTrue(type(self.new_short_url))

    def test_jew_short_url_length(self):
        self.assertEqual(
            len(self.new_short_url),
            6
        )

    def test_new_url_created(self):
        self.assertNotEqual(
            self.new_url.short_url,
            None
        )

    def test_new_url_is_URL_instance(self):
        self.assertTrue(
            isinstance(self.new_url, models.URL)
        )

    def test_new_url_equal_long_url(self):
        self.assertEqual(
            self.new_url.long_url,
            'https://google.com/'
        )

    def test_new_url_short_url_is_string(self):
        self.assertEqual(
            type(self.new_url.short_url),
            type('')
        )

    def test_create_many_new_urls_with_one_long_url(self):
        for _ in range(10):
            url = services.create_new_url('https://google.com/', self.user)

            self.assertEqual(
                self.new_url,
                url
            )

    def test_create_new_url_without_long_url(self):
        url = services.create_new_url('', self.user)
        self.assertEqual(
            url,
            ''
        )

    def test_create_new_url_withput_long_url_equal_instance(self):
        url = services.create_new_url('', self.user)
        self.assertFalse(isinstance(url, models.URL))

    def tearDown(self):
        pass

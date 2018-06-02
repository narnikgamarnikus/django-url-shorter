from django.urls import reverse, resolve

from test_plus.test import TestCase
from . import factories


class TestURLurls(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.url = factories.URLFactory()

    def setUp(self):
        pass

    def test_url_create_reverse(self):
        """shorter:url_create reverse to /shorter/create/ """
        self.assertEqual(
            reverse('url_shorter:create'),
            '/shorter/create/'
        )

    def test_url_create_resolve(self):
        """/shorter/create/ should resolve to 'url_shorter:url_create'."""
        self.assertEqual(
            resolve('/shorter/create/').view_name,
            'url_shorter:create'
        )

    def test_url_redirect_reverse(self):
        """shorter:url_redirect reverse to /shorter/zxcwqe/ """
        self.assertEqual(
            reverse('url_shorter:redirect', kwargs={'short_url': self.url.pk}),
            '/shorter/{}/'.format(self.url.pk)
        )

    def test_url_redirect_resolve(self):
        """/shorter/zxcwqe/ should resolve to 'url_shorter:url_redirect'."""
        self.assertEqual(
            resolve('/shorter/zxcwqe/').view_name,
            'url_shorter:redirect'
        )

    def test_url_detail_reverse(self):
        """shorter:url_detail should reverse to /shorter/url_detail/asdzxc/."""
        self.assertEqual(
            reverse('url_shorter:detail', kwargs={'short_url': self.url.pk}),
            '/shorter/detail/{}/'.format(self.url.pk)
        )

    def test_url_detail_resolve(self):
        """/shorter/detail/asdzxc/ should resolve to shorter:url_detail."""
        self.assertEqual(
            resolve('/shorter/detail/asdzxc/').view_name,
            'url_shorter:detail'
        )

from django.test import TestCase
from django.test import RequestFactory
from django.template import Context, Template
from .factories import UserFactory
from url_shorter.models import URL


class TestCreateNewUrlForUser(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_with_authenticated_user(self):
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user
        out = Template(
            "{% load url_shorter %}"
            "{% create_new_url_for_user 'https://google.com/' request.user %}"
        ).render(Context({
            'request': request,
            })
        )
        url = URL.objects.first()
        self.assertEqual(
            out,
            url.short_url
        )

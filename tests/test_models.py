#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-url-shorter
------------

Tests for `django-url-shorter` models module.
"""

from django.test import TestCase

# from url_shorter.models import

from . import factories
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from url_shorter.models import URL
from django.contrib.auth import get_user_model


class TestURL(TestCase):

    def setUp(self):
        self.url = factories.URLFactory()

    def test_url_data(self):
        self.assertEqual(
            len(self.url.short_url),
            6
        )
        self.assertEqual(
            self.url.long_url,
            'https://google.com/'
        )
        self.assertTrue(
            self.url.created < timezone.now()
        )
        self.assertEqual(
            self.url.count,
            0
        )

    def test__str__(self):
        self.assertEqual(
            self.url.__str__(),
            'https://google.com/'
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.url.get_absolute_url(),
            '/shorter/detail/{}/'.format(self.url.short_url)
        )

    def test_not_created_without_data(self):
        new_url = URL()
        self.assertRaises(
            ValidationError,
            new_url.full_clean
        )

    def test_not_created_with_exists_long_url(self):
        new_url = URL(short_url='asdsad',
                      long_url='https://google.com/', count=0)
        self.assertRaisesRegex(
            ValidationError,
            'Url with this Long url already exists.',
            new_url.full_clean
        )

    def test_add_count(self):
        self.url.count += 1
        self.url.save()
        self.assertEqual(
            self.url.count,
            1
        )

    def tearDown(self):
        pass

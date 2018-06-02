# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from url_shorter.urls import urlpatterns as url_shorter_urls

urlpatterns = [
    url(r'^shorter/', include((url_shorter_urls, 'url_shorter'), namespace='url_shorter'))
]
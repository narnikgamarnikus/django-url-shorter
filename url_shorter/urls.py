# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.generic import TemplateView

from . import views

app_name = 'url_shorter'

urlpatterns = [
    re_path(
        r"^$",
        view=TemplateView.as_view(template_name="url_shorter/base.html"),
        name="base"
    ),
    re_path(
        r"^list/$",
        view=views.URLListView.as_view(),
        name="list"
    ),
    re_path(
        r"^create/$",
        view=views.URLCreateView.as_view(),
        name="create"
    ),
    re_path(
        r"^detail/(?P<short_url>[\w.@+-]+)/$",
        view=views.URLDetailView.as_view(),
        name="detail"
    ),
    re_path(
        r"^(?P<short_url>[\w.@+-]+)/$",
        view=views.URLRedirectView.as_view(),
        name="redirect"
    ),
    # url(r'user_url_redirect/(?P<short_url>[\w.@+-]+)/',
    #    views.UserURLRedirectView.as_view(), name="user_url_redirect"),

    #url(r'url_create/', views.URLCreateView.as_view(), name="url_create"),
    # url(r'url_detail/(?P<short_url>[\w.@+-]+)/',
    #    views.URLDetailView.as_view(), name='url_detail'),
]

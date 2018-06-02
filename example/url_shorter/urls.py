# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'url_shorter'

urlpatterns = [
	url(r'user_url_list/', views.UserURLListView.as_view(), name="user_url_list"),
    url(r'user_url_create/', views.UserURLCreateView.as_view(), name="user_url_create"),
    url(r'user_url_detail/(?P<short_url>[\w.@+-]+)/', views.UserURLDetailView.as_view(), name='user_url_detail'),
    url(r'user_url_redirect/(?P<short_url>[\w.@+-]+)/', views.UserURLRedirectView.as_view(), name="user_url_redirect"),

    url(r'url_create/', views.URLCreateView.as_view(), name="url_create"),
    url(r'url_detail/(?P<short_url>[\w.@+-]+)/', views.URLDetailView.as_view(), name='url_detail'),
    url(r'url_redirect/(?P<short_url>[\w.@+-]+)/', views.URLRedirectView.as_view(), name="url_redirect"),
    
    url(r'', TemplateView.as_view(template_name="url_shorter/base.html")),
]

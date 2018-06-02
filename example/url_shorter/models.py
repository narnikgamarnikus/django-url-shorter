# -*- coding: utf-8 -*-

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _

from django.urls import reverse

from .utils import string_generator

from django.contrib.auth import get_user_model

from django.http import HttpResponseRedirect


class URL(models.Model):

	short_url = models.SlugField(max_length=6, primary_key=True, unique=True)
	long_url = models.URLField(max_length=100, unique=True)
	created = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.long_url

	def get_absolute_url(self):
		return reverse('url_shorter:url_detail', kwargs={'short_url': self.short_url})

	def save(self, *args, **kwargs):
		if not self.short_url:
			self.short_url = string_generator()
		return super(URL, self).save(*args, **kwargs)


class UserURL(URL):

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('url_shorter:user_url_detail', kwargs={'short_url': self.short_url})
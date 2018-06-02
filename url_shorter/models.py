# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel
from annoying.fields import JSONField

from geolite2 import geolite2

from .utils import string_generator


class URL(TimeStampedModel):

    """
    Description: Model Description
    """

    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    short_url = models.SlugField(max_length=6, primary_key=True, unique=True)
    long_url = models.URLField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url

    def get_absolute_url(self):
        return reverse(
            'url_shorter:detail',
            kwargs={'short_url': self.short_url}
        )

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = string_generator()
        return super(URL, self).save(*args, **kwargs)


class Hit(TimeStampedModel):

    """
    Description: Model Description
    """

    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    ip = models.CharField(default=None, null=True, max_length=50)
    data = JSONField(default=None, null=True)

    class Meta:
        pass

    def save(self, *args, **kwargs):
        if self.ip:
            reader = geolite2.reader()
            data = reader.get(self.ip)
            self.data = data
            geolite2.close()
        return super(Hit, self).save(*args, **kwargs)

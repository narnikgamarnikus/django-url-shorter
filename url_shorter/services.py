from .models import URL
from .utils import string_generator


def generate_short_url():
    while True:
        short_url = string_generator()
        try:
            URL.objects.get(pk=short_url)
        except:
            return short_url


def create_new_url(long_url, user):
    if long_url:
        new_url, created = URL.objects.get_or_create(
            long_url=long_url,
        )
        if created:
            new_url.user = user
            new_url.save()
        return new_url
    return long_url

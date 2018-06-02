from .models import URL
from .utils import string_generator


def generate_short_url():
    while True:
        short_url = string_generator()
        try:
            url = Url.objects.get(pk=short_url)
        except:
            return short_url


def create_new_url(long_url):
    if long_url:
        new_url, created = URL.objects.get_or_create(long_url=long_url)
        return new_url
    return long_url

from django import template
from django.contrib.auth import get_user_model


from ..services import create_new_url
from ..utils import uri_validator

register = template.Library()
User = get_user_model()


@register.simple_tag()
def create_new_url_for_user(long_url, user):

    assert uri_validator(long_url)
    assert isinstance(user, User), ('user must be instance of User model')
    new_url = create_new_url(long_url, user)
    return new_url.short_url

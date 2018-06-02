import string
import random

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


validate = URLValidator()


def string_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def uri_validator(uri):
    try:
        validate(uri)
        return True
    except ValidationError:
        return False

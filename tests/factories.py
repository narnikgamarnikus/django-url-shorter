import factory
from url_shorter import models
import factory.fuzzy as fuzzy
import datetime


class UserFactory(factory.django.DjangoModelFactory):

    username = factory.Sequence(lambda n: 'user-{}'.format(n))
    email = factory.Sequence(lambda n: 'user-{}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username', )


class URLFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)

    long_url = 'https://google.com/'
    created = fuzzy.FuzzyNaiveDateTime(datetime.datetime.now())
    count = fuzzy.FuzzyInteger(0)

    class Meta:
        model = models.URL

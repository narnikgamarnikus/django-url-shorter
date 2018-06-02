from test_plus.test import TestCase
from url_shorter import views, models, urls
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from .factories import UserFactory

User = get_user_model()


class TestURLListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('12345')
        cls.user.save()
        cls.view = views.ListView

    def setUp(self):
        self.logged_in = self.client.login(
            username='testuser', password='12345'
        )
        self.response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'})
        self.response = self.client.get('/shorter/list/')

    def test_status_code(self):
        self.assertEqual(
            self.response.status_code,
            200
        )

    def test_queryset(self):
        self.assertQuerysetEqual(
            self.response.context['url_list'],
            models.URL.objects.filter(user=self.user),
            transform=lambda x: x
        )


class TestURLCreateView(TestCase):

    def setUp(self):
        self.view = views.URLCreateView
        self.user = UserFactory(password='123456789QWERTYUIOP')

    def test_post_with_data(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'}
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertTrue(
            isinstance(models.URL.objects.first(), models.URL)
        )
        self.assertEqual(
            response.url,
            models.URL.objects.first().get_absolute_url()
        )

    def test_post_without_data(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        response = self.client.post('/shorter/create/', {})

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertFormError(
            response,
            'form',
            'long_url',
            'This field is required.'
        )

    def test_post_with_integer_in_data(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        response = self.client.post('/shorter/create/', {'long_url': 123})

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertFormError(
            response,
            'form',
            'long_url',
            'Enter a valid URL.'
        )

    def test_post_with_wrong_url(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        response = self.client.post(
            '/shorter/create/', {'long_url': 'http://asd'})

        self.assertEquals(
            response.status_code,
            200
        )

        self.assertFormError(
            response,
            'form',
            'long_url',
            'Enter a valid URL.'
        )

    def test_post_with_exist_long_url(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'})
        response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'})

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertFormError(
            response,
            'form',
            'long_url',
            'Url with this Long url already exists.'
        )

    def tearDown(self):
        pass


class TestURLDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view = views.URLDetailView
        cls.user = UserFactory(password='123456789QWERTYUIOP')

    def setUp(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        self.response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'}
        )
        self.template_response = self.client.get(self.response.url)

    def test_get_200(self):
        self.assertEqual(
            self.template_response.status_code,
            200
        )

    def test_context_object_is_URL_instance(self):
        self.assertTrue(
            isinstance(self.template_response.context['object'], models.URL)
        )

    def test_context_object_long_url(self):
        self.assertEqual(
            self.template_response.context['object'].long_url,
            'https://google.com/'
        )


class TestURLRedirectView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view = views.URLRedirectView
        cls.user = UserFactory(password='123456789QWERTYUIOP')

    def setUp(self):
        self.client.login(
            username=self.user.username,
            password='123456789QWERTYUIOP'
        )
        self.response = self.client.post(
            '/shorter/create/', {'long_url': 'https://google.com/'})
        self.template_response = self.client.get(self.response.url)
        self.obj = self.template_response.context['object']
        self.response = self.client.get(
            '/shorter/{}/'.format(self.obj.short_url))

    def test_get_success_url(self):
        self.assertEqual(
            self.response.status_code,
            302
        )

        self.assertEqual(
            self.response['Location'],
            self.obj.long_url
        )

        self.assertEqual(
            self.response.url,
            self.obj.long_url
        )

        self.assertEqual(
            self.response['Location'],
            'https://google.com/'
        )
        self.assertRedirects(
            self.response,
            'https://google.com/',
            fetch_redirect_response=False
        )

    def test_object(self):
        self.assertEqual(
            self.obj,
            models.URL.objects.first()
        )

    def test_with_remote_addr(self):
        self.client.get(
            '/shorter/{}/'.format(self.obj.short_url),
            REMOTE_ADDR='5.152.37.206'
        )
        obj = models.Hit.objects.last()
        self.assertEqual(obj.ip, '5.152.37.206')
        self.assertEqual(obj.data, {
            'location': {
                'time_zone': 'Asia/Tbilisi',
                'accuracy_radius': 50,
                'longitude': 43.5,
                'latitude': 42.0
            },
            'country': {
                'iso_code': 'GE',
                'geoname_id': 614540,
                'names': {
                    'de': 'Georgien',
                    'zh-CN': '格鲁吉亚',
                    'es': 'Georgia',
                    'fr': 'Géorgie',
                    'ja': 'グルジア共和国',
                    'ru': 'Грузия',
                    'en': 'Georgia',
                    'pt-BR': 'Geórgia'
                }
            },
            'registered_country': {
                'iso_code': 'GE',
                'geoname_id': 614540,
                'names': {
                    'de': 'Georgien',
                    'zh-CN': '格鲁吉亚',
                    'es': 'Georgia',
                    'fr': 'Géorgie',
                    'ja': 'グルジア共和国',
                    'ru': 'Грузия',
                    'en': 'Georgia',
                    'pt-BR': 'Geórgia'
                }
            },
            'continent': {
                'code': 'AS',
                'geoname_id': 6255147,
                'names': {
                    'de': 'Asien',
                    'zh-CN': '亚洲',
                    'es': 'Asia',
                    'fr': 'Asie',
                    'ja': 'アジア',
                    'ru': 'Азия',
                    'en': 'Asia',
                    'pt-BR': 'Ásia'
                }
            }
        })

    def test_without_remote_addr(self):
        self.client.get(
            '/shorter/{}/'.format(self.obj.short_url),
            REMOTE_ADDR=''
        )
        obj = models.Hit.objects.last()
        self.assertIsNone(obj.ip)
        self.assertIsNone(obj.data)

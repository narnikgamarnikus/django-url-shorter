from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from url_shorter import views
from django.urls import reverse


'''
class TestURLCreateForm(LiveServerTestCase):
    port = 8082

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_submit_form(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/shorter/create/'))
        long_url_input = self.selenium.find_element_by_name('long_url')
        long_url_input.send_keys('https://google.com/')
        self.selenium.find_element_by_xpath('//button[@value="Submit"]').click()
'''

from django.test import TestCase

from url_shorter import utils


class TestStringGenerator(TestCase):

    def setUp(self):
        self.string = utils.string_generator()

    def test_string_len_is_six(self):
        self.assertEqual(
            len(self.string),
            6
        )

    def test_generate_unique_string(self):
        self.assertNotEqual(
            self.string,
            utils.string_generator()
        )

    def test_another_count_in_string_generator(self):
        self.assertEqual(
            len(utils.string_generator(25)),
            25
        )

    def test_another_chars_in_string_generator(self):
        self.assertTrue(
            type(utils.string_generator(chars='1234567890qwertyuiop[]asdfghjkl;')),
            str()
        )

    def test_another_chars_and_size_in_string_generator(self):
        new_string = utils.string_generator(
            size=25, chars='1234567890qwertyuiop[]asdfghjkl;')
        self.assertTrue(
            type(new_string),
            str()
        )
        self.assertTrue(
            len(new_string),
            25
        )

from unittest import TestCase
from dungeonsanddragons import generate_name


class TestGenerateName(TestCase):

    def test_length(self):
        self.assertEqual(6, len(generate_name(3)))

    def test_type(self):
        self.assertIsInstance(generate_name(3), str)

    def test_first_capital(self):  # first letter should be a capital consonant
        self.assertIn((generate_name(4))[0], 'BCDFGHJKLMNPQRSTVWXYZ')

    def test_vowels(self):
        for i in range(1, len(generate_name(4)), 2):  # every odd letter should be a vowel
            self.assertIn((generate_name(4))[i], 'aeiouy')

    def test_consonants(self):
        for i in range(2, len(generate_name(4)), 2):  # every even letter after the first should be a consonant
            self.assertIn((generate_name(4))[i], 'bcdfghjklmnpqrstvwxyz')
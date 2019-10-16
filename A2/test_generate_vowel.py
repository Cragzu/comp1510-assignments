from unittest import TestCase
from dungeonsanddragons import generate_vowel


class TestGenerateVowel(TestCase):

    def test_generate_vowel(self):
        self.assertIn(generate_vowel(), 'aeiouy')

    def test_length(self):
        self.assertEqual(len(generate_vowel()), 1)

    def test_type(self):
        self.assertIsInstance(generate_vowel(), str)

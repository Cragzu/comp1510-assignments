from unittest import TestCase
from dungeonsanddragons import generate_consonant


class TestGenerateConsonant(TestCase):

    def test_generate_consonant(self):
        self.assertIn(generate_consonant(), 'bcdfghjklmnpqrstvwxyz')

    def test_length(self):
        self.assertEqual(len(generate_consonant()), 1)

    def test_type(self):
        self.assertIsInstance(generate_consonant(), str)

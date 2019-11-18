from unittest import TestCase
from question_1 import eratosthenes


class TestEratosthenes(TestCase):

    def test_eratosthenes(self):
        self.assertEqual(eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_empty_return(self):
        self.assertEqual(eratosthenes(1), [])

    def test_invalid_type(self):
        self.assertRaises(Exception, eratosthenes, 'a')

from unittest import TestCase
from question_1 import is_prime


class TestIsPrime(TestCase):

    def test_prime_number(self):
        self.assertEqual(is_prime(7), True)

    def test_not_prime_number(self):
        self.assertEqual(is_prime(8), False)

    def test_below_1(self):
        self.assertEqual(is_prime(1), False)

    def test_negative(self):
        self.assertEqual(is_prime(-1), False)

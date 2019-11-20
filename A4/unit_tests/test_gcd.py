from unittest import TestCase
from question_2 import gcd


class TestGcd(TestCase):

    def test_two_positives(self):
        self.assertEqual(gcd(25, 15), 5)

    def test_positive_negative(self):
        self.assertEqual(gcd(-25, 15), 5)

    def test_two_negatives(self):
        self.assertEqual(gcd(-25, -15), -5)

    # def test_invalid_arguments(self):  # todo: enable when raising exception is implemented
    #     self.assertRaises(Exception, gcd, 'a', 0)  # todo: do the special way as pinned in discord

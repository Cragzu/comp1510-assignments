from unittest import TestCase
from question_2 import gcd
import io
import unittest.mock


class TestGcd(TestCase):

    def test_two_positives(self):
        self.assertEqual(gcd(25, 15), 5)

    def test_positive_negative(self):
        self.assertEqual(gcd(-25, 15), 5)

    def test_two_negatives(self):
        self.assertEqual(gcd(-25, -15), -5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_arguments(self, mock_stdout):
        expected_output = 'The given argument was not int!\n'
        gcd('a', 'b')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

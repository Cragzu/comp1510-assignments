from unittest import TestCase
from question_1 import eratosthenes
import io
import unittest.mock


class TestEratosthenes(TestCase):

    def test_eratosthenes(self):
        self.assertEqual(eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_empty_return(self):
        self.assertEqual(eratosthenes(1), [])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_arguments(self, mock_stdout):
        expected_output = 'The given upperbound was not an int!\n'
        eratosthenes('a')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

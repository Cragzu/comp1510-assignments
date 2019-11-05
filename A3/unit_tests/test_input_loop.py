from unittest import TestCase
from character import input_loop
import io
import unittest.mock


class TestInputLoop(TestCase):

    @unittest.mock.patch('builtins.input', return_value='n')
    def test_return_value(self, mock_input):  # check that returned string is the user choice
        self.assertEqual(input_loop('Test', ['N']), 'N')

    @unittest.mock.patch('builtins.input', side_effect=['a', 'b', 'n'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):  # check for error messages on invalid input
        expected_output = 'Sorry, that wasn\'t a valid input. Please try again.\n' \
                          'Sorry, that wasn\'t a valid input. Please try again.\n'
        input_loop('Test', ['N'])
        self.assertEqual(mock_stdout.getvalue(), expected_output)
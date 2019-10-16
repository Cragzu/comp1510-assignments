from unittest import TestCase
import unittest.mock
import io
from dungeonsanddragons import selection_helper


class TestSelectionHelper(TestCase):

    @unittest.mock.patch('builtins.input', return_value='1')
    def test_returned_item(self, mock_input):  # check that returned string is the user choice
        test_dict = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(selection_helper('letter', test_dict), 'a')

    @unittest.mock.patch('builtins.input', return_value='1')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output(self, mock_stdout, mock_input):  # check for correctly printed output
        test_dict = {1: 'a', 2: 'b', 3: 'c'}
        expected_output = 'Which letter would you like your character to be? There are 3 available:\n1 - a' \
                          '\n2 - b\n3 - c\nYour letter is: a\n'
        selection_helper('letter', test_dict), 'a'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('builtins.input', side_effect=['a', '12', '1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):  # check for error messages on invalid input
        test_dict = {1: 'a', 2: 'b', 3: 'c'}
        expected_output = 'Which letter would you like your character to be? There are 3 available:\n1 - a' \
                          '\n2 - b\n3 - c\nThat wasn\'t an acceptable input. Please enter a number corresponding ' \
                          'to a letter.\nThat wasn\'t an acceptable input. Please enter a number corresponding ' \
                          'to a letter.\nYour letter is: a\n'
        selection_helper('letter', test_dict), 'a'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

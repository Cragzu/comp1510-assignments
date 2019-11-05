from unittest import TestCase
from monster import backstab
import unittest.mock
import io


class TestBackstab(TestCase):

    @unittest.mock.patch('random.randint', side_effect=[1, 4])
    def test_backstab_success(self, mock_randint):
        self.assertEqual(backstab(), 4)

    @unittest.mock.patch('random.randint', side_effect=[1, 4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output_backstab_success(self, mock_stdout, mock_randint):
        expected_output = 'The monster stabbed you in the back!\nYou took 4 damage before escaping.\n'
        backstab()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('random.randint', return_value=3)
    def test_backstab_fail(self, mock_randint):
        self.assertEqual(backstab(), 0)

    @unittest.mock.patch('random.randint', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output_backstab_fail(self, mock_stdout, mock_randint):
        expected_output = 'You got away safely!\n'
        backstab()
        self.assertEqual(mock_stdout.getvalue(), expected_output)



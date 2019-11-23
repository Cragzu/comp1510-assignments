from unittest import TestCase
from question_4 import selection_sort
import io
import unittest.mock


class TestSelectionSort(TestCase):

    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 5, 1, 9, -4]), [-4, 3, 1, 5, 9])

    def test_empty_list(self):
        self.assertRaises(Exception, selection_sort, [])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_arguments(self, mock_stdout):
        expected_output = 'The given argument is not a sortable list!\n'
        selection_sort('a')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

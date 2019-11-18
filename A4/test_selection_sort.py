from unittest import TestCase
from question_4 import selection_sort


class TestSelectionSort(TestCase):  # todo: raising error for list of unsortable items

    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 5, 1, 9, -4]), [-4, 3, 1, 5, 9])

    def test_empty_list(self):
        self.assertRaises(Exception, selection_sort, [])

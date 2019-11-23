from unittest import TestCase
from question_8 import find_highest_bars


class TestFindHighestBars(TestCase):

    def test_no_padding(self):
        self.assertEqual(find_highest_bars(1, 9), ['8', 7])

    def test_with_padding(self):
        self.assertEqual(find_highest_bars(1, 9, '0'), ['08', 13])

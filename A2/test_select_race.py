from unittest import TestCase
import unittest.mock
from dungeonsanddragons import select_race


class TestSelectRace(TestCase):

    @unittest.mock.patch('builtins.input', return_value='1')
    def test_select_race(self, mock_input):
        self.assertEqual('dragonborn', select_race())

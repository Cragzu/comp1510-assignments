from unittest import TestCase
import unittest.mock
from dungeonsanddragons import select_class


class TestSelectClass(TestCase):

    @unittest.mock.patch('builtins.input', return_value='1')
    def test_select_class(self, mock_input):
        self.assertEqual('barbarian', select_class())

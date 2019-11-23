from unittest import TestCase
from question_7 import update_dict
import io
import unittest.mock


class TestUpdateDict(TestCase):

    @unittest.mock.patch('builtins.input', return_value='1')
    def test_update_dict(self, mock_input):
        _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                     "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
        calories_after = {'a': 1, "lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225,
                          "milk": 122, "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

        self.assertEqual(update_dict('a', _calories), calories_after)

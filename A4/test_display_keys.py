from unittest import TestCase
from question_7 import display_keys
import io
import unittest.mock


class TestDisplayKeys(TestCase):

    def test_display_keys(self):
        self.fail()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_keys(self, mock_stdout):
        _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                     "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
        expected_output = "Food Items: ['apple', 'beef', 'bread', 'butter', 'carrot', 'cheese', " \
                          "'chicken', 'lettuce', 'milk', 'pasta', 'rice', 'yogurt']\n"
        display_keys(_calories)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_dict(self, mock_stdout):
        _calories = {}
        expected_output = "Food Items: []\n"
        display_keys(_calories)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

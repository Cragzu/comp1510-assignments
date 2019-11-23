from unittest import TestCase
from question_7 import calculate_calories
import io
import unittest.mock


class TestCalculateCalories(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_calories(self, mock_stdout):
        _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                     "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
        expected_output = 'Total Calories: 1505 Average Calories: 125.4\n\n'
        calculate_calories(_calories)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_no_values(self, mock_stdout):
        _calories = {}
        expected_output = 'There were no items in the dictionary!\n'
        calculate_calories(_calories)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

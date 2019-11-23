from unittest import TestCase
from question_7 import update_calories
import unittest.mock


class TestUpdateCalories(TestCase):

    @unittest.mock.patch('question_7.update_dict')
    @unittest.mock.patch('question_7.display_keys')
    @unittest.mock.patch('question_7.calculate_calories')
    @unittest.mock.patch('builtins.input', side_effect=['pie', 'q'])
    def test_update_calories(self, mock_input, mock_calculate_calories, mock_display_keys, mock_update_dict):
        update_calories()
        for i in [mock_calculate_calories, mock_display_keys, mock_update_dict]:  # check that functions were called
            self.assertTrue(i.called)

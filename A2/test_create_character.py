from unittest import TestCase
import unittest.mock
from dungeonsanddragons import create_character
# todo: currently throws error - fix that

class TestCreateCharacter(TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['2', '2'])
    @unittest.mock.patch('dungeonsanddragons.roll_die', side_effect=[7, 14, 9, 6, 11, 13, 9])
    @unittest.mock.patch('dungeonsanddragons.create_name', return_value='Vedyma')
    def test_create_character(self, mock_create_name, mock_roll_die, mock_input):
        expected_output = {'Name': 'Vedyma', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                           'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                           'XP': 0, 'Inventory': []}
        self.assertEqual(create_character(3), expected_output)

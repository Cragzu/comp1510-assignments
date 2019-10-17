from unittest import TestCase
import unittest.mock
from dungeonsanddragons import create_character


class TestCreateCharacter(TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['2', '2'])
    def test_is_dictionary(self, mock_input):  # test if returned  object is a dict
        self.assertIsInstance(create_character(3), dict)

    @unittest.mock.patch('builtins.input', side_effect=['2', '2', '2', '2', '2', '2'])
    def test_string_pairs(self, mock_input):  # check that name, race, and class are strings
        for i in ['Name', 'Race', 'Class']:
            self.assertIsInstance((create_character(3))[i], str)

    @unittest.mock.patch('builtins.input', side_effect=['2', '2', '2', '2', '2', '2', '2',
                                                        '2', '2', '2', '2', '2', '2', '2'])
    def test_int_pairs(self, mock_input):  # check that XP and stats are ints
        for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'XP']:
            self.assertIsInstance((create_character(3))[i], int)

    @unittest.mock.patch('builtins.input', side_effect=['2', '2', '2', '2'])
    def test_list_pairs(self, mock_input):  # check that HP and inventory are lists
        for i in ['HP', 'Inventory']:
            self.assertIsInstance((create_character(3))[i], list)

from unittest import TestCase
import io
import unittest.mock
from dungeonsanddragons import print_character


class TestPrintCharacter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        expected_output = 'Your character is named Vedyma \nYour race is dwarf \nYour class is bard \n' \
                          'Your starting HP is 7\nYour Strength is 14\nYour Dexterity is 9\nYour Constitution is 6\n' \
                          'Your Intelligence is 11\nYour Wisdom is 13\nYour Charisma is 9\nYour current XP is 0' \
                          '\nYou don\'t have any items right now.\n'

        print_character({'Name': 'Vedyma', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                         'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                         'XP': 0, 'Inventory': []})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

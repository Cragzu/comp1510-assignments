from unittest import TestCase
import io
import unittest.mock
from dungeonsanddragons import combat_round


class TestCombatRound(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('dungeonsanddragons.attack', return_value=7)
    @unittest.mock.patch('dungeonsanddragons.roll_die', side_effect=[9, 1])
    def test_defender_defeated(self, mock_roll_die, mock_attack, mock_stdout):
        attacker = {'Name': 'Attacker', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        defender = {'Name': 'Defender', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 1, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        expected_output = 'Rolling to determine attack priority...\nAttacker rolled: 9\n' \
                          'Defender rolled: 1\nAttacker attacks first!\nDefender was defeated!\n'
        combat_round(attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('dungeonsanddragons.attack', side_effect=[4, 4])
    @unittest.mock.patch('dungeonsanddragons.roll_die', side_effect=[9, 1])
    def test_counterattack(self, mock_roll_die, mock_attack, mock_stdout):
        attacker = {'Name': 'Attacker', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        defender = {'Name': 'Defender', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 1, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        expected_output = 'Rolling to determine attack priority...\nAttacker rolled: 9\n' \
                          'Defender rolled: 1\nAttacker attacks first!\n'
        combat_round(attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('dungeonsanddragons.attack', side_effect=[4, 4])
    @unittest.mock.patch('dungeonsanddragons.roll_die', side_effect=[5, 5, 9, 1])
    def test_tie_roll(self, mock_roll_die, mock_attack, mock_stdout):
        attacker = {'Name': 'Attacker', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        defender = {'Name': 'Defender', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                    'Dexterity': 1, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                    'XP': 0, 'Inventory': []}
        expected_output = 'Rolling to determine attack priority...\nAttacker rolled: 5\n' \
                          'Defender rolled: 5\nA tie! Rolling again...\nAttacker rolled: 9\n' \
                          'Defender rolled: 1\nAttacker attacks first!\n'
        combat_round(attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

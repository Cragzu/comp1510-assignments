from unittest import TestCase
import unittest.mock
from dungeonsanddragons import attack


class TestAttack(TestCase):

    @unittest.mock.patch('dungeonsanddragons.roll_die', return_value=10)
    def test_attack_hit(self, mock_roll_die):
        attacker = {'Name': 'Attacker', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                         'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                         'XP': 0, 'Inventory': []}
        defender = {'Name': 'Defender', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                         'Dexterity': 1, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                         'XP': 0, 'Inventory': []}
        self.assertGreater(attack(attacker, defender), 0)

    @unittest.mock.patch('dungeonsanddragons.roll_die', return_value=1)
    def test_attack_miss(self, mock_roll_die):
        attacker = {'Name': 'Attacker', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                         'Dexterity': 9, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                         'XP': 0, 'Inventory': []}
        defender = {'Name': 'Defender', 'Race': 'dwarf', 'Class': 'bard', 'HP': [7, 7], 'Strength': 14,
                         'Dexterity': 1, 'Constitution': 6, 'Intelligence': 11, 'Wisdom': 13, 'Charisma': 9,
                         'XP': 0, 'Inventory': []}
        self.assertEqual(attack(attacker, defender), 0)


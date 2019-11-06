from unittest import TestCase
from monster import attack
import unittest.mock
import io


class TestAttack(TestCase):

    @unittest.mock.patch('random.randint', return_value=1)
    def test_miss(self, mock_randint):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 5, 'max_HP': 5}

        self.assertEqual(attack(attacker=creature_one, defender=creature_two), 0)

    @unittest.mock.patch('random.randint', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_miss_printed_output(self, mock_stdout, mock_randint):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        expected_output = 'The attack from Creature_One missed!\n'

        attack(attacker=creature_one, defender=creature_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('random.randint', side_effect=[2, 2])
    def test_hit(self, mock_randint):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 5, 'max_HP': 5, 'hit_die': 6}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 5, 'max_HP': 5}

        self.assertEqual(attack(attacker=creature_one, defender=creature_two), -2)

    @unittest.mock.patch('random.randint', side_effect=[2, 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hit_printed_output(self, mock_stdout, mock_randint):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 5, 'max_HP': 5, 'hit_die': 6}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        expected_output = 'Creature_One dealt 2 damage to Creature_Two!\n'

        attack(attacker=creature_one, defender=creature_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)



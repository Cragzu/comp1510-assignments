from unittest import TestCase
from monster import battle


class TestBattle(TestCase):

    def test_monster_killed(self):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 999, 'max_HP': 999, 'hit_die': 6}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 1, 'max_HP': 1, 'hit_die': 6}
        battle(character=creature_one, monster=creature_two)
        self.assertTrue(creature_two['HP'] == 0)

    def test_player_killed(self):
        creature_one = {'name': 'creature_one', 'description': 'testing', 'HP': 1, 'max_HP': 1, 'hit_die': 6}
        creature_two = {'name': 'creature_two', 'description': 'testing', 'HP': 999, 'max_HP': 999, 'hit_die': 6}
        self.assertRaises(SystemExit, battle, creature_one, creature_two)  # game exits

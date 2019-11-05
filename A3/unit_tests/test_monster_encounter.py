from unittest import TestCase
from monster import monster_encounter
import unittest.mock
import io


class TestMonsterEncounter(TestCase):  # todo: case for player dying

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('random.randint', return_value=3)
    def test_printed_output_no_monster(self, mock_randint, mock_stdout):  # check for error messages on invalid input
        expected_output = '\nThere don\'t seem to be any monsters here right now.\n' \
                          'You take a moment to catch your breath, healing a little.\n' \
                          'Alberto The Mighty\'s HP modified from 10 to 10\n'

        monster_encounter({'name': 'creature', 'description': 'testing'})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('monster.battle', return_value=None)
    @unittest.mock.patch('builtins.input', return_value='f')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('random.randint', return_value=1)
    def test_printed_output_fight_monster(self, mock_randint, mock_stdout, mock_input, mock_battle):
        expected_output = '\nYou encountered a testing creature!\n'
        monster_encounter({'name': 'creature', 'description': 'testing', 'HP': 5, 'max_HP': 5})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @unittest.mock.patch('random.randint', return_value=3)
    def test_printed_output_dead_monster(self, mock_randint, mock_stdout):  # check for error messages on invalid input
        expected_output = '\nYou see the corpse of the monster you\'d previously slain here. ' \
                          'Thankfully, it\'s still dead.\n' \
                          'You take a moment to catch your breath, healing a little.\n' \
                          'Alberto The Mighty\'s HP modified from 10 to 10\n'

        monster_encounter({'name': '', 'description': 'testing'})
        self.assertEqual(mock_stdout.getvalue(), expected_output)


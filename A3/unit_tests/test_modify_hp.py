from unittest import TestCase
from monster import modify_hp
import io
import unittest.mock


class TestModifyHp(TestCase):

    def test_modify_successful(self):
        creature = {'name': 'creature', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        modify_hp(entity=creature, value=-2)
        self.assertEqual(creature['HP'], 3)

    def test_modify_below_zero(self):
        creature = {'name': 'creature', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        modify_hp(entity=creature, value=-7)
        self.assertEqual(creature['HP'], 0)

    def test_modify_above_maximum(self):
        creature = {'name': 'creature', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        modify_hp(entity=creature, value=2)
        self.assertEqual(creature['HP'], 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output(self, mock_stdout):
        creature = {'name': 'creature', 'description': 'testing', 'HP': 5, 'max_HP': 5}
        expected_output = 'Creature\'s HP modified from 5 to 3\n'
        modify_hp(entity=creature, value=-2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


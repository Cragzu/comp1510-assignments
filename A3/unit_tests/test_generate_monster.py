from unittest import TestCase
from monster import generate_monster
from constants import MONSTER_DESCRIPTIONS, MONSTER_TYPES


class TestGenerateMonster(TestCase):

    def test_datatype(self):
        self.assertIsInstance(generate_monster(types=MONSTER_TYPES, descriptions=MONSTER_DESCRIPTIONS), dict)

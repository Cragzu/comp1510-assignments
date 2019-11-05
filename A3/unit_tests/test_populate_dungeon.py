from unittest import TestCase
from monster import populate_dungeon
from constants import GAME_BOARD


class TestPopulateDungeon(TestCase):

    def test_population_successful(self):
        populate_dungeon(GAME_BOARD)
        for row in GAME_BOARD:
            for room in row:
                self.assertIn('monster', room.keys())  # check that each room has a monster assigned

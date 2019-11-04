from unittest import TestCase
from map import valid_movements


class TestValidMovements(TestCase):

    def test_no_walls(self):
        self.assertEqual(valid_movements([2, 2]), [['(N)orth', '(S)outh', '(E)ast', '(W)est'], ['N', 'S', 'E', 'W']])

    def test_wall(self):
        self.assertEqual(valid_movements([0, 2]), [['(S)outh', '(E)ast', '(W)est'], ['S', 'E', 'W']])

    def test_corner(self):
        self.assertEqual(valid_movements([0, 0]), [['(S)outh', '(E)ast'], ['S', 'E']])


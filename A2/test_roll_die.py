from unittest import TestCase
from dungeonsanddragons import roll_die


class TestRollDie(TestCase):

    def test_negative_roll(self):
        self.assertEqual(0, roll_die(0, 1))

    def test_negative_sides(self):
        self.assertEqual(0, roll_die(1, 0))

    def test_successful(self):
        self.assertIn(roll_die(3, 6), range(3, 18))  # make sure result is within parameters

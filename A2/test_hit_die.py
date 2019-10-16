from unittest import TestCase
from dungeonsanddragons import hit_die


class TestHitDie(TestCase):

    def test_d12(self):
        self.assertIn(hit_die('barbarian'), range(1, 12))

    def test_d10(self):
        self.assertIn(hit_die('fighter'), range(1, 10))

    def test_d8(self):
        self.assertIn(hit_die('bard'), range(1, 8))

    def test_d6(self):
        self.assertIn(hit_die('wizard'), range(1, 6))

from unittest import TestCase
from question_8 import im_not_sleepy


class TestImNotSleepy(TestCase):

    def test_im_not_sleepy(self):
        self.assertIsInstance(im_not_sleepy(), str)

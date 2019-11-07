from unittest import TestCase
import unittest.mock
import io
from sud import victory
from constants import VICTORY_ROOM


class TestVictory(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_datatype(self, mock_stdout):
        victory(VICTORY_ROOM)
        self.assertIsInstance(mock_stdout.getvalue(), str)

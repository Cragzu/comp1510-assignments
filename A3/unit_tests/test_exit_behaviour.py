from unittest import TestCase
import unittest.mock
import io
from character import exit_behaviour


class TestExitBehaviour(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_quit(self, mock_stdout):
        expected_output = 'You successfully escaped the dungeon. Maybe you\'ll find the treasure another day...\n'
        exit_behaviour('quit')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_quit(self, mock_stdout):
        expected_output = 'You were defeated! Future adventurers will discover your remains as a gruesome warning...\n'
        exit_behaviour('death')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

from unittest import TestCase
from character import move
import unittest.mock
import io


class TestMove(TestCase):

    @unittest.mock.patch('character.input_loop', return_value='N')
    def test_move_north(self, mock_input_loop):
        self.assertEqual(move([2, 2]), [1, 2])

    @unittest.mock.patch('character.input_loop', return_value='S')
    def test_move_south(self, mock_input_loop):
        self.assertEqual(move([2, 2]), [3, 2])

    @unittest.mock.patch('character.input_loop', return_value='E')
    def test_move_east(self, mock_input_loop):
        self.assertEqual(move([2, 2]), [2, 3])

    @unittest.mock.patch('character.input_loop', return_value='W')
    def test_move_west(self, mock_input_loop):
        self.assertEqual(move([2, 2]), [2, 1])

    @unittest.mock.patch('character.input_loop', return_value='S')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_output_dead_end(self, mock_stdout, mock_input_loop):
        expected_output = 'You\'ve reached a dead end! Best not to continue past here ' \
                          'or you will likely be eaten by a grue...\n'
        move([0, 0])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

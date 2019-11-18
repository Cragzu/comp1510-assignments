from unittest import TestCase
from sud import introduction
import unittest.mock
import io


class TestIntroduction(TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['u', 's'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_datatype(self, mock_stdout, mock_input):
        introduction()
        self.assertIsInstance(mock_stdout.getvalue(), str)

import io
import random
import unittest.mock
from unittest import TestCase

from map import describe_room


class TestDescribeRoom(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_datatype(self, mock_stdout):

        for row in range(0, 4):
            for room in range(0, 4):
                describe_room([row, room])  # check every room to ensure it has a description
                self.assertIsInstance(mock_stdout.getvalue(), str)

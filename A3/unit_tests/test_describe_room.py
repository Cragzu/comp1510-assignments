import io
import random
import unittest.mock
from unittest import TestCase

from map import describe_room


class TestDescribeRoom(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_room(self, mock_stdout):

        describe_room([random.randint(0, 4), random.randint(0, 4)])  # check random room to ensure it has a description

        self.assertIsInstance(mock_stdout.getvalue(), str)


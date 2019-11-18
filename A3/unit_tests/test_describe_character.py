from unittest import TestCase
import unittest.mock
import io
from character import describe_character


class TestDescribeCharacter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_datatype(self, mock_stdout):
        creature = {'name': 'creature', 'description': 'testing', 'goal': 'to pass the unit test', 'HP': 5, 'max_HP': 5}
        describe_character(creature)
        self.assertIsInstance(mock_stdout.getvalue(), str)

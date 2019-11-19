from unittest import TestCase
from question_3 import dijkstra


class TestDijkstra(TestCase):

    def test_all_different(self):
        dutch = ['white', 'blue', 'red']
        dijkstra(dutch)
        self.assertEqual(dutch, ['red', 'white', 'blue'])

    def test_duplicates(self):
        dutch = ['white', 'white', 'red', 'red']
        dijkstra(dutch)
        self.assertEqual(dutch, ['red', 'red', 'white', 'white'])

    def test_no_changes(self):
        dutch = ['red', 'white']
        dijkstra(dutch)
        self.assertEqual(dutch, ['red', 'white'])

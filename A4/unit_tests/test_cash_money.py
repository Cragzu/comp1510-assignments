from unittest import TestCase
from question_5 import cash_money
import io
import unittest.mock


class TestCashMoney(TestCase):

    def test_amount(self):
        self.assertEqual(cash_money(66.53), {50: 1, 5: 3, 1: 1, 0.25: 2, 0.01: 3})

    def test_empty(self):
        self.assertEqual(cash_money(0.0), {})

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_argument(self, mock_stdout):
        expected_output = 'Cannot divide by that argument!\n'
        for i in ['a', 0]:
            cash_money(i)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

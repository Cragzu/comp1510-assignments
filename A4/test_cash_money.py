from unittest import TestCase
from question_5 import cash_money


class TestCashMoney(TestCase):

    def test_amount(self):
        self.assertEqual(cash_money(66.53), {50: 1, 5: 3, 1: 1, 0.25: 2, 0.01: 3})

    def test_empty(self):
        self.assertEqual(cash_money(0.0), {})

    # def test_invalid_argument(self):  # todo: enable when raising exception is implemented
    #     self.assertRaises(Exception, cash_money, 'a')

from unittest import TestCase
from dungeonsanddragons import choose_inventory
import unittest.mock
import io
from dungeonsanddragons import choose_inventory


class TestChooseInventory(TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['5', '4', '-1'])
    def test_expected_return(self, mock_input):
        self.assertEqual(choose_inventory(), ['Juggling Balls of JavaScript', 'Staff of Serenity'])

    @unittest.mock.patch('builtins.input', return_value='-1')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output(self, mock_stdout, mock_input):
        expected_output = "Welcome to Yolanda's Premium Adventure Shop! For all your dungeon-crawling needs.\n" \
                          "\nToday there are 14 shop items available. They are:\n" \
                          "1 - Sword of Sanctimony\n2 - Potion of Python\n3 - Daggers of Deception" \
                          "\n4 - Staff of Serenity\n5 - Juggling Balls of JavaScript\n6 - Detonator of Divide-by-Zero" \
                          "\n7 - Gloves of Genius\n8 - Map of Misdirection\n9 - Crossbow of Courage" \
                          "\n10 - Charm of Chris' Approval\n11 - Cloak of Confusion\n12 - Takashi's Donut Box" \
                          "\n13 - Bottle of Binary\n14 - Axe of Asking Questions\n\n\n"
        choose_inventory()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
"""
Module containing a function to convert a given int to its Roman Numerals equivalent.
"""


def convert_to_roman_numeral(positive_int):
    """
    Convert a given positive int to a string containing its equivalent in Roman Numerals.

    Repeatedly divides the given int by increasingly smaller values to determine how many of each letter in the
    Roman number system to add to the roman_string.

    :param positive_int: an int between 0 and 10000
    :precondition: positive_int must be an int greater than 0 and less than 10000
    :postcondition: calculate the equivalent to the given int in Roman Numerals
    :return: a string made up of capital letters from the Roman number system
    """
    roman_string = ""  # initialize empty string

    thousands = positive_int // 1000  # get number of thousands in the int
    roman_string += ("M" * thousands)  # add that many Ms to the string
    positive_int -= (thousands * 1000)  # remove all thousands from the int

    five_hundreds = positive_int // 500  # repeat the above steps for every roman letter
    roman_string += ("D" * five_hundreds)
    positive_int -= (five_hundreds * 500)

    hundreds = positive_int // 100
    roman_string += ("C" * hundreds)
    positive_int -= (hundreds * 100)

    fifties = positive_int // 50
    roman_string += ("L" * fifties)
    positive_int -= (fifties * 50)

    tens = positive_int // 10
    roman_string += ("X" * tens)
    positive_int -= (tens * 10)

    fives = positive_int // 5
    roman_string += ("V" * fives)
    positive_int -= (fives * 5)

    roman_string += ("I" * positive_int)  # ones don't need any further calculations

    return roman_string


def main():
    """
    Drive the program.

    Tests the function in this module.
    """
    int_to_convert = int(input("Enter a positive int to convert, 1 <= int <= 10000: "))

    print(convert_to_roman_numeral(int_to_convert))


if __name__ == "__main__":
    main()


'''
Take a positive int between 1 and 10,000 and turn it into the equivalent in roman numerals.

    I = 1       L = 50      M = 1000
    V = 5       C = 100
    X = 10      D = 500

Computational thinking:
    Decomposition: Break down the int into multiples of the above numbers that can then be translated to roman numerals.
    Pattern matching: Each section of the number can be translated the same way, simply dividing the original int
    by the value equivalent to the current letter.
'''

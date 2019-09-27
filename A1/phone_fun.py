"""
Module containing a function to play a rudimentary rock-paper-scissors game.
"""
import doctest


def replace_letter(character):
    """
    Determine the number equivalent to the given character in the standard phone system.

    :precondition: the given character must be of length 1, and capitalized if it is a letter
    :postcondition: function will return an int representative of the given char
    :param character: a string of length 1 (char), either a number or letter
    :return: a 1-digit number string equivalent to the given character in the phone system

    >>> replace_letter("3")
    '3'
    >>> replace_letter("G")
    '4'
    """
    if character in "0123456789":  # char is already a number, do nothing
        return character

    else:  # replace letter with the appropriate number
        if character in "ABC":
            return "2"
        elif character in "DEF":
            return "3"
        elif character in "GHI":
            return "4"
        elif character in "JKL":
            return "5"
        elif character in "MNO":
            return "6"
        elif character in "PQRS":
            return "7"
        elif character in "TUV":
            return "8"
        elif character in "WXYZ":
            return "9"


def number_translator():
    """
    Convert a phone number containing some combination of letters and numbers to one containing only numbers.

    :precondition: user input must be a 10-digit phone code containing numbers and/or letters in the format xxx-xxx-xxxx
    :postcondition: function will return a converted phone number with all letters replaced with digits
    :return: a 12-character string equivalent to the given phone number containing only numbers and two dashes
    """
    initial_number = (input("Enter a 10-digit phone number: ")).upper()  # get the input, convert to uppercase
    print(initial_number)
    final_number = ""

    final_number += replace_letter(initial_number[0])  # replace each digit individually without loops
    final_number += replace_letter(initial_number[1])
    final_number += replace_letter(initial_number[2])

    final_number += "-"  # index 3

    final_number += replace_letter(initial_number[4])
    final_number += replace_letter(initial_number[5])
    final_number += replace_letter(initial_number[6])

    final_number += "-"  # index 7

    final_number += replace_letter(initial_number[8])
    final_number += replace_letter(initial_number[9])
    final_number += replace_letter(initial_number[10])
    final_number += replace_letter(initial_number[11])

    return final_number


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    doctest.testmod()

    print(number_translator())


if __name__ == "__main__":
    main()

'''
Get a 10-digit telephone number as user input, in the format xxx-xxx-xxxx. Return the number with any letters
translated into their numerical equivalent. 

    ex. 555-GET-FOOD = 555-438-3663
    A, B, C = 2         D, E, F = 3
    G, H, I = 4         J, K, L = 5
    M, N, O = 6         P, Q, R, S = 7
    T, U, V = 8         W, X, Y, Z = 9
    
Computational thinking:
    Decomposition: Broke down the function into a helper function that could be called repeatedly. Called the function
    10 times manually here, but could use a loop for conciseness.
    Abstraction: Used "if in" statements to check characters against multiple strings of letters at once rather than
    each letter individually.
'''

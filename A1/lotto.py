"""
Module containing a function to play a rudimentary rock-paper-scissors game.
"""
import random


def number_generator():
    """
    Generate a lottery ticket composed of 6 random ints sorted in ascending order.

    Use the built-in Python methods sample, range, and sort to efficiently complete the task.

    :precondition: none, function requires no arguments
    :postcondition: function will return a list of lottery numbers
    :return: a sorted list of 6 random ints between 1 and 49.
    """

    lotto_numbers = (random.sample(range(1, 49), 6))  # generate 6 unique random ints from 1-49

    lotto_numbers.sort()  # sort from lowest to highest
    return lotto_numbers


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    print(number_generator())


if __name__ == "__main__":
    main()


'''
Generate six unique random numbers from 1-49 and print them out in order from lowest to highest.

Computational thinking:
    Automation: Make use of python random methods to solve the problem, don't reinvent things unnecessarily
'''
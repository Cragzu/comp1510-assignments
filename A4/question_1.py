"""
Part 1 of 8: Module containing the sieve of Eratosthenes algorithm for finding prime numbers.
"""
import math
# todo: unit tests


def is_prime(num: int) -> bool:
    """
    Check whether a number is prime.

    Immediately returns False if the number is below 2 as these will never be prime.
    Otherwise, loops through every number between 2 and the square root of the given num, and divides num by each to
    check the remainder. If no divisions result in a remainder of 0, the number is prime.

    :param num: int
    :return: a bool representing whether or not the given num is prime.

    >>>is_prime(8)
    False
    >>>is_prime(7)
    True
    """
    if num < 2:  # account for edge cases of 2, 1, 0, negative numbers
        return False

    for i in range(2, round(math.sqrt(num))):  # only need to check up to square root of number
        if num % i == 0:  # number is divisible by something; not prime
            return False

    return True  # number is not divisible by anything


def eratosthenes(upperbound: int) -> list:
    """
    Create a list of prime numbers between 0 and upperbound.

    Creates an initial list of every number between 2 and upperbound. Creates a copy to modify, and loops through the
    list checking if each number is prime. If it is, remove all its multiples from the list. Stop the process once
    the loop reaches the square root of upperbound, as continuing past this point changes nothing.

    :param upperbound: int
    :precondition: upperbound must be a positive int
    :return: a list containing all prime numbers between 0 and the given upperbound
    """
    range_list = list(range(2, upperbound))  # make a list of all numbers between 2 and upperbound, ignore 0 and 1
    primes = range_list  # list to modify

    for index, value in enumerate(range_list):
        if value >= math.sqrt(upperbound):
            break
        if is_prime(value):
            for higher_num in range_list[(index + 1):]:  # all items after the current item
                if higher_num % value == 0:
                    primes.remove(higher_num)

    return primes


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    print(eratosthenes(30))


if __name__ == "__main__":
    main()
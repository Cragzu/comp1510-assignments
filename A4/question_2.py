"""
Part 2 of 8: Module containing an algorithm for finding the greatest common divisor of two ints.
"""


def gcd(a: int, b: int) -> int:
    """
    Determine the greatest common divisor of the two given ints a and b.

    Checks if b is 0, returns a if true. a will be the GCD.
    If b is not 0, calls itself with the remainder of a/b and b. Continues until b is 0.

    :param a: int
    :param b: int
    :precondition: a and b must be non-zero ints
    :return: an int representing the GCD of a and b.

    >>>gcd(270, 192)
    6
    """
    if b == 0:  # check to break out of recursion
        return a  # the non-zero value; the GCD

    try:
        return gcd(b, a % b)  # standard recursion, get remainder of a/b and continue with b and the remainder

    except TypeError:
        print('The given argument was not int!')


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    print(gcd('a', 15))


if __name__ == "__main__":
    main()

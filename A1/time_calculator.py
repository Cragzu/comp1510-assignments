"""
Module containing a function to calculate the number of days, hours and minutes in a given number of seconds.
"""

SECONDS_IN_DAY = 84600
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def time_calculator(seconds):
    """
    Convert the param seconds into its equivalent in days, hours, minutes, and seconds.

    Repeatedly divide the given int by consts representing the number of seconds in each time unit. Add each result
    to a variable, and print them all separated by white space.

    :precondition: seconds must be a positive integer
    :postcondition: prints the equivalent number of days, hours, minutes, and seconds separated by white space
    :param seconds: a positive int representing the number of seconds to be converted
    :return: none, uses print instead
    """
    days = seconds // SECONDS_IN_DAY  # divide by number of seconds in a day to get number of days
    seconds -= (days * SECONDS_IN_DAY)  # subtract all multiples of days from the int

    hours = seconds // SECONDS_IN_HOUR  # repeat as above
    seconds -= (hours * SECONDS_IN_HOUR)

    minutes = seconds // SECONDS_IN_MINUTE
    seconds -= (minutes * SECONDS_IN_MINUTE)

    print(days, hours, minutes, seconds, sep=" ")  # print all values separated by white space


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    time_calculator(99999)
    time_calculator(60)
    time_calculator(84600)
    time_calculator(3)


if __name__ == "__main__":
    main()


'''
Get an int representing a number of seconds, find the number of days, hours, and minutes in that number.

    84,600 seconds = 1 day
    3,600 seconds = 1 hour
    60 seconds = 1 minute

Computational thinking:
    Decomposition: Break down the int into multiples of the time unit consts to find the needed values.
    Automation and pattern matching: Noticing that this problem can be solved similarly to the previous roman_numerals
    problem, emulating and altering that as necessary.
'''

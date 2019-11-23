"""
Part 8 of 8: Module containing an algorithm to find the time that
displays the largest number of bars on a digital clock.
"""


def find_highest_bars(lowerbound: int, upperbound: int, padding=None) -> list:
    """
    Find the number requiring the highest number of bars to represent on a digital clock between the given parameters.

    Loop through the numbers. Optionally pad the number with a leading padding, convert to string. Check the digits
    against the amounts_of_bars dict to find the number requiring the most bars.

    :param lowerbound: int
    :param upperbound: int
    :param padding: optional, a string to pad the 1-digit numbers with. Likely 0.
    :precondition: padding must be a number 0-9
    :precondition: lowerbound must be less than upperbound, they must both be ints
    :return: a list containing the number and its required number of bars

    >>>find_highest_bars(1, 9)
    ['8', 7]
    """
    # number: amount of bars
    amounts_of_bars = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

    greatest_amount = 0
    most_bars = 0
    current_amount = 0

    for number in range(lowerbound, upperbound):

        num_string = str(number)

        if padding:  # pad with leading number if given
            if len(num_string) == 1:
                num_string = padding + num_string

        for digit in num_string:
            current_amount += amounts_of_bars[digit]

        if current_amount > greatest_amount:
            greatest_amount = current_amount
            most_bars = num_string

        current_amount = 0

    return [most_bars, greatest_amount]


def im_not_sleepy() -> str:
    """
    Finds the time on a digital clock that takes the most bars to represent.

    :precondition: find_highest_bars must work as expected
    :return: a string displaying the found time and its number of bars
    """

    hours = find_highest_bars(1, 13)  # check 1-12
    minutes = find_highest_bars(0, 60, '0')  # check 0-59, pad with extra 0

    output = 'The greatest amount of bars on a clock is at the time ' + hours[0] + ':' + minutes[0]\
             + ' with ' + str(hours[1] + minutes[1]) + ' bars.'

    return output


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    print(im_not_sleepy())


if __name__ == "__main__":
    main()

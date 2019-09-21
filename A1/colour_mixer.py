"""
Module containing a function to mix two primary colours into a secondary colour.
"""


def red_colour_check(first_check, second_check):
    """
    Check whether the given parameters are "red" and another primary colour.

    :precondition: first_check must be a string, and should be "red" for the function to return a colour.
    :precondition: second_check must be a string, and should be "blue" or "yellow" for the function to return a colour.
    :postcondition: function will output either a colour or False, depending on what the inputs were as listed above.
    :param first_check: a string representing the first given colour.
    :param second_check: a string representing the second given colour.
    :return: a string representing the secondary colour made by the two primary colours, or False if there is none.
    """
    if first_check == "red":
        if second_check == "yellow":
            return "orange"
        elif second_check == "blue":
            return "purple"

    return False


def yellow_colour_check(first_check, second_check):
    """
    Check whether the given parameters are "yellow" and "blue".

    :precondition: first_check must be a string, and should be "yellow" for the function to return "green".
    :precondition: second_check must be a string, and should be "blue" for the function to return "green".
    :postcondition: function will output either "green "or False, depending on what the inputs were as listed above.
    :param first_check: a string representing the first given colour.
    :param second_check: a string representing the second given colour.
    :return: a string containing "green", or False if the inputs were not "yellow" and "blue".
    """
    if first_check == "yellow":
        if second_check == "blue":
            return "green"

    return False


def colour_mixer():
    """
    Find the secondary colour created by mixing the two given primary colours.

    Gets the two strings as user input and passes them into the helper functions in both possible positions.

    If the whole function has been executed with no return, the colours were invalid. Returns a helpful error message.

    :precondition: first_colour must be a string, and should be a primary colour
    :precondition: second_colour must be a string, and should be a primary colour different from first_colour
    :postcondition: find the secondary colour created by mixing the given primary colours
    :return: a string containing the created secondary colour, or an error message if the input was invalid
    """
    first_colour = input("Enter a primary colour: ")
    second_colour = input("Enter another primary colour: ")

    if red_colour_check(first_colour, second_colour):  # if the function returns a colour, not False
        return red_colour_check(first_colour, second_colour)

    elif red_colour_check(second_colour, first_colour):
        return red_colour_check(second_colour, first_colour)

    # if red is not one of the colours, yellow must be one of the colours for it to be valid
    elif yellow_colour_check(first_colour, second_colour):
        return yellow_colour_check(first_colour, second_colour)

    elif yellow_colour_check(second_colour, first_colour):
        return yellow_colour_check(second_colour, first_colour)

    return "The entered colours were invalid. Please enter two different primary colours (red, yellow, or blue)."


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    print(colour_mixer())


if __name__ == "__main__":
    main()


'''
Get two strings representing primary colours, create functions that go through a sequence of if statements to find 
the secondary colour they will mix into and print it; or print an error message if the input is invalid.

    red + yellow = orange, red + blue = purple, blue + yellow = green

Computational thinking:
    Decomposition: First consider all cases when one colour exists, then move on to the other. Make helper functions
    that will allow this program to work as efficiently as possible using only the basics of Python.
    Pattern matching: Noticing that if red does not exist, the only possible options are yellow and blue. Don't bother
    repeating code by checking things twice.
'''

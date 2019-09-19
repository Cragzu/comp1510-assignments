"""
Module containing a function to mix two primary colours into a secondary colour.
"""


def colour_mixer():
    """
    Find the secondary colour created by mixing the two given primary colours.

    Gets the two strings as user input and adds them to a list. Uses nested if statements to determine which two
    colours were given, and returns the appropriate secondary colour.

    If the whole function has been executed with no return, the colours were invalid. Returns a helpful error message.

    :precondition: first_colour must be a string, and should be a primary colour
    :precondition: second_colour must be a string, and should be a primary colour different from first_colour
    :postcondition: find the secondary colour created by mixing the given primary colours
    :return: a string containing the created secondary colour, or an error message if the input was invalid
    """
    colours = []
    first_colour = input("Enter a primary colour: ")
    second_colour = input("Enter another primary colour: ")
    colours.extend((first_colour, second_colour))

    if "red" in colours:
        if "yellow" in colours:
            return "orange"
        elif "blue" in colours:
            return "purple"

    elif "yellow" in colours:  # if red is not one of the colours, yellow must be one of the colours for it to be valid
        if "blue" in colours:
            return "green"

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
Get two strings representing primary colours, go through a sequence of if statements to find the secondary colour
they will mix into and print it; or print an error message if the input is invalid.

    red + yellow = orange, red + blue = purple, blue + yellow = green

Computational thinking:
    
'''

"""
Module containing functions that manage the character/user in the SUD.
"""
from constants import PLAYER
# todo: should contain character description, health, healing


def describe_character(character):
    """
    Print information about the user's character.

    :param character: a dictionary containing character information
    :precondition: the character dict must be properly formed, with keys for name, description, goal, HP, and max_HP
    :return: none, uses print statements
    """
    print('You are', (character['name'] + '.'), character['description'])
    print('Your goal:', (character['goal'] + '.'))

    print('\nCurrent HP:', (str(character['HP']) + '/' + str(character['max_HP'])))


def input_loop(prompt, valid_choices):
    """
    Prompt the user repeatedly for a choice until a valid input is entered.

    :param prompt: a string describing what the user can choose from
    :param valid_choices: a list containing chars representing the available choices
    :precondition: the valid_choices list must contain only length-1 strings of capital letters
    :return: a char representing the user's choice
    """
    valid_input = False
    while not valid_input:
        user_choice = (input(prompt)).upper()

        if user_choice not in valid_choices:  # check if input is valid
            print('Sorry, that wasn\'t a valid input. Please try again.')

        else:
            valid_input = True

    return user_choice


def move(current_position):
    print('Current position:', current_position)
    # todo: make this dynamic? how?

    direction = input_loop('Move (N)orth, (S)outh, (E)ast, or (W)est?: ', ['N', 'S', 'E', 'W'])

    if direction == 'N':
        current_position[0] += 1

    elif direction == 'S':
        current_position[0] -= 1

    elif direction == 'E':
        current_position[1] += 1

    elif direction == 'W':
        current_position[1] -= 1

    print('New position:', current_position)
    return current_position


def main():
    """
    Drive the SUD program.
    """

    describe_character(PLAYER)

if __name__ == "__main__":
    main()

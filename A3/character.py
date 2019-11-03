"""
Module containing functions that manage the character/user in the SUD.
"""
from constants import PLAYER
from map import valid_movements


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


def input_loop(prompt, valid_choices):  # todo: typing quit should end program
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


def move(current_position):  # todo: docstring
    """

    :param current_position:
    :return:
    """
    print('Current position:', current_position)  # todo: remove this later

    prompt_list = valid_movements(current_position)[0]

    if len(prompt_list) < 4:
        print('You\'ve reached a wall! Best not to continue past here or you will likely be eaten by a grue...')

    prompt = 'Which direction to move? You can go: '
    for i in prompt_list:
        prompt += (i + ' ')

    direction = input_loop(prompt, valid_movements(current_position)[1])

    if direction == 'N':
        current_position[0] -= 1

    elif direction == 'S':
        current_position[0] += 1

    elif direction == 'E':
        current_position[1] += 1

    elif direction == 'W':
        current_position[1] -= 1

    print('New position:', current_position) # todo: remove this later
    return current_position

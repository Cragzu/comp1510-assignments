"""
Module containing functions that manage the character/user in the SUD.
"""
from map import valid_movements
import atexit


def exit_behaviour(case: str):
    """
    Print statements before exiting the program.

    :param case: a string representing the code for the string to print
    :precondition: case must be one of the specified strings, else function will default to a generic quit message.
    :postcondition: function will print the appropriate statement depending on the situation in which the user exits.
    :return: none, uses print statements
    """
    if case == 'death':
        print('You were defeated! Future adventurers will discover your remains as a gruesome warning...')

    else:
        print('You successfully escaped the dungeon. Maybe you\'ll find the treasure another day...')


def describe_character(character: dict):
    """
    Print information about the user's character.

    :param character: a dictionary containing character information
    :precondition: the character dict must be properly formed, with keys for name, description, goal, HP, and max_HP
    :return: none, uses print statements
    """
    print('You are', (character['name'] + '.'), character['description'])
    print('Your goal:', (character['goal'] + '.'))

    print('\nCurrent HP:', (str(character['HP']) + '/' + str(character['max_HP'])))


def input_loop(prompt: str, valid_choices: list) -> str:
    """
    Prompt the user repeatedly for a choice until a valid input is entered.

    :param prompt: a string describing what the user can choose from
    :param valid_choices: a list containing chars representing the available choices
    :precondition: the valid_choices list must contain only length-1 strings of capital letters
    :return: a string representing the user's choice; one of the strings in valid_choices
    """
    valid_choices.append('QUIT')  # account for quitting the program

    valid_input = False
    while not valid_input:
        user_choice = (input(prompt)).upper()

        if user_choice not in valid_choices:  # check if input is valid
            print('Sorry, that wasn\'t a valid input. Please try again.')

        elif user_choice == 'QUIT':
            atexit.register(exit_behaviour, case='quit')
            exit()

        else:
            valid_input = True

    return user_choice


def move(current_position: list) -> list:
    """
    Update the character's position on the game board.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: an updated version of current_position with one of the ints incremented
    """
    prompt_list = valid_movements(current_position)[0]

    if len(prompt_list) < 4:
        print('You\'ve reached a dead end! Best not to continue past here or you will likely be eaten by a grue...')

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

    return current_position

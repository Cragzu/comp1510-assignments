"""
Module containing logic for the game board of the SUD.
"""
from constants import GAME_BOARD


def describe_room(current_position):
    """
    Print a description of the current room.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: none, uses print statements
    """
    room = GAME_BOARD[current_position[0]][current_position[1]]
    print(room['description'] + '\n')


def valid_movements(current_position):
    """
    Determine which movements can be taken based on the user's position in the game board.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: a list containing two lists with only the valid options

    >>> valid_movements([2, 2])
    [['(N)orth', '(S)outh', '(E)ast', '(W)est'], ['N', 'S', 'E', 'W']]

     >>> valid_movements([0, 0])
    [['(S)outh', '(E)ast'], ['S', 'E']]
    """
    instructions = ['(N)orth', '(S)outh', '(E)ast', '(W)est']  # for printing available options
    directions = ['N', 'S', 'E', 'W']

    if current_position[0] == 0:  # against north wall, cannot move north
        directions.remove('N')
        instructions.remove('(N)orth')

    if current_position[0] == 4:  # against south wall, cannot move south
        directions.remove('S')
        instructions.remove('(S)outh')

    if current_position[1] == 0:  # against west wall, cannot move west
        directions.remove('W')
        instructions.remove('(W)est')

    if current_position[1] == 4:  # against east wall, cannot move east
        directions.remove('E')
        instructions.remove('(E)ast')

    return [instructions, directions]

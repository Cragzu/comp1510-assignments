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
    print(room['description'])


def main():
    """
    Drive the SUD program.
    """



if __name__ == "__main__":
    main()

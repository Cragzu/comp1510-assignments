"""
Module containing logic for the game board of the SUD.
"""
from monster import generate_monster
from constants import GAME_BOARD, MONSTER_TYPES, MONSTER_DESCRIPTIONS


def populate_dungeon(dungeon):
    """
    Populate the rooms in the dungeon dungeon with monsters.

    :param dungeon: a list containing dungeon rooms
    precondition: dungeon is a properly formed matrix; a list containing 5 lists with 5 dicts representing 25 rooms
    :return: none, modifies the given dungeon
    """
    for row in dungeon:
        for room in row:
            room['monster'] = generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS)


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
    print('Before: \n', GAME_BOARD)
    populate_dungeon(GAME_BOARD)
    print('\n \n After: \n', GAME_BOARD)


if __name__ == "__main__":
    main()

"""
Main module that runs the Single User Dungeon.
"""
# todo: imports go here. should be importing most things from here
from constants import GAME_BOARD, PLAYER, VICTORY_ROOM
from map import describe_room
from character import describe_character, input_loop, move
from monster import populate_dungeon


def introduction():
    """
    Print introductory text for the player.

    Teach the player how to play and present them with their character and objectives.

    :return: none, uses print statements
    """
    print('Welcome to the dungeon!\n')

    print('~~~How to Play~~~')
    print('You will be wandering through the twisty tunnels, fighting monsters and searching for the treasure room.'
          '\nWhen prompted to interact, you will be presented with various options. You can input the letter '
          'corresponding to the one in parentheses () that goes with your desired choice (case doesn\'t matter).')

    input_loop('\nPlease confirm you (U)nderstand how to interact: ', ['U'])
    print('\nGreat! One more thing: you can type "quit" at any time to end the game.')

    input_loop('\nReady to (S)tart?: ', ['S'])

    print('Entering the dungeon...\n')


def gameplay_loop():

    current_position = [2, 2]  # starting position

    victory_reached = False
    while not victory_reached:
        describe_character(PLAYER)
        move(current_position)
        if current_position == VICTORY_ROOM:  # quit
            victory_reached = True  # todo: victory text? in separate function


def main():
    """
    Drive the SUD program.
    """

    #introduction()

    populate_dungeon(GAME_BOARD)

    gameplay_loop()


if __name__ == "__main__":
    main()

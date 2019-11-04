"""
Main module that runs the Single User Dungeon.
"""
# todo: imports go here. should be importing most things from here
from constants import GAME_BOARD, PLAYER, VICTORY_ROOM
from map import describe_room
from character import describe_character, input_loop, move
from monster import populate_dungeon, monster_encounter


def dividing_line():
    """
    Prints a line to divide sections of printed output.
    :return: none
    """
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')  # dividing line


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
    dividing_line()


def gameplay_loop():
    """
    Run the game.

    Continuously loop the gameplay until the user wins or quits.

    :return: none
    """
    current_position = [2, 2]  # starting position

    victory_reached = False
    while not victory_reached:

        describe_room(current_position)
        describe_character(PLAYER)
        move(current_position)

        if current_position == VICTORY_ROOM:  # quit
            victory_reached = True

        current_monster = GAME_BOARD[current_position[0]][current_position[1]]['monster']  # get monster from matrix
        monster_encounter(current_monster)

        dividing_line()

    victory(current_position)


def victory(current_position):
    """
    Print victory text and end the game.

    :param current_position: a list containing two coordinates equivalent to the room location
    :return: none
    """

    dividing_line()
    describe_room(current_position)

    print('You found the treasure! You win!')
    print('Thank you for playing.')


def main():
    """
    Drive the SUD program.
    """

    introduction()

    populate_dungeon(GAME_BOARD)

    gameplay_loop()


if __name__ == "__main__":
    main()

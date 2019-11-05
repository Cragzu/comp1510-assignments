"""
Main module that runs the Single User Dungeon.
"""
from constants import GAME_BOARD, PLAYER, VICTORY_ROOM, DIVIDING_LINE
from map import describe_room
from character import describe_character, input_loop, move
from monster import populate_dungeon, monster_encounter

# todo: unit tests

def introduction():
    """
    Print introductory text for the player.

    Teach the player how to play and present them with their character and objectives.

    :precondition: this function should be executed as the first thing in the game.
    :postcondition: function will print helpful introductory text and instructions, and provide a simple input tutorial.
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
    print(DIVIDING_LINE)


def gameplay_loop():
    """
    Run the game.

    Continuously loop the gameplay until the user wins or quits.

    :postcondition: the game will be over once this function terminates.
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

        print(DIVIDING_LINE)

    victory(current_position)


def victory(current_position: list):
    """
    Print victory text and end the game.

    :param current_position: a list containing two coordinates equivalent to the room location
    :precondition: function should only be executed when the player has won the game
    :postcondition: function will print victory text and end the program.
    :return: none, uses print statements
    """

    print(DIVIDING_LINE)
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

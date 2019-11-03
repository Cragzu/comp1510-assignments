"""
Main module that runs the Single User Dungeon.
"""
# todo: imports go here
from map import GAME_BOARD


def move(current_position):
    print('Current position:', current_position)
    # todo: make this dynamic? how?

    direction = input_loop('Move (N)orth, (S)outh, (E)ast, or (W)est?: ', ['N', 'S', 'E', 'W'])

    if direction == 'n':
        current_position[0] += 1

    elif direction == 's':
        current_position[0] -= 1

    elif direction == 'e':
        current_position[1] += 1

    elif direction == 'w':
        current_position[1] -= 1

    print('New position:', current_position)
    return current_position

def describe_room(current_position):
    pass


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


def main():
    """
    Drive the SUD program.
    """
    pos = move([2, 2])
    #print(pos, pos[0], pos[1])

    #print(GAME_BOARD[1][2])

    room = GAME_BOARD[pos[0]][pos[1]]

    print(room['description'])


if __name__ == "__main__":
    main()

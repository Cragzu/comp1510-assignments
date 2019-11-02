"""
Main module that runs the Single User Dungeon.
"""
# todo: imports go here
from map import GAME_BOARD


def move(current_position):
    print('Current position:', current_position)

    direction_options = ['n', 's', 'e', 'w']  # todo: make this dynamic? how?

    input_loop = True
    while input_loop:

        direction = input('Move (N)orth, (S)outh, (E)ast, or (W)est?: ')

        if direction not in direction_options:
            print('Sorry, that wasn\'t a valid movement. Please try again.')

        else:
            if direction.lower() == 'n':
                current_position[0] += 1

            elif direction.lower() == 's':
                current_position[0] -= 1

            elif direction.lower() == 'e':
                current_position[1] += 1

            elif direction.lower() == 'w':
                current_position[1] -= 1

            input_loop = False


    print('New position:', current_position)




def main():
    """
    Drive the SUD program.
    """
    move([2, 2])



if __name__ == "__main__":
    main()

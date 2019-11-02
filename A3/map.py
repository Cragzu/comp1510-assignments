"""
Module containing logic for the game board of the SUD.
"""

# a matrix, a list containing lists containing dicts with room info
GAME_BOARD = [[
    # first row - [0][0] through [0][4]
    {"description": "Placeholder"}, 
    {"description": "Placeholder"}, 
    {"description": "Placeholder"}, 
    {"description": "Placeholder"}, 
    {"description": "Placeholder"}],

    # second row - [1][0] through [1][4]
    [{"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}],

    # third row - [2][0] through [2][4]
    [{"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Center room"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}],

    # fourth row - [3][0] through [3][4]
    [{"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}],

    # fifth row - [4][0] through [4][4]
    [{"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}, 
     {"description": "Placeholder"}
     ]]


def main():
    """
    Drive the SUD program.
    """
    print(GAME_BOARD[2][2])


if __name__ == "__main__":
    main()
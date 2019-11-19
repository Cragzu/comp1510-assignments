"""
Part 3 of 8: Module containing the Dutch National Flag function by Edsgar Dijkstra.
"""


def dijkstra(colors: list):
    """
    Sort a given list of randomly shuffled 'red', 'white', and 'blue' strings into that order.
    
    :param colors: a list of strings
    :precondition: colors must contain any number of the strings 'red', 'white', and 'blue'
    :return: none, modifies the given list
    """
    color_order = {'red': 0, 'white': 1, 'blue': 2}
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(colors) - 1):
            if color_order[colors[i]] > color_order[colors[i + 1]]:  # bubble sort, check list items against dict value
                colors[i], colors[i + 1] = colors[i + 1], colors[i]  # swap the items
                is_sorted = False  # list is not yet sorted if a swap was made


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    dutch = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
    print('Unsorted:', dutch)
    dijkstra(dutch)
    print('Sorted:', dutch)


if __name__ == "__main__":
    main()

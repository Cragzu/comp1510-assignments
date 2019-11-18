"""
Part 4 of 8: Module containing a selection sort algorithm.
"""


def selection_sort(list_to_sort: list):
    """
    Sort a list using a selection sort algorithm.

    Loop through the list, then start an inner loop through the sorted section of the list. Check every item in that
    section to find the smallest, then swap the first item in the section with the smallest item.

    Repeat until the end of the list is reached.

    :param list_to_sort: a list
    :precondition: list_to_sort must contain a non-empty list containing sortable items
    :postcondition: function will aise an error if list_to_sort is not a non-empty list of sortable items
    :return: a list containing the same items as list_to_sort, sorted in ascending order
    """
    if not list_to_sort:  # todo: raising error for empty list or list of unsortable items
        raise Exception('The list doesn\'t contain sortable items! The given list was: {}'.format(list_to_sort))

    for unsorted_section in range(len(list_to_sort)):  # repeat as many times as the vector length

        for i in range(unsorted_section, len(list_to_sort)):  # iterate through list at each position
            smallest_index = unsorted_section  # set index to first index of unsorted section

            if list_to_sort[i] < list_to_sort[smallest_index]:  # check each item against smallest
                smallest_index = i  # update smallest index

        list_to_sort[unsorted_section], list_to_sort[smallest_index] = \
            list_to_sort[smallest_index], list_to_sort[unsorted_section]  # swap first index of unsorted with smallest

    return list_to_sort


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    unsorted = [3, 5, 1, 9, -4]
    print("Unsorted:", unsorted)
    sorted_copy = selection_sort(unsorted)
    print("Sorted:", sorted_copy)


if __name__ == "__main__":
    main()

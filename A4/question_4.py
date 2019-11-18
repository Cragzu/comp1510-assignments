"""
Part 4 of 8: Module containing a selection sort algorithm.
"""


def selection_sort(list_to_sort: list):
    smallest = 100
    for count in range(len(list_to_sort)):  # repeat as many times as the vector length

        for i in range(count, len(list_to_sort)):  # iterate through list at each position
            if list_to_sort[i] < smallest:  # check each item against smallest
                smallest = list_to_sort[i]  # update smallest

        list_to_sort.remove(smallest)
        list_to_sort.insert(count, smallest)
        smallest = 100

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

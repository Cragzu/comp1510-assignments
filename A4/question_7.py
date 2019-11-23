"""
Part 7 of 8: Module containing a refactor of an existing script that calculates calorie amounts.
The script is reworked to be modular and atomic.
"""


def update_dict(item: str, document: dict) -> dict:
    """
    Add a new user-given item to the dict constant.

    Gets user's input for the value, then adds the new key-value pair to the dict.

    :param item: str
    :param document: dict
    :precondition: user input for calories must be convertible to int
    :return: a dict equal to the given document with one new k-v pair
    """
    try:
        new_item_calories = int(input("Enter calories for " + item + ": "))
        document[item] = new_item_calories
    except ValueError:
        print('Calories must be a number!')

    return document


def calculate_calories(document: dict):
    """
    Calculate the total calories and average calories per item in the global dict const.

    :precondition: all values in global _calories are ints
    :return: none, uses print statements
    """
    total_calories = 0

    for item in document:
        total_calories += document[item]  # this should always be int as exception was caught in update_dict

    avg_calories = total_calories / len(document)
    print("Total Calories:", total_calories, "Average Calories: %0.1f\n" % avg_calories)


def display_keys(document: dict):
    """
    Display all the keys in the global dict const as sorted list items.

    Creates a list of every key in the dict, sorts it alphabetically, and prints it.

    :return: none, uses print statement
    """
    food_item_names = [item for item in document]  # refactored to use list comprehension

    print("Food Items:", sorted(food_item_names))


def update_calories():
    """
    Add new key-value pairs to the global dict const through user input.

    Repeatedly prompts the user to enter a new item, ending when they enter 'q'. Adds the item to the dict with the
    value (calorie amount) from input. Displays information about the current dict items.
    :return: none
    """

    # Global Constant
    _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                 "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

    # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")

    while new_item != "q":
        _calories = update_dict(new_item, _calories)
        display_keys(_calories)
        calculate_calories(_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    update_calories()


if __name__ == "__main__":
    main()

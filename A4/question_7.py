"""
Part 7 of 8: Module containing a refactor of an existing script that calculates calorie amounts.
The script is reworked to be modular and atomic.
"""
# Global Constant
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
             "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}


def update_dict(item: str):
    """
    Add a new user-given item to the dict constant.

    Gets user's input for the value, then adds the new key-value pair to the dict.

    :param item: str
    :precondition: user input for calories must be convertible to int
    :return: none, modifies the _calories dict constant.
    """
    try:
        new_item_calories = int(input("Enter calories for " + item + ": "))
        _calories[item] = new_item_calories
    except ValueError:
        print('Calories must be a number!')


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """


    # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")

    while new_item != "q":
        update_dict(new_item)

        total_calories = 0

        for item in _calories:
            total_calories += _calories[item]

        food_item_names = [item for item in _calories]  # refactored to use list comprehension

        avg_calories = total_calories / len(_calories)
        print("\nFood Items:", sorted(food_item_names))
        print("Total Calories:", total_calories, "Average Calories: %0.1f\n" % avg_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")


if __name__ == "__main__":
    main()

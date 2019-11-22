"""
Part 7 of 8: Module containing a refactor of an existing script that calculates calorie amounts.
The script is reworked to be modular and atomic.
"""


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    # Global Constant
    _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                 "cheese": 115, "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

    # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")

    while new_item != "q":
        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories
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

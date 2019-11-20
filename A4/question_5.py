"""
Part 5 of 8: Module containing a function to sort amounts of money into denominations.
"""


def cash_money(amount: float) -> dict:  # todo: raise exception if amount is not positive double
    """
    Calculate the number of each type of bill and coin there is in a given amount of money.

    Sets up an initial dict with each type of bill/coin, all values initially 0. Loops through the dict, dividing
    the given amount by each key and determining the amount.

    Removes all dict entries with 0 values once finished.

    :param amount: float
    :precondition: amount must be a positive double
    :return: a dict with k/v pairs representing each denomination and number of it

    >>>cash_money(66.53)
    {50: 1, 5: 3, 1: 1, 0.25: 2, 0.01: 3}
    """
    breakdown = {100: 0, 50: 0, 20: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}  # setup dict

    for key in breakdown.keys():  # loop through dict
        denomination = int(amount // key)
        breakdown[key] = denomination  # set value to amount of that denomination
        amount -= denomination * key

    breakdown = {k: v for k, v in breakdown.items() if v != 0}  # remove empty keys

    return breakdown


def main():
    """
    Drive the program.

    Showcases the function defined in this module.
    """
    print(cash_money(66.53))


if __name__ == "__main__":
    main()


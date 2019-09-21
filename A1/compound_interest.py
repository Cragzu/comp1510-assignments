"""
Module containing a function to calculate the amount of money in a bank account after interest has accrued.
"""


def compound_interest(principal_amount, interest_rate, times_compounded, num_of_years):
    return principal_amount * (1 + (interest_rate / times_compounded)) ** (times_compounded * num_of_years)


def main():
    """
    Drive the program.

    Tests the function in this module.
    """

    print(compound_interest(500, 0.1, 4, 10))
    print(compound_interest(800, 0.08, 12, 20))
    print(round(compound_interest(800, 0.08, 12, 20), 2))  # optionally round the float to 2 decimal places (for money)


if __name__ == "__main__":
    main()


'''
Get ints and floats representing the principal amount of money in the bank account, the annual interest rate, the
number of times per year the interest is compounded, and the number of years. Return the final amount of money in
the account with interest over time.

    A = P(1 + (r / n))**(n * t)
    A = final amount            P = principal (initial) amount
    r = annual interest rate    n = number of times per year the interest is compounded
    t = number of years

Computational thinking:
   Automation: This is a more complex math problem, so it's faster and easier to have a program do it for us.
   Data representation: Using ints and floats appropriately to represent monetary, time, and other values
'''

"""
Module containing functions for creating a D&D character.
"""
import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate the result of rolling a die with a given number of sides a given number of times.

    Check to make sure the given ints are positive, else return 0 and quit the function.

    We roll each die in succession. Generate a random number between 1 and number_of_sides for each roll.

    :precondition: number_of_rolls and number_of_sides should be positive ints, else 0 will be returned
    :postcondition: an int representing the total score of all dice rolls will be returned
    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :return: a random positive int within the calculated range
    """

    if number_of_rolls < 1 or number_of_sides < 1:  # make sure that ints are positive
        return 0

    total = 0

    for i in range(number_of_rolls):
        total += (random.randint(1, number_of_sides))

    return total


def choose_inventory():  # todo: finish this function + docstring
    """

    :precondition: inventory should not be empty, else a warning will be returned
    :postcondition: function will return a list of length selection containing a random sample from inventory
    :return: a list containing a selection of items from the original inventory list
    """

    print('Welcome to Yolanda\'s Premium Adventure Shop! For all your dungeon-crawling needs.')

    shop_items = {1: 'Sword of Sanctimony', 2: 'Potion of Python', 3: 'Daggers of Deception', 4: 'Staff of Serenity',
                  5: 'Juggling Balls of JavaScript', 6: 'Detonator of Divide-by-Zero', 7: 'Gloves of Genius',
                  8: 'Map of Misdirection', 9: 'Crossbow of Courage', 10: 'Charm of Chris\' Approval',
                  11: 'Cloak of Confusion', 12: 'Takashi\'s Donut Box', 13: 'Bottle of Binary',
                  14: 'Axe of Asking Questions'}

    print('\nToday there are', len(shop_items), 'shop items available. They are:')
    for number, item in shop_items.items():  # print all shop items and their keys
        print(number, '-', item)

    print('\n')

    purchase_list = []

    user_exit = False
    while not user_exit:
        purchase = input('What would you like to buy? (enter an item number or -1 to finish): ')

        if purchase.isdigit() and int(purchase) in shop_items.keys():  # check if input is a positive number
            purchase_list.append(shop_items[int(purchase)])
            print(purchase_list)

        elif purchase == '-1':
            user_exit = True

        else:
            print('That wasn\'t an acceptable input. Please enter a number corresponding to an item or -1 to quit.')


def generate_vowel():
    """
    Randomly select one vowel and return it.

    :return: a string of length 1 containing a vowel
    """
    return random.choice('aeiouy')


def generate_consonant():
    """
    Randomly select one consonant and return it.

    :return: a string of length 1 containing a consonant
    """
    return random.choice('bcdfghjklmnpqrstvwxyz')


def generate_syllable():
    """
    Create a syllable using one consonant and one vowel. Use the generate consonant and vowel functions.

    :return: a string of length 2 containing a consonant and vowel
    """
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Create a name using the specified number of syllables. Use the generate syllable function.

    :precondition: syllables must be a positive int
    :postcondition: function will generate a character name
    :param syllables: a positive int representing the desired number of syllables for the name
    :return: a string of length syllables * 2
    """
    name = ""

    for i in range(syllables):
        name += generate_syllable()

    return name.capitalize()


def selection_helper(selection_category, choices):
    """
    Get a user's choice from a dictionary of items within a certain category.

    Print out all the available choices in a user-friendly way, then prompt the user to choose one. If the user enters
    a number corresponding to a valid choice, print a confirmation and return the choice. Otherwise, print a helpful
    error message. Repeat until the input is valid.

    :param selection_category: the category we are selecting from, e.g. race, as a string
    :param choices: a dict containing all the available choices in the selection_category
    :return: a string corresponding to the user's selection from the choices
    """
    print('Which', selection_category, 'would you like your character to be? There are', len(choices), 'available:')
    for number, item in choices.items():  # print all choices and their keys
        print(number, '-', item)

    user_exit = False
    while not user_exit:  # repeat until input is valid
        selection = input('Please enter the number corresponding to your desired class: ')

        if selection.isdigit() and int(selection) in choices.keys():  # check if input is valid
            print('Your', selection_category, 'is:', choices[int(selection)])
            user_exit = True

        else:
            print('That wasn\'t an acceptable input. Please enter a number corresponding to a class.')

    return choices[int(selection)]


def select_class():
    """
    Prompt the user to choose a class for their character from the available classes.

    :precondition: selection_helper must work as expected
    :postcondition: the function will run until a valid class is chosen, then will return it.
    :return: a string corresponding to the user's selected class
    """
    classes = {1: 'barbarian', 2: 'bard', 3: 'cleric', 4: 'druid', 5: 'fighter', 6: 'monk', 7: 'paladin',
               8: 'ranger', 9: 'rogue', 10: 'sorcerer', 11: 'warlock', 12: 'wizard'}

    return selection_helper('class', classes)


def select_race():
    """
        Prompt the user to choose a race for their character from the available races.

        :precondition: selection_helper must work as expected
        :postcondition: the function will run until a valid race is chosen, then will return it.
        :return: a string corresponding to the user's selected race
        """
    races = {1: 'dragonborn', 2: 'dwarf', 3: 'elf', 4: 'gnome', 5: 'half-elf', 6: 'halfling', 7: 'half-orc',
             8: 'human', 9: 'tiefling'}

    return selection_helper('race', races)


def create_character(name_length):
    """
    Create a D&D character as a list with a name and six statistics.

    :precondition: name_length must be a positive int
    :param name_length: a positive int representing the desired number of syllables in the character name
    :return: a list of length 7 containing a string and 6 nested lists, each containing a string and int
    """
    # begin the dict with the name, race, and class as chosen by the user
    character = {'Name': generate_name(name_length), 'Race': select_race(), 'Class': select_class()}

    # roll for initial HP depending on class
    if character['Class'] in ['bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock']:
        hp = roll_die(1, 8)

    elif character['Class'] in ['fighter', 'paladin', 'ranger']:
        hp = roll_die(1, 10)

    elif character['Class'] in ['sorcerer', 'wizard']:
        hp = roll_die(1, 6)

    else:  # only barbarian rolls d12
        hp = roll_die(1, 12)

    character['HP'] = [hp, hp]

    for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
        character[i] = roll_die(3, 6)  # create each dict pair with the statistic name and value

    character['XP'] = 0  # assign 0 XP to new character

    character['Inventory'] = []  # assign empty inventory to new character

    return character


def print_character(character):  # todo: needs to be modified to accept character dictionary
    print('Your character is named', character[0])  # print name

    for i in range(1, 6):  # print stats
        print('Your', character[i][0], 'is', character[i][1])

    if len(character) == 8 and character[7]:  # print items if they exist
        print('You have these items:')
        for i in character[7]:
            print(i)
    else:
        print('You don\'t have any items right now.')


# todo: combat function (+ attack helper function?)
def combat_round(opponent_one, opponent_two):
    pass


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """
    print(create_character(3))
    #choose_inventory()


if __name__ == "__main__":
    main()

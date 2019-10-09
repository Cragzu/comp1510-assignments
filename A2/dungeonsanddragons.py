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


def choose_inventory(inventory, selection):
    """
    Select an assortment of items from a given list, create a sorted list containing the given number of selected items.

    :precondition: inventory should not be empty, else a warning will be returned
    :precondition: selection should be a positive int between 1 and inventory length, else a warning will be returned
    :postcondition: function will return a list of length selection containing a random sample from inventory
    :param inventory: a list representing all available items to choose from
    :param selection: a positive int less than or equal to the length of inventory representing the desired # of items
    :return: a sorted list containing a selection of items from the original inventory list
    """
    if inventory == [] and selection == 0:
        return []

    elif selection < 0:
        print("The selection cannot be a negative number!")
        return []

    elif selection >= len(inventory):  # selection is equal or longer than inventory
        if selection > len(inventory):  # warning message only when selection is longer
            print("The selection cannot be larger than the available inventory!")
        return sorted(inventory)

    else:
        return sorted(random.sample(inventory, selection))


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


def create_character(name_length):
    """
    Create a D&D character as a list with a name and six statistics.

    :precondition: name_length must be a positive int
    :param name_length: a positive int representing the desired number of syllables in the character name
    :return: a list of length 7 containing a string and 6 nested lists, each containing a string and int
    """

    character = {'Name': generate_name(name_length)}  # begin the dict with the character name

    for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
        character[i] = roll_die(3, 6)  # create each dict pair with the statistic name and value

    character['XP'] = 0  # todo: is there a way to insert items in the middle of dicts?

    character['Inventory'] = []  # assign empty inventory to new character

    # todo: the rest of the create character function

    return character


def print_character(character):
    print('Your character is named', character[0])  # print name

    for i in range(1, 6):  # print stats
        print('Your', character[i][0], 'is', character[i][1])

    if len(character) == 8 and character[7]:  # print items if they exist
        print('You have these items:')
        for i in character[7]:
            print(i)
    else:
        print('You don\'t have any items right now.')

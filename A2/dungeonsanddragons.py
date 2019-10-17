"""
Module containing functions for creating a D&D character.
"""
import random
# todo: doctests if any functions need them?


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


def hit_die(character_class):
    """
    Roll a die with a certain number of sides depending on the class of the character.

    For HP and combat purposes, different classes roll different dice. Call the roll_die function with the appropriate
    number of sides to get a random value within the proper range and return it.

    :precondition: roll_die function must work as expected
    :precondition: character_class must be a string and must contain one of the 12 D&D classes
    :param character_class: a string containing the character's class
    :return: an int representing the rolled value
    """
    if character_class in ['bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock']:
        return roll_die(1, 8)

    elif character_class in ['fighter', 'paladin', 'ranger']:
        return roll_die(1, 10)

    elif character_class in ['sorcerer', 'wizard']:
        return roll_die(1, 6)

    else:  # only barbarian rolls d12
        return roll_die(1, 12)


def choose_inventory():
    """
    Prompt the user to select items to purchase from a predefined dictionary.

    Print all the available items, then run a loop asking the user to select items, exiting when -1 is entered. If
    the user enters invalid input, print a helpful error message before prompting again.

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

    return purchase_list


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
        selection = input('Please enter the number corresponding to your desired ' + selection_category + ':')

        if selection.isdigit() and int(selection) in choices.keys():  # check if input is valid
            print('Your', selection_category, 'is:', choices[int(selection)])
            user_exit = True

        else:
            print('That wasn\'t an acceptable input. Please enter a number corresponding to a',
                  (selection_category + '.'))

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

# todo: unit test
def create_character(name_length):
    """
    Create a D&D character as a dictionary with a name and statistics.

    :precondition: name_length must be a positive int
    :param name_length: a positive int representing the desired number of syllables in the character name
    :return: a dictionary containing the character's name, race, class, HP, stats, XP, and inventory
    """
    # begin the dict with the name, race, and class as chosen by the user
    character = {'Name': generate_name(name_length), 'Race': select_race(), 'Class': select_class()}

    hp = hit_die(character['Class'])  # roll for initial HP depending on class
    character['HP'] = [hp, hp]

    for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:
        character[i] = roll_die(3, 6)  # create each dict pair with the statistic name and value

    character['XP'] = 0  # assign 0 XP to new character

    character['Inventory'] = []  # assign empty inventory to new character

    return character


def print_character(character):
    """
    Display information about a D&D character in a way easily readable by the user.

    :param character: a properly formed dictionary containing character information
    :return: none, uses print statements
    """
    print('Your character is named', character['Name'], '\nYour race is', character['Race'],
          '\nYour class is', character['Class'], '\nYour starting HP is', character['HP'][0])

    for i in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']:  # print stats
        print('Your', i, 'is', character[i])

    print('Your current XP is', character['XP'])

    if character['Inventory']:
        print('You have these items:')
        for i in character['Inventory']:
            print(i)

    else:
        print('You don\'t have any items right now.')

# todo: unit test
def attack(attacker, defender):
    """
    Attempt an attack from one character on another.

    Roll a die and check the result against the defender's dexterity to determine whether the attack misses. If the
    attack hits, roll the attacker's hit die to determine the damage dealt.

    :precondition: hit_die function must work as expected
    :precondition: attacker and defender must be properly formed character dictionaries
    :param attacker: a dictionary containing the attacking character
    :param defender: a dictionary containing the defending character
    :return: the damage dealt to the defender as an int
    """
    dexterity_check = roll_die(1, 20)
    print('The dexterity check was', dexterity_check)
    print('Defender dexterity is', defender['Dexterity'])
    if dexterity_check > defender['Dexterity']:
        damage = hit_die(attacker['Class'])
        print(attacker['Name'], 'dealt', damage, 'damage to', (defender['Name'] + '!'))
        return damage

    else:
        print('The attack missed!')
        return 0

# todo: unit test
def combat_round(opponent_one, opponent_two):
    """
    Simulate a round of combat between two characters.

    Roll a d20 for each character to determine who attacks first. If rolls are equal, continue rolling until one is
    higher. Call the attack function with the attacker and defender and adjust the defender's HP. If the defender
    survives the attack (HP > 0), call the attack function again with the roles reversed for a counterattack.

    :param opponent_one: a dictionary containing a character
    :param opponent_two: a dictionary containing a character
    :return: none, uses print statements
    """

    print('Rolling to determine attack priority...')
    equal_rolls = True
    while equal_rolls:  # determine start player
        opponent_one_roll = roll_die(1, 20)
        print(opponent_one['Name'], 'rolled:', opponent_one_roll)

        opponent_two_roll = roll_die(1, 20)
        print(opponent_two['Name'], 'rolled:', opponent_two_roll)

        if opponent_one_roll > opponent_two_roll:
            print(opponent_one['Name'], 'attacks first!')
            equal_rolls = False
            opponent_two['HP'][1] -= attack(opponent_one, opponent_two)
            if opponent_two['HP'][1] > 0:
                opponent_one['HP'][1] -= attack(opponent_two, opponent_one)
            else:
                print(opponent_two['Name'], 'was defeated!')

        elif opponent_two_roll > opponent_one_roll:
            print(opponent_two['Name'], 'attacks first!')
            equal_rolls = False
            opponent_one['HP'][1] -= attack(opponent_two, opponent_one)
            if opponent_one['HP'][1] > 0:
                opponent_two['HP'][1] -= attack(opponent_one, opponent_two)
            else:
                print(opponent_one['Name'], 'was defeated!')

        else:
            print('A tie! Rolling again...')


def main():
    """
    Drive the program.

    Showcases the functions created in this module.
    """
    print('~~~ Welcome to the D&D Simulator! ~~~')
    print('\nPlayer 1, create your character:')
    player_one = create_character(int(input('How many syllables should your character\'s name have?: ')))

    print('\nSelect', (player_one['Name'] + '\'s inventory:'))
    player_one['Inventory'] = choose_inventory()

    print('\nHere\'s your character!')
    print_character(player_one)

    print('\nPlayer 2, create your character:')
    player_two = create_character(int(input('How many syllables should your character\'s name have?: ')))

    print('\nSelect', (player_two['Name'] + '\'s inventory:'))
    player_two['Inventory'] = choose_inventory()

    print('\nHere\'s your character!')
    print_character(player_two)

    print('\nIt\'s time for', player_one['Name'], 'and', player_two['Name'], 'to battle!')
    combat_round(player_one, player_two)


if __name__ == "__main__":
    main()

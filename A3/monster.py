"""
Module containing monster functions for SUD.
"""
import random
from sud import input_loop

# todo: should contain monster health

MONSTER_TYPES = ['dragon', 'goblin', 'ghost', 'slime', 'vampire', 'gelatinous cube', 'slaad', 'zombie', 'banshee']
MONSTER_DESCRIPTIONS = ['horrible', 'dark', 'terrifying', 'deadly', 'pale', 'wicked', 'flying', 'sinister']


def generate_monster(types, descriptions):
    """
    Generate a random monster and store its data.

    :param types: a list containing available types of monsters to pick from
    :param descriptions: a list containing monster adjectives  to pick from
    :postcondition: returned dict will contain name, description, HP, and hit_die keys
    :return: a dictionary containing monster data
    """
    monster = {'name': random.choice(types), 'description': random.choice(descriptions),
               'HP': 5, 'hit_die': 6}
    return monster


def monster_encounter(monster):
    """
    Simulate an encounter with a monster.

    Present the monster to the player, and offer the choice of fighting or running away.

    :param monster: a dictionary containing monster data
    :precondition: monster dict must be properly formed as per generate_monster postcondition
    :return: a string ('F'/'R') representing whether the player wants to fight or run away
    """
    print('You encountered a', monster['description'], (monster['name'] + '!'))

    return input_loop('Do you want to (F)ight or (R)un away?: ', ['F', 'R'])


def main():
    """
    Drive the SUD program.
    """

    monster_encounter(generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS))


if __name__ == "__main__":
    main()

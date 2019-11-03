"""
Module containing monster functions for SUD.
"""
import random
from sud import input_loop


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

    fight_decision = input_loop('Do you want to (F)ight or (R)un away?: ', ['F', 'R'])

    if fight_decision == 'R':
        backstab()

    # todo: code for fights


def backstab():  # todo: docstring. returns the amount of damage taken from the backstab, 0 if it didn't happen
    """
    Attempt a backstab on the player.

    Calculate whether or not the backstab was successful based on a 10% chance. If it was, apply a random amount of
    damage between 1 and 4. If not, the player takes no damage.

    :postcondition: function will return an int between 0 and 4
    :return: an int representing the damage done by the backstab
    """
    stab_chance = random.randint(1, 10)

    if stab_chance == 1:  # 10% chance of backstabbing
        print('The monster stabbed you in the back!')
        damage = random.randint(1, 4)
        print('You took', damage, 'damage before escaping.')
        return damage

    else:
        print('You got away safely!')
        return 0


def main():
    """
    Drive the SUD program.
    """

    monster_encounter(generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS))


if __name__ == "__main__":
    main()

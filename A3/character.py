"""
Module containing functions that manage the character/user in the SUD.
"""
from monster import generate_monster, MONSTER_TYPES, MONSTER_DESCRIPTIONS

# todo: should contain character description, health, healing


def modify_hp(entity, value):
    """
    Update the HP value of an entity.

    Add the value to the current HP of the entity, capping it at its max HP and at 0.

    :param entity: a dictionary containing a player or monster
    :param value: an int representing the value to change the HP by, can be positive or negative
    :precondition: entity must be a properly formed dictionary
    :return: none, modifies the given entity and prints information
    """
    hp_before = entity['HP']

    entity['HP'] += value  # will subtract if value is negative

    if entity['HP'] <= 0:  # entity is dead
        entity['HP'] = 0

    if entity['HP'] > entity['max_HP']:  # full health
        entity['HP'] = entity['max_HP']

    print((entity['name'].title() + '\'s'), 'HP modified from', hp_before, 'to', entity['HP'])


def main():
    """
    Drive the SUD program.
    """

    monster = generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS)
    print(monster)

    modify_hp(monster, -3)
    modify_hp(monster, 2)

    print(monster)


if __name__ == "__main__":
    main()

"""
Module containing monster functions for SUD.
"""
import random
from constants import PLAYER, MONSTER_TYPES, MONSTER_DESCRIPTIONS
from character import input_loop


def generate_monster(types, descriptions):
    """
    Generate a random monster and store its data.

    :param types: a list containing available types of monsters to pick from
    :param descriptions: a list containing monster adjectives  to pick from
    :postcondition: returned dict will contain name, description, HP, and hit_die keys
    :return: a dictionary containing monster data
    """
    monster = {'name': random.choice(types), 'description': random.choice(descriptions),
               'HP': 5, 'max_HP': 5, 'hit_die': 6}
    return monster


def populate_dungeon(dungeon):
    """
    Populate the rooms in the dungeon with monsters.

    :param dungeon: a list containing dungeon rooms
    precondition: dungeon is a properly formed matrix; a list containing 5 lists with 5 dicts representing 25 rooms
    :return: none, modifies the given dungeon
    """
    for row in dungeon:
        for room in row:
            room['monster'] = generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS)


def monster_encounter(monster):
    """
    Simulate an encounter with a monster.

    Present the monster to the player, and offer the choice of fighting or running away.

    :param monster: a dictionary containing monster data
    :precondition: monster dict must be properly formed as per generate_monster postcondition
    :return: a string ('F'/'R') representing whether the player wants to fight or run away
    """
    encounter_chance = random.randint(1, 4)

    if encounter_chance == 1:  # 25% chance of encountering a monster
        print('\nYou encountered a', monster['description'], (monster['name'] + '!'))

        fight_decision = input_loop('Do you want to (F)ight or (R)un away?: ', ['F', 'R'])

        if fight_decision == 'R':
            backstab()

        else:  # fight
            battle(PLAYER, monster)

    else:
        print('\nThere doesn\'t seem to be any monsters here right now.')


def backstab():
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


def attack(attacker, defender):
    """
    Attempt an attack from one entity on another.

    Check whether the attack misses (10%)

    :precondition: attacker and defender must be properly formed character dictionaries
    :param attacker: a dictionary containing the attacking character
    :param defender: a dictionary containing the defending character
    :return: the damage dealt to the defender as an int
    """
    miss_chance = random.randint(1, 10)

    if miss_chance == 1:  # 10% chance to miss
        print('The attack from', attacker['name'].title(), 'missed!')
        return 0

    else:
        damage = random.randint(1, (attacker['hit_die']))
        print(attacker['name'].title(), 'dealt', damage, 'damage to', (defender['name'].title() + '!'))
        return -damage


def battle(character, monster):  # a battle to the death, call combat_round alternating until someone dies
    """
    Simulate a battle between the player and a monster.

    Randomly determine attack priority.

    Call the attack function with the attacker and defender and adjust the defender's HP.
    Continue with the roles reversed until someone dies.

    :return:
    """
    combatants = [character, monster]  # index 0 is attacker, 1 is defender
    random.shuffle(combatants)

    continue_battle = True
    while continue_battle:
        modify_hp(combatants[1], attack(combatants[0], combatants[1]))
        print('\n')

        temp = combatants[0]
        combatants[0] = combatants[1]
        combatants[1] = temp

        if combatants[0]['HP'] == 0 or combatants[1]['HP'] == 0:
            continue_battle = False




def main():
    """
    Drive the SUD program.
    """

    battle(PLAYER, generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS))

    # my_monster = generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS)
    #
    # damage = (attack(my_monster, PLAYER))
    # modify_hp(my_monster, -5)


if __name__ == "__main__":
    main()

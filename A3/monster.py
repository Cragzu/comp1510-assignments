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
               'HP': 5, 'max_HP': 5, 'hit_die': 6}
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


def attack(attacker, defender):
    """
    Attempt an attack from one entity on another.

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


def combat_round(player, monster):
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
    Drive the SUD program.
    """

    monster_encounter(generate_monster(MONSTER_TYPES, MONSTER_DESCRIPTIONS))


if __name__ == "__main__":
    main()

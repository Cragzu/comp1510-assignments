"""
Module containing monster functions for SUD.
"""
import random

# todo: should contain monster health

MONSTER_TYPES = ['dragon', 'goblin', 'ghost', 'slime', 'vampire', 'gelatinous cube', 'slaad', 'zombie', 'banshee']

MONSTER_DESCRIPTIONS = ['horrible', 'dark', 'terrifying', 'deadly', 'pale', 'wicked', 'flying', 'sinister']


def generate_monster():
    monster = {'name': random.choice(MONSTER_TYPES), 'description': random.choice(MONSTER_DESCRIPTIONS),
               'HP': 5, 'hit_die': 6}
    return monster

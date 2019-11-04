"""
File containing all constants in the SUD.

Room descriptions credit: Matthew Sernett, wizards.com
"""

# monster info to pull from
MONSTER_TYPES = ['dragon', 'goblin', 'ghost', 'slime', 'vampire', 'gelatinous cube', 'slaad', 'zombie', 'banshee']
MONSTER_DESCRIPTIONS = ['horrible', 'dark', 'terrifying', 'deadly', 'pale', 'wicked', 'flying', 'sinister']

# a matrix, a list containing lists containing dicts with room info
GAME_BOARD = [
    # first row - [0][0] through [0][4]
    [{"description": "A large forge squats against the far wall of this room, and coals glow dimly inside. "
                     "Before the forge stands a wide block of iron with a heavy-looking hammer lying atop it, no doubt "
                     "for use in pounding out shapes in hot metal. Other forge tools hang in racks nearby, and a "
                     "barrel of water and bellows rest on the floor nearby."},
     {"description": "This small room contains several pieces of well-polished wood furniture. Eight ornate, "
                     "high-backed chairs surround a long oval table, and a side table stands next to the far exit. All "
                     "bear delicate carvings of various shapes. One bears carvings of skulls and bones, another is "
                     "carved with shields and magic circles, and a third is carved with shapes like "
                     "flames and lightning strokes."},
     {"description": "This otherwise bare room has one distinguishing feature. The stone around one of the other doors "
                     "has been pulled over its edges, as though the rock were as soft as clay and could be moved with "
                     "fingers. The stone of the door and wall seems hastily molded together."},
     {"description": "This chamber served as an armory for some group of creatures. Armor and weapon racks line the "
                     "walls and rusty and broken weapons litter the floor. It hasn't been used in a long time, and "
                     "all the useful weapons have been taken but for a single sword. Unlike the other weapons in the "
                     "room, this one gleams untarnished in the light."},
     {"description": "Huge rusted metal blades jut out of cracks in the walls, and rusting spikes project down from "
                     "the ceiling almost to the floor. This room may have once been trapped heavily, but someone "
                     "triggered them, apparently without getting killed. The traps were never reset and now "
                     "seem rusted in place."}],

    # second row - [1][0] through [1][4]
    [{"description": "The strong, sour-sweet scent of vinegar assaults your nose as you enter this room. Sundered casks"
                     " and broken bottle glass line the walls of this room. Clearly this was someone's wine cellar for "
                     "a time. The shards of glass are somewhat dusty, and the spilled wine is nothing more than a "
                     "sticky residue in some places. Only one small barrel remains unbroken amid the rubbish."},
     {"description": "Several white marble busts that rest on white pillars dominate this room. Most appear to be male "
                     "or female humans of middle age, but one clearly bears small horns projecting from its forehead "
                     "and another is spread across the floor in a thousand pieces, leaving one pillar empty."},
     {"description": "A crack in the ceiling above the middle of the north wall allows a trickle of water to flow down "
                     "to the floor. The water pools near the base of the wall, and a rivulet runs along the wall an "
                     "out into the hall. The water smells fresh."},
     {"description": "Thick cobwebs fill the corners of the room, and wisps of webbing hang from the ceiling and waver "
                     "in a wind you can barely feel. One corner of the ceiling has a particularly large clot of "
                     "webbing within which a goblin's bones are tangled."},
     {"description": "A liquid-filled pit extends to every wall of this chamber. The liquid lies about 10 feet below "
                     "your feet and is so murky that you can't see its bottom. The room smells sour. A rope bridge "
                     "extends from your door to the room's other exit."}],

    # third row - [2][0] through [2][4]
    [{"description": "Fire crackles and pops in a small cooking fire set in the center of the room. The smoke from a "
                     "burning rat on a spit curls up through a hole in the ceiling. Around the fire lie several fur "
                     "blankets and a bag. It looks like someone camped here until not long ago, "
                     "but then left in a hurry."},
     {"description": "A flurry of bats suddenly flaps through the doorway, their screeching barely audible as they "
                     "careen past your heads. They flap past you into the rooms and halls beyond. The room "
                     "from which they came seems barren at first glance."},
     {"description": "Rusting spikes line the walls and ceiling of this chamber. The dusty floor shows no sign that "
                     "the walls move over it, but you can see the skeleton of some humanoid impaled on some "
                     "wall spikes nearby."},
     {"description": "You gaze into the room and hundreds of skulls gaze coldly back at you. They're set in niches "
                     "in the walls in a checkerboard pattern, each skull bearing a half-melted candle on its head. "
                     "The grinning bones stare vacantly into the room, which otherwise seems empty."},
     {"description": "Unlike the flagstone common throughout the dungeon, this room is walled and floored with black "
                     "marble veined with white. The ceiling is similarly marbled, but the thick pillars "
                     "that hold it up are white. A brown stain drips down one side of a nearby pillar."}],

    # fourth row - [3][0] through [3][4]
    [{"description": "This room is hung with hundreds of dusty tapestries. All show signs of wear: moth holes, "
                     "scorch marks, dark stains, and the damage of years of neglect. They hang on all the walls and "
                     "hang from the ceiling to brush against the floor, blocking your view of the rest of the room."},
     {"description": "Three low, oblong piles of rubble lie near the center of this small room. Each has a weapon "
                     "jutting upright from one end -- a longsword, a spear, and a quarterstaff. "
                     "The piles resemble cairns used to bury dead adventurers."},
     {"description": "Huge rusted metal blades jut out of cracks in the walls, and rusting spikes project down from "
                     "the ceiling almost to the floor. This room may have once been trapped heavily, but someone "
                     "triggered them, apparently without getting killed. "
                     "The traps were never reset and now seem rusted in place."},
     {"description": "Many doors fill the room ahead. Doors of varied shape, size, and design are set in every wall "
                     "and even the ceiling and floor. Barely a hand's width lies between one door and the next. "
                     "All the doors but the one you entered by are shut, and many have obvious locks."},
     {"description": "A strange ceiling is the focal point of the room before you. It's honeycombed with hundreds of "
                     "holes about as wide as your head. They seem to penetrate the ceiling to some height beyond a "
                     "couple feet, but you can't be sure from your vantage point."}],

    # fifth row - [4][0] through [4][4]
    [{"description": "This chamber was clearly smaller at one time, but something knocked down the wall that separated "
                     "it from an adjacent room. Looking into that space, you see signs of another wall knocked over. "
                     "It doesn't appear that anyone made an effort to clean up the rubble, but some paths through "
                     "see more usage than others."},
     {"description": "You pull open the door and hear the scrape of its opening echo throughout what must be a massive "
                     "room. Peering inside, you see a vast cavern. Stalactites drip down from the ceiling in sharp "
                     "points while flowstone makes strange shapes on the floor."},
     {"description": "Many small desks with high-backed chairs stand in three long rows in this room. Each desk has "
                     "an inkwell, book stand, and a partially melted candle in a rusting tin candleholder. "
                     "Everything is covered with dust."},
     {"description": "You open the door and before you is a dragon's hoard of treasure. Coins cover every inch of "
                     "the room, and jeweled objects of precious metal jut up from the money like glittering islands "
                     "in a sea of gold."},  # treasure room
     {"description": "In the center of this large room lies a 30-foot-wide round pit, its edges lined with rusting "
                     "iron spikes. About 5 feet away from the pit's edge stand several stone semicircular benches. "
                     "The scent of sweat and blood lingers, which makes the pit's resemblance to a "
                     "fighting pit or gladiatorial arena even stronger."}
     ]
]
VICTORY_ROOM = [4, 3]

# character description
PLAYER = {'name': 'Alberto the Mighty', 'description': 'An intrepid traveller seeking the riches of this dungeon.',
          'goal': 'To find the treasure hidden within this maze of twisty tunnels',
          'HP': 10, 'max_HP': 10, 'hit_die': 6}

# display
DIVIDING_LINE = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'

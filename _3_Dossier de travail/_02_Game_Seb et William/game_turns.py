#-*- coding: utf-8 -*-
"""
Dictionnaires de tests basés sur le fichier "Short example.ano"
"""
size = (6, 6)

entities = {(2, 1): [1, "alpha", 60], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, "deers", 100]}

"""
Index
------
- Generic Tools
    - entity_at #PLUS NECESSAIRE A PRIORI
    - range
    - energy
- Game Functions
    - pacify
    - bonus
    - feed
    - attack
    - being_human
    - move
-------------------------
-------------------------
Glossary
--------
ww = werewolf = loup-garou
E = energy
******************************
"""

"""
========================================
            GENERIC TOOLS
=======================================
"""
def entity_at(entity_coords): # VALIDE
    """
    Description of the function
	---------------------------
    Check if there entity(ies) at given position

    Uses:
    -----
    1) To populate the map
    2) To permit or not the feed
    3) To permit or not the attack
    4) To permit or not a move

    Args:
    -----
    entity_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
    (bool, string, string, int) : list that contain true or false, dict_name, type, energy - list

   	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
    """
    # Validée
    for key, values in foods.items():
        if key == entity_coords:
            return ["foods", values[0], values[1], ]
    for key, values in teams.items():
        if key == entity_coords:
            return [values[0], values[1], values[2], ]
    return False

def range(ray, ww_coords):
    """
   	Description of the function
	---------------------------
    Check and count number of entity in range

    Uses:
    -----
    -

    Args:
    -----
    ray : range around the entity (int)
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
    list - entities in range

   	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
    """
    flag = 0
    nbr_entity = 0
    nbr_ally = 0
    nbr_enemy = 0
    for i in team1:
        #Rajouter un test pour voir si c'est un food
        x = abs(i[0]-entity[0])
        y = abs(i[1]-entity[1])
        if x == 0 and y == 0:
            flag += 1
        elif (x <= rayon) and (y <= rayon):
            nbr_entity += 1
    if flag == 1:
        nbr_ally = nbr_entity
    else:
        nbr_enemy = nbr_entity
    flag = 0
    nbr_entity = 0
    for j in team2:
        x = abs(j[0]-entity[0])
        y = abs(j[1]-entity[1])
        if x == 0 and y == 0:
            flag += 1
        elif (x <= rayon) and (y <= rayon):
            nbr_entity += 1
    if flag == 1:
        nbr_ally = nbr_entity
    else:
        nbr_enemy = nbr_entity


    #print("nbr ally : "+str(nbr_ally)+"")
    #print("nbr ennemy : "+str(nbr_enemy)+"")

def energy(ww_coords):
	"""
	Description of the function
	---------------------------
    Return the energy of the werewolf at given position

    Uses:
    -----
    - For Omega to launch pacify
    - After an attack
        => If Alpha E == 0 ==> Game finished
        => If E of a ww ==0 ==> being-human

    Args:
    -----
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	int : energy of the werewolf

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

"""
==========================================================
                    GAMERULES CYCLE
========================================================
    """
def pacify(ww_coords):
    """
	Description of the function
	---------------------------
    Launch "Pacify" on all around, and in range werewolfs
    Update Omega energy

    Uses:
    -----
    Only used by Omegas
    ** Reminder
    * For each ww at range <= 6
    * Cost : 40 E

    Args:
    -----
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	list : list of pacified wolf for this turn.

	Version:
	--------
	specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

def bonus(ww_coords):
    """
	Description of the function
	---------------------------
    Check allied ww in range, calculate and give bonuse.

    Uses:
    -----
    Each turn, for each player, for each werewolf
    ** Reminder
    * Bonus only for attack.
    * E = E + (10*ww_number(in range <=2) + (30 if alpha range <= 4)

    Args:
    -----
    w_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	type : Description

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

def feed(list): # VALIDE
    """
	Description of the function
	---------------------------
    Update ww energy if food in range and update food energy

    Args:
    -----
    list : list that contains ww_coords and entity_coords - type (list)

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 03/03/2022)
	code : Sébastien Baudoux (v.1.0 - 03/03/2022)
	"""
    is_ww = entities[list[0]]
    is_food = entities[list[1]]
    if is_food and is_food[0] == 0:
        if is_ww and is_ww[0] == 1:
            if is_ww[2] < 100:
                food_E = is_food[2]
                ww_E = is_ww[2]
                toteaten = 0
                while (food_E > 0) and (ww_E < 100):
                    food_E -= 1
                    ww_E += 1
                    toteaten += 1
                if food_E == 0:
                    print("The "+is_food[1]+" have been completely eaten.")
                    entities.pop(list[1])
                else:
                    is_food[2] = food_E
                is_ww[2] = ww_E
                entities.update({list[1]: is_food})
                entities.update({list[0]: is_ww})
                print("The werewolf at "+str(list[0])+" has eat "+str(
                    toteaten)+" energy from "+str(entities[list[1]][1])+" at "+str(list[1])+".")
            else:
                print("Your werewolf energy is already at max.")
    else:
        print("This is not food.")


def fight(listat):
	"""
	Description of the function
	---------------------------
    Make damage to ww2 from ww1
    ** Reminder
    * Strenght = E/10 (rounded nearest)

    Args:
    -----
    list : list that contains attacker coordinates and defender coordinates - type (list)

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 03/03/2022)
	code : Sébastien Baudoux (v.1.0 - 03/03/2022)
    """
    attacker = entities[listat[0]]
    defender = entities[listat[1]]
    attack_strength = (attacker[2]/10)
    defender[2] = defender[2] - attack_strength
    print(""+str(defender[1]+" loose "+str(attack_strength)+", his energy is now : "+str(defender[2]))+"")
    entities.update({listat[1]: defender})


def being_human(ww_coords):
    """
    Description of the function:
    ----------------------------
    Check the energy of a werewolf and turn it into human if == 0
    For reminder : Humans can only feed

    Uses:
    -----
    Function use after attack phase.

    Args:
    -----
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

def move(listmov):
    """
    Description of the function:
    ----------------------------
    Move a werewolf

    Parameters
    ----------
    start_coord : Origin coordinates - (x, y) - type (list)
    dest_coord : Destination coordinates - (x, y) - type (list)

    Returns
    -------
    Nothing or just a log message.

    Raises
    ------
    IOError: if there is no werewolf at origin coordinates
    IOError: if the destinations coordinates are further than 1
    IOError: if the destinations coordinates are occupied by an entity
    IOError: if the destination is outside the boardgame

    Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	Code : Sébastien Baudoux (v.1.0 - 03/03/2022)
    """
    #Check if destination is not out of the boardgame.
    if listmov[1][0] <= size[0] and listmov[1][1] <= size[1]:
        #Check is the destination is empty
        if not (listmov[1] in entities):
            x = int(abs(listmov[1][0]-listmov[0][0]))
            y = int(abs(listmov[1][1]-listmov[0][1]))
            if x == 1 and y == 1:
                print("Move possible")
            else:
                print("Move out of range")
        else:
            print("Can't move there, this space is not empty.")
    else:
        print("Can't move out of boardgame.")
#-*- coding: utf-8 -*-
"""
Ce fichier regroupe toutes les fonctions realtives aux actions du jeu ainsi que la gestion des ordres des 2 joueurs.

Dictionnaires de tests basés sur le fichier "Short example.ano"
"""
size = (6, 6)

entities = {(2, 1): [1, "alpha", 57], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, "deers", 100]}

"""
TEST ordres complets pour P1 et P2
orders_P1 = "  10-10:@10-11   12-10:*12-11 19-20:*20-20  2-1:<2-4  12-72:<27-48 17-20:pacify"
orders_P2 = "7-10:<8-11 22-10:@12-11 19-20:*14-15 45-99:pacify"
"""
# Test ordre light pour P1
orders_P1 = "1-1:<2-2 3-1:<2-3"
orders_P2 = ""
"""
Index
------
- Generic Tools
    - in_range
    - hacher
    - order_manager
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
game_turn = 0
print("Game turn : "+str(game_turn)+"")
"""
========================================
            GENERIC TOOLS
=======================================
"""
def entity_at(entity_coords): # VALIDE -- A SUPPRIMER NORMALEMENT
    """
    Description of the function
	---------------------------
    Check if there entity(ies) in entities dictionnary

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
    (int, string, int) : list that contain team of entity, name of entity, energy - list

   	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 09/03/2022)
	Code : Sébastien Baudoux (v.2.0 - 09/03/2022)
    """
    # Validée
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2]]
    return False

def in_range(range, omega_coord):# VALIDE
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
    nbr_entity = 0
    ww_in_range = {}
    key = []
    for key, values in entities.items():
        #Test if entity is a werewolf
        if values[0] == 1 or values[0] == 2:
            x = abs(key[0]-omega_coord[0])
            y = abs(key[1]-omega_coord[1])
            if x == 0 and y == 0:
                ...  # current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key: values})
    return ww_in_range

def hacher(string): #Refaire la spec
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
    ordre = string
    #print(ordre)
    #Split gauche droite
    gd = ordre.split(":")
    #Split origine X et origine Y
    c = gd[0].split("-")
    #Création de la liste avec les coordonnées d'origine X, Y
    origine = (int(c[0]), int(c[1]))
    #Test si l'ordre est pacify
    if gd[1] == "pacify":
        order_type = gd[1]
        hach_order = origine
    else:
        #Sinon débute le split des coordonnées de destination
        e = gd[1].split("-")
        z = e[0][1:]
        order_type = e[0][0]
        destination = (int(z), int(e[1]))
        hach_order = [order_type, origine, destination]
    return hach_order
"""
==========================================================
                    GAMERULES CYCLE
========================================================
    """
def pacify(rayon, omega, pacified_werewolves):# VALIDE
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
    if entities[omega][1] == "omega":
        if entities[omega][2] < 40:
            print("Omega don't have enough energy to pacify")
        #For each ww at range <= 6
        else:
            for key in in_range(rayon, omega):
                pacified_werewolves.append(key)
            print("These werewolves has been pacified for this turn " +
                  str(pacified_werewolves)+"")
    else:
        print("Not omega")
    return pacified_werewolves

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
    if entity_at[entities[list[0]]]:
        is_ww = entities[list[0]]
    if entity_at[entities[list[1]]]:
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

def fight(listat, pacified_werewolves):  # VALIDE
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
    #verifier si attaquant est dans pacified_werewolves
    if listat[0] in pacified_werewolves:
        print("This werewolf "+str(listat[0])+" has been pacified this turn.")
    else:
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

def move(listmov): # VALIDE
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


"""
========================================
            ORDER MANAGER
=======================================
"""
def orders_manager(orders_P1, orders_P2, game_turn):
    """
	Description of the function
	---------------------------
    The order manager rules every game stages.
    His job is to clean and sort players orders and dispatch them to related functions.
    The order manager make a complete turn.

    Args:
    -----
    orders_P1 : string that contains ordres from player 1 - type (string)
    orders_P2 : string that contains ordres from player 2 - type (string)

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 03/03/2022)
	code : Sébastien Baudoux (v.1.0 - 03/03/2022)
	"""
    # Convert Player 1 orders in a list
    cleanP1 = orders_P1.split()
    # Convert Player 2 orders in a list
    cleanP2 = orders_P2.split()
    # Initialize lists of differents orders for each players.
    pacify_P1 = []
    pacify_P2 = []
    feeds_orders_P1 = []
    feeds_orders_P2 = []
    attacks_orders_P1 = []
    attacks_orders_P2 = []
    move_orders_P1 = []
    move_orders_P2 = []

    # Populate lists orders for player 1
    i = 0
    while i < len(cleanP1):
        current_order = cleanP1[i]
        listcurord = hacher(current_order)
        # Il faut rajouter pour chaque ordre un check afin de s'assurer que le ww est bien de la bonne équipe
        # if entity_at(listcurord[1])[0] == 1
        if listcurord[0] == "<":
            feeds_orders_P1.append(listcurord)
        elif listcurord[0] == "*":
            attacks_orders_P1.append(listcurord)
        elif listcurord[0] == "@":
            move_orders_P1.append(listcurord)
        else:
            pacify_P1.append(listcurord)
        i += 1
    # Populate lists orders for player 2
    i = 0
    while i < len(cleanP2):
        current_order = cleanP2[i]
        listcurord = hacher(current_order)
        if listcurord[0] == "<":
            feeds_orders_P2.append(listcurord)
        elif listcurord[0] == "*":
            attacks_orders_P2.append(listcurord)
        elif listcurord[0] == "@":
            move_orders_P2.append(listcurord)
        else:
            pacify_P2.append(listcurord)
        i += 1

    # --------------------
    # --- PACIFY PHASE ---
    # --------------------

    pacified_werewolves = []

    # Check if Player 1 given pacify order and run it.
    if len(pacify_P1) > 0:
        print("Player 1 pacify phase.")
        while len(pacify_P1) > 0:
            # Rajouter les arguments rayon et pacified_werewolfs
            pacify(3, pacify_P1[0], pacified_werewolves)
            pacify_P1.pop(0)
    # Check if Player 2 given pacify order and run it.
    if len(pacify_P2) > 0:
        print("Player 2 pacify phase.")
        while len(pacify_P2) > 0:
            # Rajouter les arguments rayon et pacified_werewolfs
            pacify(3, pacify_P2[0], pacified_werewolves)
            pacify_P2.pop(0)

    # ---------------------
    # --- BONUSES PHASE ---
    # ---------------------
    # --- bonuses(P1) ---
    #Make a team_P1 dictionnary that contains all alive werewolfs from player 1
    team1 = {}
    for key, values in entities.items():
        if values[0] == 1:
            team1.update({key: values})
    if len(team1) > 0:
        print("Player 1 bonus phase.")
        for keys in team1:
            # Send to bonus function each werewolf from team 1 dictionnary
            coords = [keys]
            bonus(coords)
    # --- bonuses(P2) ---
    #Make a team_P2 dictionnary that contains all alive werewolfs from player 2
    team2 = {}
    for key, values in entities.items():
        if values[0] == 1:
            #ajouter au dictionnaire team2
            team2.update({key: values})
    if len(team2) > 0:
        print("Player 2 bonus phase.")
        for keys in team2:
            # Send to bonus function each werewolf from team 21 dictionnary
            coords = [keys]
            bonus(coords)

    # ------------------
    # --- FEED PHASE ---
    # ------------------
    # Check if Player 1 given feeds orders and run them.
    if len(feeds_orders_P1) > 0:
        print("Player 1 feed phase.")
        while len(feeds_orders_P1) > 0:
            print(feeds_orders_P1)
            feed(feeds_orders_P1[0][1:3])
            
            feeds_orders_P1.pop(0)
    # Check if Player 2 given feeds orders and run them.
    if len(feeds_orders_P2) > 0:
        print("Player 2 feed phase.")
        while len(feeds_orders_P2) > 0:
            feed(feeds_orders_P2[0][1:3])
            feeds_orders_P2.pop(0)

    # --------------------
    # --- ATTACK PHASE ---
    # --------------------
    # Check if Player 1 given attacks orders and run them.
    if len(attacks_orders_P1) > 0:
        print("Player 1 attack phase.")
        while len(attacks_orders_P1) > 0:
            fight(attacks_orders_P1[0][1:3], pacified_werewolves)
            attacks_orders_P1.pop(0)
    # Check if Player 2 given attacks orders and run them.
    if len(attacks_orders_P2) > 0:
        print("Player 2 attack phase.")
        while len(attacks_orders_P2) > 0:
            fight(attacks_orders_P2[0][1:3], pacified_werewolves)
            attacks_orders_P2.pop(0)

    # ------------------
    # --- MOVE PHASE ---
    # ------------------
    # Check if Player 1 given move orders and run them.
    if len(move_orders_P1) > 0:
        print("Player 1 move phase.")
        while len(move_orders_P1) > 0:
            move(move_orders_P1[0][1:3])
            move_orders_P1.pop(0)
    # Check if Player 2 given move orders and run them.
    if len(move_orders_P2) > 0:
        print("Player 2 move phase.")
        while len(move_orders_P2) > 0:
            move(move_orders_P2[0][1:3])
            move_orders_P2.pop(0)

    game_turn += 1
    return game_turn


print("Game turn : "+str(orders_manager(orders_P1, orders_P2, game_turn))+"")

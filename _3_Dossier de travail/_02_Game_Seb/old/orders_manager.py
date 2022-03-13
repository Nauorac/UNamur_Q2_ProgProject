#-*- coding: utf-8 -*-


"""
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
# Test ordre light pour pacify P1
orders_P1 = "1-1:pacify 2-2:*6-5"
orders_P2 = ""

def in_range(range, omega_coord):
    nbr_entity = 0
    ww_in_range = {}
    key = []
    for key, values in entities.items():
        #Test if entity is a werewolf
        if values[0] == 1 or values[0] == 2:
            x = abs(key[0]-omega_coord[0])
            y = abs(key[1]-omega_coord[1])
            if x == 0 and y == 0:
                ... #current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key:values})
    return ww_in_range

in_range(2,(1,1))

#fct test pacify
def pacify(rayon, omega, pacified_werewolves):
    if entities[omega][1] == "omega":
        if entities[omega][2] < 40:
            print("Omega don't have enough energy to pacify")
        #For each ww at range <= 6
        else:
            for key in in_range(rayon,omega):
                pacified_werewolves.append(key)
            print("These werewolves has been pacified for this turn "+str(pacified_werewolves)+"")
    else:
        print("Not omega")
    return pacified_werewolves


def fight(listat, pacified_werewolves):  # VALIDE
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

#fct test bonus
def bonus(list):
    print(list)

def hacher(string):
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

game_turn = 0
print("Game turn : "+str(game_turn)+"")
"""
==========================================================
                    ORDERS MANAGER
========================================================
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
            team1.update({key:values})
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




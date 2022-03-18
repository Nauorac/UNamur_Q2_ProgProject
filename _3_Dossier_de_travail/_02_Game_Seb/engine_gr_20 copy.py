#-*- coding: utf-8 -*-
import math, random

size = (20, 20)
entities = {(2, 2): [1, 'alpha', 100, 0], (1, 1): [1, 'omega', 100, 0], (1, 2): [1, 'normal', 100, 0], (2, 1): [1, 'normal', 100, 0], (1, 3): [1, 
'normal', 100, 0], (2, 3): [1, 'normal', 100, 0], (3, 3): [1, 'normal', 100, 0], (3, 2): [1, 'normal', 100, 0], (3, 1): [1, 'normal', 100, 0], 
            (19, 19): [2, 'alpha', 100, 0], (20, 20): [2, 'omega', 100, 0], (20, 19): [2, 'normal', 100, 0], (19, 20): [2, 'normal', 100, 0], (20, 18): [2, 'normal', 100, 0], (19, 18): [2, 'normal', 100, 0], (18, 18): [2, 'normal', 100, 0], (18, 19): [2, 'normal', 100, 0], (18, 20): [2, 'normal', 100, 0], 
(4, 4): [0, 'berries', 10, 0], (4, 5): [0, 'berries', 10, 0], (5, 4): [0, 'berries', 10, 0], (5, 5): [0, 'berries', 10, 0], (16, 16): [0, 'berries', 10, 0], (16, 17): [0, 'berries', 10, 0], (17, 16): [0, 'berries', 10, 0], (17, 17): [0, 'berries', 10, 0], (1, 4): [0, 'apples', 30, 0], (1, 5): [0, 'apples', 30, 0], (20, 16): [0, 'apples', 30, 0], (20, 17): [0, 'apples', 30, 0], (4, 1): [0, 'mice', 50, 0], (5, 1): [0, 'mice', 50, 0], (16, 20): [0, 'mice', 50, 0], (17, 20): [0, 'mice', 50, 0], (5, 7): [0, 'rabbits', 100, 0], (7, 5): [0, 'deers', 500, 0], (16, 14): [0, 'rabbits', 100, 0], (14, 16): [0, 'deers', 500, 0]}

# DUMB A.I.
def DAI_orders_generator(Px):  # Spec 100 % and Code 100%
    # for each ww from Playerx in entities
    # get position and add to str
    AI_orders = ""
    for key, values in entities.items():
        if values[0] == Px:
            orig = key
            AI_orders = AI_orders + str(orig[0]) + "-" + str(orig[1]) + ":"
            #rand an order and add to str
            order_type = random.choice(["@", "*", "<", "pacify "])
            AI_orders = AI_orders + order_type
            # for x
            if order_type == "pacify ":
                #print(AI_orders)
                ...
            else:
                dest = [0, 0]
                stepx = random.choice([+1, -1, 0])
                dest[0] = orig[0] + stepx
                stepy = random.choice([+1, -1, 0])
                dest[1] = orig[1] + stepy
                AI_orders = AI_orders + str(dest[0]) + "-" + str(dest[1])+ " "
    #print(AI_orders)
    return AI_orders

# Test ordre 
orders_P1 = "10-10:@10-11 12-10:*12-11 19-20:*20-20 1-1:pacify 12-72:<27-48 17-20:pacify"
print("Orders for P1 this turn : "+orders_P1+"")
orders_P2 = DAI_orders_generator(2)
print("Orders for P2 this turn : "+orders_P2+"")
"""
===================
    GAME CYCLE
===================
*************
GENERIC TOOLS
*************
"""
def hash(string):  # Spec 100 % and Code 100%
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

def entity_at(entity_coords): # Spec 100 % and Code 100%
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2]]
    return [-1, "null", -1]

def in_range(range, ww_coords):  # Spec 100 % and Code 100%
    nbr_entity = 0
    ww_in_range = {}
    key = []
    for key, values in entities.items():
        #Test if entity is a werewolf
        if values[0] == 1 or values[0] == 2:
            x = abs(key[0]- ww_coords[0])
            y = abs(key[1]- ww_coords[1])
            if x == 0 and y == 0:
                ...  # current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key: values})
    return ww_in_range

"""
**************
GAME FUNCTIONS
**************
"""
# TESTER SI ENTITES A PORTEE POUR FEED AND FIGHT
def pacify(rayon, omega, pacified_werewolves):  # Spec 100 % and Code 100%
    if entities[omega][1] == "omega":
        if entities[omega][2] < 40:
            print(" Omega don't have enough energy to pacify")
        #For each ww at range <= 6
        else:
            for key in in_range(rayon, omega):
                pacified_werewolves.append(key)
            print(" These werewolves has been pacified for this turn " +
                str(pacified_werewolves)+"")
    else:
        print(" Not omega")
    return pacified_werewolves

def bonus(ww_coords):# Spec 0 % and Code 0%
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
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""
    #print(ww_coords)
    print(in_range(2, ww_coords))

def feed(list):  # Spec 100 % and Code 90%
    is_ww = []
    is_food = []
    if list[0] in entities:
        is_ww = entities[list[0]]
    #print(list[1])
    if list[1] in entities:
        is_food = entities[list[1]]
    else:
        print(" This entity doesn't exist on boardgame.")
    if is_food and is_food[0] == 0:
        if is_ww and is_ww[0] == 1:
            if is_ww[2] < 100:
                food_E = is_food[2]
                ww_E = is_ww[2]
                # Check if it's a werewolf or a human and put a "mutate" flag for that
                mutate = 0
                if ww_E == 0:
                    mutate = 1
                toteaten = 0
                while (food_E > 0) and (ww_E < 100):
                    food_E -= 1
                    ww_E += 1
                    toteaten += 1
                if food_E == 0:
                    print(" The "+is_food[1]+" have been completely eaten.")
                    entities.pop(list[1])
                else:
                    is_food[2] = food_E
                is_ww[2] = ww_E
                entities.update({list[1]: is_food})
                # If the "werewolf" was human, turn it into omega (if it was it in the past) or into werewolf
                if mutate == 1:
                    if is_ww[1] == "Human":
                        is_ww[1] = "omega"
                    else:
                        is_ww[1] = "normal"
                entities.update({list[0]: is_ww})
                print(" The werewolf at "+str(list[0])+" has eat "+str(
                    toteaten)+" energy from "+str(entities[list[1]][1])+" at "+str(list[1])+".")
            else:
                print(" Your werewolf energy is already at max.")
    else:
        print(" This is not food.")

def fight(listat, pacified_werewolves):  #  Spec 100 % and Code 90%
    #Check if attacker is in [pacified_werewolves]
    if listat[0] in pacified_werewolves:
        print(" This werewolf "+str(listat[0])+" has been pacified this turn.")
        #Check if E = 0 'cause human can't attack
        if listat[0] in entities:
            coord = listat[0]
            E_ww = entities[coord][2]
            if E_ww == 0:
                print(" A human (werewolf with energy = 0) can't attack")
            else:
                attacker = entities[listat[0]]
                if listat[1] in entities:
                    defender = entities[listat[1]]
                    attack_strength = (attacker[2]/10)
                    defender[2] = defender[2] - attack_strength
                    if defender[2] == 0:
                        if defender[1] == "omega":
                            defender[1] == "Human"
                        else:
                            defender[1] = "human"""
                    print(" "+str(defender[1]+" loose "+str(attack_strength) +
                        ", his energy is now : "+str(defender[2]))+"")
                    entities.update({listat[1]: defender})
                else:
                    print(" Nothing to attack there.")

def move(listmov):  # Spec 100 % and Code 100%
    #Check if destination is not out of the boardgame.
    if listmov[1][0] <= size[0] and listmov[1][1] <= size[1]:
        #Check is the destination is empty
        if not (listmov[1] in entities):
            x = int(abs(listmov[1][0]-listmov[0][0]))
            y = int(abs(listmov[1][1]-listmov[0][1]))
            if x == 1 and y == 1:
                print(" Move possible")
            else:
                print(" Move out of range")
        else:
            print(" Can't move there, this space is not empty.")
    else:
        print(" Can't move out of boardgame.")

"""
*****************
ORDERS MANAGEMENT
*****************
"""
def orders_manager(orders_P1, orders_P2):  # Spec 100 % and Code 100%
    # Convert Player 1 orders in a list
    cleanP1 = orders_P1.split()
    # Convert Player 2 orders in a list
    cleanP2 = orders_P2.split()
    # Initialize lists of different orders for each players.
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
        listcurord = hash(current_order)
        #print(listcurord)
        # Next 3 lines check if ww is in team 1
        current_ww = listcurord[1]
        current_ww_values = entity_at(current_ww)
        if current_ww_values[0] == 1:
            #print(current_ww_values)
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
        listcurord = hash(current_order)
        # Next 3 lines check if ww is in team 2
        current_ww = listcurord[1]
        current_ww_values = entity_at(current_ww)
        if current_ww_values[0] == 2:
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
        print(pacify_P1)
        if pacify_P1[0] in entities:
            print("Player 1 pacify phase.")
            while len(pacify_P1) > 0:
                pacify(6, pacify_P1[0], pacified_werewolves)
                pacify_P1.pop(0)
    # Check if Player 2 given pacify order and run it.
    if len(pacify_P2) > 0:
        print("Player 2 pacify phase.")
        while len(pacify_P2) > 0:
            # Rajouter les arguments rayon et pacified_werewolfs
            pacify(6, pacify_P2[0], pacified_werewolves)
            pacify_P2.pop(0)
    # ---------------------
    # --- BONUSES PHASE ---
    # ---------------------
    # Store bonus of each ww in a separated list
    # --- bonuses(P1) ---
    #Make a team_P1 dictionnary that contains all alive werewolfs from player 1
    team1 = {}
    for key, values in entities.items():
        if values[0] == 1:
            team1.update({key: values})
    #Supprimer ce if et envoyer team1 à bonus()
    # retuner team1 depuis bonus et l'utiliser dans fight -> attacker
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
            #print(feeds_orders_P1)
            feed(feeds_orders_P1[0][1:3])
            print(" --- ")
            feeds_orders_P1.pop(0)
    # Check if Player 2 given feeds orders and run them.
    if len(feeds_orders_P2) > 0:
        print("Player 2 feed phase.")
        while len(feeds_orders_P2) > 0:
            #print(feeds_orders_P2)
            feed(feeds_orders_P2[0][1:3])
            print(" --- ")
            feeds_orders_P2.pop(0)
    # --------------------
    # --- ATTACK PHASE ---
    # --------------------
    # Check if Player 1 given attacks orders and run them.
    if len(attacks_orders_P1) > 0:
        print("Player 1 attack phase.")
        while len(attacks_orders_P1) > 0:
            fight(attacks_orders_P1[0][1:3], pacified_werewolves)
            print(" --- ")
            attacks_orders_P1.pop(0)
    # Check if Player 2 given attacks orders and run them.
    if len(attacks_orders_P2) > 0:
        print("Player 2 attack phase.")
        while len(attacks_orders_P2) > 0:
            fight(attacks_orders_P2[0][1:3], pacified_werewolves)
            print(" --- ")
            attacks_orders_P2.pop(0)
    # ------------------
    # --- MOVE PHASE ---
    # ------------------
    # Check if Player 1 given move orders and run them.
    if len(move_orders_P1) > 0:
        print("Player 1 move phase.")
        while len(move_orders_P1) > 0:
            move(move_orders_P1[0][1:3])
            print(" --- ")
            move_orders_P1.pop(0)
    # Check if Player 2 given move orders and run them.
    if len(move_orders_P2) > 0:
        print("Player 2 move phase.")
        while len(move_orders_P2) > 0:
            move(move_orders_P2[0][1:3])
            print(" --- ")
            move_orders_P2.pop(0)
    #Nettoyer et vider les listes et valeurs bonus.

orders_manager(orders_P1, orders_P2)

#-*- coding: utf-8 -*-
import blessed, math, os, time, random
from remote_play import *


pics = {"alpha": "α", "omega": "Ω", "normal": "🐺", "human": "👤",
        "berries": "🍒", "apples": "🍎", "mice": "🐁", "rabbits": "🐇", "deers": "🦌"}

"""
===========================================
    GLOBAL AND INITIALIZATION FUNCTIONS
===========================================
"""
# SELECTION OF ONE OF THE SIX DIFFERENT GAME MODE

# Creation of all "global" variables required for the game
P1_game_mode = "local"
P2_game_mode = "local"
group_1 = 20
group_2 = 1
P1_type = "Human"
P2_type ="A.I."
orders_P1 = "-"
orders_P2 = "-"
size = []
entities = {}
game_turn = 1

#print(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type, orders_P1, orders_P2)

def game_settings(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):  # Spec and Code 100%
 
    # Selection player 1
    # ------------------
    #Local OR Remote
    temp_P1_game_mode = int(input('Select game mode for player 1 => 0 (Local) OR 1 (Remote) : '))
    # If Remote ask for group number
    if temp_P1_game_mode == 1:
        P1_game_mode = "remote"
        group_1 = int(input("Please enter the group number for player 1 : "))
    else:
        P1_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    temp_P1_type = int(input("Select game type for player 1 => 0 (Human) OR 1 (A.I.) : "))
    if temp_P1_type == 1:
        P1_type = "A.I."
    else:
        P1_type = "Human"
    # ------------------
    # Selection player 2
    # ------------------
    #Local OR Remote
    temp_P2_game_mode = int(input("Select game mode for player 2 => 0 (Local) OR 1 (Remote) : "))
    # If Remote ask for group number
    if temp_P2_game_mode == 1:
        P2_game_mode = "remote"
        group_2 = int(input("Please enter the group number for player 2 : "))
    else:
        P2_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    temp_P2_type = int(input("Select game type for player 2 => 0 (Human) OR 1 (A.I.) : "))
    if temp_P2_type == 1:
        P2_type = "A.I."
    else:
        P2_type = "Human"
    # P1 from group number on local/remote and it's a human/IA
    print(f"Player 1 from group : {group_1} on {P1_game_mode} and it's a {P1_type}.")
    # P2 from group number on local/remote and it's a human/IA
    print(f"Player 2 is from group : {group_2} on {P2_game_mode} and it's a {P2_type}.")
    return [P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type]

#P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type = game_settings(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)

#print(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)

def data_import(size, entities): # Spec and Code 100%
    # Ask for ano file path
    #path = input("Please give the path to the .ano file : ")
    path = "C:/Users/Seb/Documents/GitHub/UNamur_Q2_ProgProject/_3_Dossier_de_travail/Short example.ano"
    # List for map size
    #size = []
    # A unique dictionnary to rules them all
    #entities = {}
    # Open .ano file
    with open(path, "r+") as file:
        # Read the entire file and store it into a list.
        brut = file.readlines()
        for i in brut:
            # Ignore string line
            if (i[0] == "m") or (i[0] == "w") or (i[0] == "f"):
                continue
            # Detect if line contains boardgame size
            if len(i) <= 6:
                si = i.split()
                size = [int(si[0]), int(si[1])]
                continue
            j = i.split()
            # Check if line contain werewolf info or not
            if (j[3] == "alpha") or (j[3] == "omega") or (j[3] == "normal"):
                x = int(j[1])
                y = int(j[2])
                values = [int(j[0]), (j[3]), 100, 0]
                entities.update({(x, y): values})
            else:
                x = int(j[0])
                y = int(j[1])
                # Add "0" as first list value element for food to make the "food team" identified with 0
                values = [0, (j[2]), int((j[3])), 0]
                entities.update({(x, y): values})
    return size, entities
    print("Map Size : ", size)
    print("Entities :", entities)

size, entities = data_import(size, entities)

# create connection, if necessary
if P1_game_mode == 'remote':
    connection = create_connection(group_2, group_1)
elif P2_game_mode == 'remote':
    connection = create_connection(group_1, group_2)

# close connection, if necessary
def end_connection():  # Spec 0 % and Code 100%
    if P1_game_mode == 'remote' or P2_game_mode == 'remote':
        close_connection(connection)

"""
===================
    A.I. ENGINE
===================
"""
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
                AI_orders = AI_orders + str(dest[0]) + "-" + str(dest[1]) + " "
    #print(AI_orders)
    return AI_orders

# SMART A.I.
def SAI_orders_generator(Px): #Spec 0 % and Code 0%
    ...

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
    return False

def in_range(range, omega_coord):  # Spec 100 % and Code 100%
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

def at_range():
    ...


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


def bonus(ww_coords):  # Spec 0 % and Code 0%
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
    #print(in_range(2, ww_coords))


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


def fight(listat, pacified_werewolves):  # Spec 100 % and Code 90%
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
    #print(size)
    #Check if destination is not out of the boardgame.
    if listmov[1][0] <= size[0] and listmov[1][1] <= size[1]:
        #Check is the destination is empty
        if not (listmov[1] in entities):
            x = int(abs(listmov[1][0]-listmov[0][0]))
            #print(x)
            y = int(abs(listmov[1][1]-listmov[0][1]))
            #print(y)
            if x <= 1 and y <= 1:
                print(" Move possible")
                for key, values in entities.items():
                    if key == listmov[0]:
                        val = values
                entities.update({listmov[1]: val})
                entities.pop(listmov[0])
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
def get_orders(orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type):  # Spec 100 % and Code 100%
    print(" - GET ORDERS - ")
    #Clean orders
    orders_P1 = ""
    orders_P2 = ""
    # Check if P1 is remote and if true ask for orders
    if P1_game_mode == "remote":
        print("Player 1 is remote, ask for orders...")
        orders_P1 = get_remote_orders(connection)
    # If not, check if it's human
    elif P1_type == "Human":
        orders_P1 = input(print("Player 1, could you please enter your orders for this turn : "))
    else:
        orders_P1 = DAI_orders_generator(1)
    # Notify player 2, if remote, with P1 orders
    if P2_game_mode == "remote":
        notify_remote_orders(connection, orders_P1)
    # ----------------------------------------------------
    # Check if P2 is remote and if true ask for orders
    if P2_game_mode == "remote":
        orders_P2 = get_remote_orders(connection)
    elif P2_type == "Human":
        orders_P2 = input(print("Player 2, could you please enter your orders for this turn : "))
    else:
        orders_P2 = DAI_orders_generator(2)
    # Notify player 1, if remote, with P2 orders
    if P1_game_mode == "remote":
        notify_remote_orders(connection, orders_P2)
    print("P1 orders : "+str(orders_P1)+"")
    print("P2 orders : "+str(orders_P2)+"")
    return (orders_P1, orders_P2)

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
        listcurord = hash(current_order)
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
    # Store bonus of each ww in a separated list

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
            #print(feeds_orders_P1)
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

def stop():
    print("FIN")


n = size[0]


def make_board(n):
    return [[' ..... ' for count in range(n)] for rows in range(n)]


def print_board(board):
    for row in board:
        print('|'.join(row))
    print('')


def updateboard(myboard):
    r = n
    c = n
    #print (r,c)
    for i in range(r):
        for j in range(c):
            coords = (i, j)
            #print(coords)
            if (i == 0) and (j == 0):
                myboard[i][j] = " \ "
                ...
            elif (i == 0) and (j < c):
                myboard[i][j] = " "+str(j)+""
                ...
            elif (i < r) and (j == 0):
                myboard[i][j] = " "+str(i)+" "
                ...
            elif (i == r) and (j == c):
                myboard[i][j] = " /  "
                ...
            elif coords in entities:
                picture_name = entities[coords][1]
                if (entities[coords][1] == "α") or (entities[coords][1] == "Ω"):
                    picture = (""+str(pics[picture_name][0])+" ")
                else:
                    picture = pics[picture_name][0]
                myboard[i][j] = picture
            else:
                myboard[i][j] = ".."
                #myboard[i][j] = ""+str(coords)+""

    return myboard


def test():
    myboard = make_board(n)
    updateboard(myboard)
    print_board(myboard)


"""if __name__ == '__main__':
    test()"""



def game_loop(game_turn, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type):  # Spec 100 % and Code 33%
    # Vérifier numéro de tour ==> Règles à vérifier
    if game_turn == 3:
        stop()
    # Vérifie l'E des Alphas
    
    else:
        # Demander les ordres et les envoyer au orders manager
        print(" ---------------- ")
        test()
        print("GAME TURN : "+str(game_turn)+"")
        orders_P1, orders_P2 = get_orders(orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)
        orders_manager(orders_P1, orders_P2)
        #orders_manager(get_orders(orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type))
        game_turn += 1
        #print(entities)
        game_loop(game_turn, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)


game_loop(game_turn, orders_P1, orders_P2,
          P1_game_mode, P2_game_mode, P1_type, P2_type)


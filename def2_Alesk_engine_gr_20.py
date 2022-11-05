#-*- coding: utf-8 -*-
import blessed
import math
import os
import time
import random
from remote_play import *
term = blessed.Terminal()

"""
GitHub repo link : https://github.com/Nauorac/UNamur_Q2_ProgProject.git
Teams : https://teams.microsoft.com/l/team/19%3a1PyM1mIAE8RltmCrW7LWFpIDlxBP_HpmO6jHthKtZPk1%40thread.tacv2/conversations?groupId=d3822f0a-0364-465c-922d-7c88fcd06299&tenantId=5f31c5b4-f2e8-4772-8dd6-f268037b1eca

EXPLANATIONS
~~~~~~~~~~~~
For a better comprehension of this file, we've made a glossary and an index.
Each section and functions are referenced with the line number.

Glossary
--------
Px = Player x (int)
group_x = Group number of player x (int)
Px_game_mode = Local or remote game mode of player x (str)
Px_type = Is player x is human or I.A. (str)
ww = werewolf
E = energy
S = Specification
C = Code

Index
------
GLOBALS AND INITIALIZATION FUNCTIONS - line 58
## This section contains all the functions that are used to initialize the game.
    - def game_settings() - line 95 - # S 100%/ C 100%
    - def change_path() - line 100 - # S 50%/ C 50%
    - def data_import() - line 158 - # S 100%/ C 100%
    - connection - line 198
    - def close_connection() - line 218 - # S 0%/ C 100%
    - def startlifePlayer() - line 796 - # S 0%/ C 0%
A.I. - line 234
## This section contains A.I. functions.(for the dumb A.I.)
    - def DAI_orders_generator() - line 238 - # S 100%/ C 100%
    - def SAI_orders_generator() - line 286 - # S 0%/ C 0%
GAME CYCLE - line 291
## This section contains the game cycle functions (that implement game rules) ans also usefull functions.
    - GENERIC TOOLS - line 294
        - def hash() - line 297 - # S 100%/ C 100%
        - def entity_at() - line 340 - # S 100%/ C 100%
        - def in_range() - line 371 - # S 100%/ C 100%
    - GAME FUNCTIONS - line 462
        - def pacify() - line 466 - # S 100%/ C 100%
        - def bonus() - line 511 - # S 0%/ C 0%
        - def feed() - line 539 - # S 100%/ C 90%
        - def fight() - line 601 - # S 100%/ C 90%
        - def move() - line 642 - # S 100%/ C 100%
U.I. - line 686
## This section contains the U.I. functions.
    - def welcome_screen() - line 691 - # S 0%/ C 0%
    - def settings() - line 703 - # S 0%/ C 0%
    - def boardgame_manager() - line 722 - # S 0%/ C 0%
GAME MANAGER - line 812
## This section contains the functions to manage a game.
        - def get_orders() - line 820 - # S 100%/ C 100%
        - def orders_manager() - line 879 - # S 100%/ C 100%
        - def totlifePlayer() - line 1041 - # S 0%/ C 0%
        - def stop() - line 1038 - # S 0%/ C 0%
        - def game_loop() - line 1048 - # S 100%/ C 33%
******************************
Last things to do before submission
- Bugs & Fix
    -- Ask for filepath
    -- end game check
    -- For human player : orders helper input
    -- Possibility to make a verbose mode, display or not alls the messages, add a param to each function
        by default set to 0 = non-verbose mode, possibility to change on the game settings screen to 1
    -- Possibility to make a record mode(store all the data in a file), add a param to each function
        by default set to 0 = non-storage mode, possibility to change on the game settings screen to 1 to store each action on a file
"""

"""
===========================================
    GLOBALS AND INITIALIZATION FUNCTIONS
===========================================
"""
# SELECTION OF ONE OF THE SIX DIFFERENT GAME MODE
"""
# Cases :
# 1) P1 - Local - Human | P2 - Local - Human
# 2) P1 - Local - Human | P2 - Local - IA
# 3) P1 - Local - IA    | P2 - Local - IA
# 4) P1 - Local - Human | P2 - Lan - Human
# 5) P1 - Local - IA    | P2 - Lan - IA
# 6) P1 - Local - IA    | P2 - Lan - Human
# If we want arbitrate we could add 3 more game type
# 7) P1 - Lan - Human   | P2 - Lan - Human
# 8) P1 - Lan - IA      | P2 - Lan - IA
# 9) P1- Lan - Human    | P2 - Lan - IA
"""

# Creation of all "global" variables required for the game
path = "D:/Cours/UNamur_Q2_ProgProject/_3_Dossier_de_travail/example.ano"
#https://github.com/Nauorac/UNamur_Q2_ProgProject/blob/526bafbbaa287bad23a7efa7956b62999b42a00b/_0_Ennonce/example.ano

P1_game_mode = "local"
P2_game_mode = "local"
group_1 = 20
group_2 = 1
P1_type = "A.I."
P2_type = "A.I."
orders_P1 = "-"
orders_P2 = "-"
size = []
entities = {}
game_turn = 1
turn_without_damage = 0

#Next two dictionnaries are used to assign UTF-8 "pictures" with keywords
pics = {"alpha": "α", "omega": "Ω", "normal": "🐺", "human": "👤", "berries": "🍒", "apples": "🍎", "mice": "🐁", "rabbits": "🐇", "deers": "🦌"}
g_set_pics = {"Human": "👤", "A.I.": "🤖", "local": "💻", "remote": "🖧", }

def game_settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):  # Spec and Code 100%
    """
	Description of the function
	---------------------------
    Function that ask with inputs to select all the game settings.

    Returns:
    --------
	list : Return a list with all the settings defined by players
    ["P1", group_1, P1_game_mode, P1_type, "P2", group_2, P2_game_mode, P2_type]

	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 11/03/2022)
	Code : Sébastien Baudoux (v.3.0 - 11/03/2022)
	"""
    with term.cbreak():
        # Selection player 1
        # ------------------
        #Local OR Remote
        print("Select game mode for player 1 => 0 (Local) OR 1 (Remote) : ")
        temp_P1_game_mode = term.inkey()
        # If Remote ask for group number
        if temp_P1_game_mode == 1:
            P1_game_mode = "remote"
            group_1 = int(
                input("Please enter the group number for player 1 : "))
        else:
            P1_game_mode = "local"
            group_1 = 20
        # Human or I.A.
        print("Select game type for player 1 => 0 (Human) OR 1 (A.I.) : ")
        temp_P1_type = term.inkey()
        if temp_P1_type == 1:
            P1_type = "A.I."
        else:
            P1_type = "Human"
        # ------------------
        # Selection player 2
        # ------------------
        #Local OR Remote
        print("Select game mode for player 2 => 0 (Local) OR 1 (Remote) : ")
        temp_P2_game_mode = term.inkey()
        # If Remote ask for group number
        if temp_P2_game_mode == 1:
            P2_game_mode = "remote"
            group_2 = int(
                input("Please enter the group number for player 2 : "))
        else:
            P2_game_mode = "local"
            group_1 = 20
        # Human or I.A.
        print("Select game type for player 2 => 0 (Human) OR 1 (A.I.) : ")
        temp_P2_type = term.inkey()
        if temp_P2_type == 1:
            P2_type = "A.I."
        else:
            P2_type = "Human"
        # P1 from group number on local/remote and it's a human/IA
        print(
            f"Player 1 from group : {group_1} on {P1_game_mode} and it's a {P1_type}.")
        # P2 from group number on local/remote and it's a human/IA
        print(
            f"Player 2 is from group : {group_2} on {P2_game_mode} and it's a {P2_type}.")
        return [path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type]

def change_path(path):  # Spec and Code 100%
    """
    Description of the function
    ---------------------------
    Function that ask with inputs to select the file path.

    Returns:
    --------
    string : Return the path of the file
    """
    with term.cbreak():
        print("Please enter the path of the file : ")
        path = term.inkey()
        return path

def data_import(path, size, entities):  # Spec and Code 100%
    """
	Description
	---------------------------
    Update the size tuple and the entities dictionary with data in a ano file.

    Args:
    -----
    path : filepath of the .ano file  - str
    size : Tuple with 2 elements, raw number and column number - tuple
    entities : Dictionnary that contains all elements on the boardgame - dict

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 11/03/2022)
	Code : Trésor Tchientcheu (v.3.0 - 25/04/2022)
	"""
    file = open(path, "r")
    liste = file.readlines()
    for i in range(len(liste)):
        # Detect if line contains boardgame size
        if ("map" in liste[i]):
            j = i+1
            si = liste[j].split(" ")
            size = [int(si[0]), int(si[1])]
            j = i+1
        elif ("werewolves" in liste[i]):
            j = i+1
            while liste[j] != "foods:\n":
                a = liste[j].split(" ")
                b = a[3].split("\n")
                entities[int(a[1]), int(a[2])] = [int(a[0]), (b[0]), 100, 0]
                j = j+1
        elif ("foods" in liste[i]):
            j = i+1
            while j < len(liste):
                a = liste[j].split(" ")
                b = a[2].split("\n")
                entities[int(a[0]), int(a[1])] = [0, (b[0]), int(a[3])]
                j = j+1
    return path, size, entities

path, size, entities = data_import(path, size, entities)

# create connection, if necessary
if P1_game_mode == 'remote':
    connection = create_connection(group_2, group_1)
elif P2_game_mode == 'remote':
    connection = create_connection(group_1, group_2)

# close connection, if necessary

def end_connection():  # Spec 0 % and Code 100%
    """
	Description of the function
	---------------------------
    Close connection at game end

	Version:
	--------
	Specification : Author (v.1.0 - dd/mm/yyyy)
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""
    if P1_game_mode == 'remote' or P2_game_mode == 'remote':
        close_connection(connection)

def startlifePlayer(Px):
    totlife = 0
    for key in entities:
        if entities[key][0] == Px:
            totlife += entities[key][2]
    return totlife

beginlifeP1 = startlifePlayer(1)
beginlifeP2 = startlifePlayer(2)

"""
===================
    A.I. ENGINE
===================
"""
# DUMB A.I.
def DAI_orders_generator(Px): # Spec 100 % and Code 100%
    """
	Description of the function
	---------------------------
    Generate a random order for each werewolf of the player in argument.

    Uses:
    -----
    Generate orders for A.I.

    Args:
    -----
    Px : Player number - int

    Returns:
    --------
	str : A string that contains one order for each werewolf in the player team.

	Version:
	--------
	Specification: Sébastien Baudoux(v.2.0 - 08/03/2022)
    Code: Sébastien Baudoux(v.2.0 - 08/03/2022)
	"""
    # for each ww from Playerx in entities
    # get position and add to str
    AI_orders = ""
    for key, values in entities.items():
        if values[0] == Px:
            if entities[key][1] == "alpha" :
                smart_alpha(Px, key)
            if entities[key][1] == "omega" :
                AI_orders = smart_omega(Px, key, AI_orders)
            if entities[key][1] == "normal" :
                AI_orders = smart_wolves(Px, key, AI_orders)
            if entities[key][1] == "human" :
                smart_human(Px, key)
    return AI_orders

def distance(position_x1, position_y1, position_x2, position_y2):
    if abs(position_x2 - position_x1) > abs(position_y2-position_y1):
        return abs(position_x2-position_x1)
    else:
        return abs(position_y2-position_y1)

def target_Ealpha(Px):
    Ealpha_pos=[]
    for cle in entities:
        # Check if it's an opposite alpha of the entities in argument
        if(entities[cle][0] != Px and entities[cle][0] != 0 and entities[cle][1] == "alpha"):
            Ealpha_pos.append(cle[0])
            Ealpha_pos.append(cle[1])
    return Ealpha_pos

going_to = {"N": [-1, 0], "NE": [-1, +1], "E": [0, +1], "SE": [+1, +1], "S": [+1, 0], "SW": [+1, -1], "W": [-1, 0], "NW": [-1, -1]}
alt_dir = {"N": ("NW", "NE"), "S": ("SW", "SE"), "E": ("NE", "SE"), "W": (
    "NW", "SW"), "NE": ("N", "E"), "SE": ("S", "E"), "NW": ("N", "W"), "SW": ("S", "W")}

def direction(ww_pos, Ealpha_pos):
    if Ealpha_pos[0] > ww_pos[0]:
        x = 1 #To te South
    elif Ealpha_pos[0] < ww_pos[0]:
        x = -1 #To the North
    elif Ealpha_pos[0] == ww_pos[0]:
        x = 0 #No horizontal move
    if Ealpha_pos[1] > ww_pos[1]:
        y = 1 #To the East
    elif Ealpha_pos[1] < ww_pos[1]:
        y = -1 #To the West
    elif Ealpha_pos[1] == ww_pos[1]:
        y   = 0 #No vertical move
    #Directions
    if x == -1 and y == 0:
        direct = "N"
    elif x == -1 and y == 1:
        direct = "NE"
    elif x == 0 and y == 1:
        direct = "E"
    elif x == 1 and y == 1:
        direct = "SE"
    elif x == 1 and y == 0:
        direct = "S"
    elif x == 1 and y == -1:
        direct = "SW"
    elif x == 0 and y == -1:
        direct = "W"
    elif x == -1 and y == -1:
        direct = "NW"
    #return direct
    ww_pos[0] += x
    ww_pos[1] += y
    return ww_pos

def smart_alpha(Px, key):
    ...

def smart_omega(Px, key, AI_orders):
    """
	Description of the function
	---------------------------
    The AI of the Omega werewolf

    Args:
    -----
    Px : The werewolfs team - int
    key : The werewolfs position - tuple
    AI_orders : A string of orders - str
    
    Returns:
    --------
	AI_orders : A string of orders - str

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 02/05/2022)
    Code: Aleksander Besler(v.1.0 - 02/05/2022)
	"""
    #enemy_wolf, allied_wolf = omega_strat_decider(key)
    #enemy_wolf_count = get_number_of_elements(enemy_wolf)
    #allied_wolf_count = get_number_of_elements(allied_wolf)
    enemy_wolf_count = 0 
    allied_wolf_count = 1
    if entities[key][2] > 41:
        if enemy_wolf_count > allied_wolf_count :
            x1, y1 = key
            AI_orders = AI_orders + str(x1) + "-" + str(y1) + ":"
            order_type = "pacify "
            AI_orders = AI_orders + order_type
            return AI_orders
        if enemy_wolf_count < 1 :
            direction = ""
            direction = where_to_go(key, Px)
            test = where_movement_is_available(key, direction)
            if test != []:
                x2, y2 = test
                x1, y1 = key
                AI_orders = AI_orders + str(x1) + "-" + str(y1) + ":"
                order_type = "@"
                AI_orders = AI_orders + order_type
                AI_orders = AI_orders + str(x2) + "-" + str(y2) + " " 
                return AI_orders 
            else : 
                print("movement not available")
    return AI_orders
                         
    

def smart_wolves(Px, key, AI_orders):
    danger_spaces=ww_danger(key)
    # checks for any danger around the werewolf
    if danger_spaces == []:
        if entities[key][2] > 25:
            direction = where_to_go(key, Px)
            test = where_movement_is_available(key, direction)
            if test != []:
                x2, y2 = test
                x1, y1 = key
                AI_orders = AI_orders + str(x1) + "-" + str(y1) + ":"
                order_type = "@"
                AI_orders = AI_orders + order_type
                AI_orders = AI_orders + str(x2) + "-" + str(y2) + " " 
                return AI_orders 
            else : 
                print("movement not available") 
    else:
        lowhealthwolf = lowest_health(danger_spaces)
        if entities[key][2] > 25:
            x1, y1 = key
            x2, y2 = lowhealthwolf
            AI_orders = AI_orders + str(x1) + "-" + str(y1) + ":"
            order_type = "*"
            AI_orders = AI_orders + order_type
            AI_orders = AI_orders + str(x2) + "-" + str(y2) + " " 
            return AI_orders
    
def smart_human(Px, key):
    ...
# SMART A.I.

def lowest_health(danger_spaces):
    """
	Description of the function
	---------------------------
    Ckecks wich wolf has the lowest health from the dangerous spaces list

    Args:
    -----
    danger_spaces : list of units that are from the opposing team - list

    Returns:
    --------
	lowhealthwolf : Coordinates of the lowest health wolf found - str

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 30/04/2022)
    Code: Aleksander Besler(v.1.0 - 30/04/2022)
	"""
    count= get_number_of_elements(danger_spaces)
    # Counts number of entities in a list
    danger1 = entities[danger_spaces[0]]
    lowhealth= danger1[2]
    lowhealthwolf= danger_spaces[0]
    # Puts the first wolf as the lowest health one to have a base to compare on
    for i in range(count):
        if lowhealth > danger1[2]:
            # Compares each wolfs health and takes the one with the lowest health
            lowhealth = danger1[2]
            lowhealthwolf = danger_spaces[i]
    return lowhealthwolf

def get_number_of_elements(list):
    """
	Description of the function
	---------------------------
    Counts number of entities in a list

    Args:
    -----
    list : the list wich we want to get the number of elements - list

    Returns:
    --------
	count : number of elements in list - int

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 30/04/2022)
    Code: Aleksander Besler(v.1.0 - 30/04/2022)
	"""
    count = 0
    for element in list:
        count += 1
    return count    

def where_to_go(ww_pos, Px):
    """
	Description of the function
	---------------------------
    Analyses where the werewolf can go

    Args:
    -----
    ww_pos : position of the wolf - coord 
    Px : wich team the wolf is on - int
    
    Returns:
    --------
	direction : Direction in wich the wolf can go 

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 02/05/2022)
    Code: Aleksander Besler(v.1.0 - 02/05/2022)
	"""
    if Px == 1:
        ennemy = 1
    else:
        ennemy = 2
    x2, y2 = target_Ealpha(ennemy)
    x1, y1 = ww_pos
    direction = ""
    if x1 < x2 and y1 == y2 :
        direction = "E"
    if x1 > x2 and y1 == y2 :
        direction = "W"
    if x1 == x2 and y1 < y2 :
        direction = "N"
    if x1 == x2 and y1 > y2 :
        direction = "S"
    if x1 < x2 and y1 < y2 :
        direction = "SE"
    if x1 > x2 and y1 < y2 :
        direction = "SW"
    if x1 < x2 and y1 > y2 :
        direction = "NE"
    if x1 > x2 and y1 > y2 :
        direction = "NW"
    return direction

def where_movement_is_available(ww_pos, direction):
    """
	Description of the function
	---------------------------
    Analyses where the werewolf can go

    Args:
    -----
    ww_pos : position of the wolf - coord 
    direction : direction in wich the wolf has to go - str
    
    Returns:
    --------
	confirmed_direction : Confirmed Direction in wich the wolf can go 

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 02/05/2022)
    Code: Aleksander Besler(v.1.0 - 02/05/2022)
	"""
    confirmed_direction = []
    x, y = ww_pos
    E = x+1, y
    N = x, y+1
    NE = x+1, y+1
    SE = x-1, y+1
    SW = x-1, y-1
    NW = x+1, y-1
    W = x-1, y
    S = x, y-1
    #print(NE, E, N, W, S, SE, SW, NW, direction)
    if direction == "N" :
        if (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
    if direction == "NE" :
        if (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
    if direction == "E" :
        if (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
    if direction == "SE" :
        if (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        if (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        if (x, y-1) not in entities and y-1 != 0 and confirmed_direction == []:
            confirmed_direction = S
        if (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = NE
        if (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        if (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        if (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        if (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = SW
        print(confirmed_direction)
    if direction == "S" :
        if (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
    if direction == "SW" :
        if (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
    if direction == "W" :
        if (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
        elif (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
    if direction == "NW" :
        if (x+1, y-1) not in entities and y+1 != 21 and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = NW
        elif (x-1, y) not in entities and x-1 != 0 and confirmed_direction == []:
            confirmed_direction = W
        elif (x-1, y-1) not in entities and y-1 != 0 and x-1 != 0 and confirmed_direction == [] :
            confirmed_direction = SW
        elif (x, y+1) not in entities and y+1 != 21:
            confirmed_direction = N
        elif (x, y-1) not in entities and y-1 != 0 and confirmed_direction == [] :
            confirmed_direction = S
        elif (x+1, y) not in entities and x+1 != 21 and confirmed_direction == []:
            confirmed_direction = E
        elif (x+1, y+1) not in entities and y+1 != 21 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = NE
        elif (x-1, y+1) not in entities and y-1 != 0 and x+1 != 21 and confirmed_direction == [] :
            confirmed_direction = SE
    return confirmed_direction

    
def get_team(Px):
    team = {}
    for cle in entities:
        if entities[cle][0] == Px:
            team[cle] = entities[cle]
            # Création du flag d'action
            team[cle][0] = 0
    return team

def empty_places(ww_pos):
    x = ww_pos[0]
    y = ww_pos[1]
    empty_spaces = []
    if (x+1, y) not in entities:
        empty_spaces.append((x+1, y))
    if (x, y+1) not in entities:
        empty_spaces.append((x, y+1))
    if (x+1, y+1) not in entities:
        empty_spaces.append((x+1, y+1))
    if (x-1, y+1) not in entities:
        empty_spaces.append((x-1, y+1))
    if (x-1, y-1) not in entities:
        empty_spaces.append((x-1, y-1))
    if (x+1, y-1) not in entities:
        empty_spaces.append((x+1, y-1))
    if (x-1, y) not in entities:
        empty_spaces.append((x-1, y))
    if (x, y-1) not in entities:
        empty_spaces.append((x, y-1))
    return empty_spaces

def ww_danger(ww_pos):
    """
	Description of the function
	---------------------------
    Ckecks if there is any danger around the wolf

    Args:
    -----
    ww_pos : position of teh wolf - str

    Returns:
    --------
	danger_spaces : list of units that are from the opposing team - list

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 30/04/2022)
    Code: Aleksander Besler(v.1.0 - 29/04/2022)
	"""
    x = ww_pos[0]
    y = ww_pos[1]
    team = entities[ww_pos][0]
    if team == 1:
        team = 2
    else :
        team = 1
    # Indicates wich team has to be attacked
    danger_spaces = []
    if x - 1 > 0 and x + 1 < 21:
        # Checks if the target is in boarder
        if (x+1, y) in entities :
            # Checks if the target exists
            if entities[x+1, y][0] == team :
                # Verifies if the target is of the opposing team
                danger_spaces.append((x+1, y))
                # Puts the target in the danger list
        if (x-1, y) in entities :
            if entities[x-1, y][0] == team :
                danger_spaces.append((x-1, y))
    if y - 1 > 0 and y + 1 < 21:
        if (x, y-1) in entities :
            if entities[x, y-1][0] == team :
                danger_spaces.append((x, y-1))
        if (x, y+1) in entities :
            if entities[x, y+1][0] == team :
                danger_spaces.append((x, y+1))
    if y - 1 > 0 and y + 1 < 21 and x - 1 > 0 and x + 1 < 21:
        if (x+1, y+1) in entities :
            if entities[x+1, y+1][0] == team :
                danger_spaces.append((x+1, y+1))
        if (x-1, y+1) in entities :
            if entities[x-1, y+1][0] == team :
                danger_spaces.append((x-1, y+1))
        if (x-1, y-1) in entities :
            if entities[x-1, y-1][0] == team :
                danger_spaces.append((x-1, y-1))
        if (x+1, y-1) == team :
            if entities[x+1, y-1][0] in entities :
                danger_spaces.append((x+1, y-1))
    return danger_spaces

def omega_strat_decider(ww_pos):
    """
	Description of the function
	---------------------------
    Ckecks what is around the omega to better know what strategy to implement 

    Args:
    -----
    ww_pos : position of teh wolf - str

    Returns:
    --------
	Enemy_wolf : A list of ennemy wolf around the omega - list 
    allied_wolf : A list of allied wolf around the omega - list

	Version:
	--------
	Specification: Aleksander Besler(v.1.0 - 30/04/2022)
    Code: Aleksander Besler(v.1.0 - 29/04/2022)
	"""
    x = ww_pos[0]
    y = ww_pos[1]
    team = entities[ww_pos][0]
    if team == 1:
        team = 2
    else :
        team = 1
    if team == 1:
        ally = 1
    else :
        ally = 2
    # Indicates wich team has to be attacked
    enemy_wolf = []
    allied_wolf = []
    test = 1
    while test != 4 :
        if x - test > 0 and x + test < 21:
            # Checks if the target is in boarder
            if (x+test, y) in entities :
                # Checks if the target exists
                if entities[x+test, y][0] == team :
                    # Verifies if the target is of the opposing team
                    enemy_wolf.append((x+test, y))
                    # Puts the target in the ennemy list
                if entities[x+test, y][0] == ally :
                    allied_wolf.append((x+test, y))
                    # Puts the target in the ally list
            if (x-test, y) in entities :
                if entities[x-test, y][0] == team :
                    enemy_wolf.append((x-test, y))
                if entities[x-test, y][0] == ally :
                    allied_wolf.append((x-test, y))
        if y - test > 0 and y + test < 21:
            if (x, y-test) in entities :
                if entities[x, y-test][0] == team :
                    enemy_wolf.append((x, y-test))
                if entities[x, y-test][0] == ally :
                    allied_wolf.append((x, y-test))
            if (x, y+1) in entities :
                if entities[x, y+test][0] == team :
                    enemy_wolf.append((x, y+test))
                if entities[x, y+test][0] == ally :
                    allied_wolf.append((x, y+test))
        if y - test > 0 and y + test < 21 and x - test > 0 and x + test < 21:
            if (x+test, y+test) in entities :
                if entities[x+test, y+test][0] == team :
                    enemy_wolf.append((x+test, y+test))
                if entities[x+test, y+test][0] == ally :
                    allied_wolf.append((x+test, y+test))
            if (x-test, y+test) in entities :
                if entities[x-test, y+test][0] == team :
                    enemy_wolf.append((x-test, y+test))
                if entities[x-test, y+test][0] == ally :
                    allied_wolf.append((x-test, y+test))
            if (x-test, y-test) in entities :
                if entities[x-test, y-test][0] == team :
                    enemy_wolf.append((x-test, y-test))
                if entities[x-test, y-test][0] == ally :
                    allied_wolf.append((x-test, y-test))
            if (x+test, y-test) == team :
                if entities[x+test, y-test][0] in entities :
                    enemy_wolf.append((x+test, y-test))
                if entities[x+test, y-test][0] == ally :
                    allied_wolf.append((x+test, y-test))
        test += 1
    return enemy_wolf, allied_wolf

def move_wolves(Px):
    moves_orders = ""
    
    if Px == 1:
        ennemy = 2
    else:
        ennemy = 1
    #Flag representing if the werewolf has moved (1=yes, 0=no)
    nbr_flags = 0
    while nbr_flags != 7:
        #Get team of the player
        current_team = get_team(Px)
        for key in current_team:
            #Check if current wolf flag is set to 1
            if current_team[key][0] == 0:
                #If Not, check if empty space around
                current_empty_spaces = empty_places(key)
                if current_empty_spaces != []:
                    #If empty space around, move to ennemy alpha
                    Ealpha_pos = target_Ealpha(ennemy)
                    dir = direction(key, Ealpha_pos)
                    #Check if the move is possible
                    if dir in current_empty_spaces: #Cool, move, add the move to string
                        move_orders = ""+str(key[0])+"-"+str(key[1])+":@"+str(dir[0])+"-"+str(dir[1])+" "
                        current_team[key][0] = 1
                        nbr_flags += 1
                        print(nbr_flags, Ealpha_pos, dir, current_team)
                        

"""
===================
    GAME CYCLE
===================
    *************
    GENERIC TOOLS
    *************
"""

def hash(string):  # Spec 100 % and Code 100%
    """
	Description of the function
	---------------------------
    Properly split/hash one order in a list

    Args:
    -----
    string : one order - str

    Returns:
    --------
	list of list : hach_order = [order_type, origine, destination]
    order_type - str
    origine : [x,y] - list
    destination : [x,y] - list

	Version:
	--------
	Specification: Sébastien Baudoux(v.1.0 - 24/02/2022)
    Code: Sébastien Baudoux(v.2.0 - 24/02/2022)
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

def entity_at(entity_coords): # Spec 100 % and Code 100%
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
    entity_coords: Coordinates [x, y] - list

    Returns:
    --------
    [int, string, int]: list that contain team of entity, name of entity, energy - list

   	Version:
    --------
    Specification: Sébastien Baudoux(v.2.0 - 15/03/2022)
    Code: Sébastien Baudoux(v.2.0 - 09/03/2022)
    """
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2]]
    return False

def in_range(range, omega_coord):  # Spec 100 % and Code 100%
    """
   	Description of the function
    ---------------------------
    Check and count number of entity in range

    Args:
    -----
    ray : range around the entity - int
    ww_coords : Coordinates - [x, y] - list

    Returns:
    --------
    dict - entities in range

   	Version:
    --------
    Specification: Sébastien Baudoux(v.1.0 - 21/02/2022)
    Code: Sébastien Baudoux(v.1.0 - 21/02/2022)
    """
    nbr_entity = 0
    ww_in_range = {}
    key = []
    #print(omega_coord)
    for key, values in entities.items():
        #Test if entity is a werewolf
        if values[0] != 0:
            #print(omega_coord[0])
            x = abs((key[0]) - (omega_coord[0]))
            y = abs((key[1]) - (omega_coord[1]))
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
def pacify(rayon, omega, pacified_werewolves):  # Spec 100 % and Code 100%
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

    Raises
    ------
    IOError: Order gived not by a omega
    IOError: Omega not enough energy

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	Code : Sébastien Baudoux (v.1.0 - 24/02/2022)
	"""
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
        ...
        #print(" Not omega")
    return pacified_werewolves

def bonus(ww_coords):# Spec 0 % and Code 1000%
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
    bonus = 0
    team = entities[ww_coords][0]
    #Check allied werewolf at range 2
    wwat2 = in_range(2,ww_coords)
    if len(wwat2) != 0:
        for key in wwat2:
            # Si team ==
            if (wwat2[key][0] == team):
                bonus += 10
    #Check allied alpha at range 4
    alphaat4 = in_range(4,ww_coords)
    if len(alphaat4) != 0:
        for key in alphaat4:
            # Si team == and alpha
            if (alphaat4[key][0] == team) and (alphaat4[key][1] == "alpha"):
                bonus += 30
    #entities.update({list[1]: is_food})
    ww_coords_values = entities[ww_coords]
    ww_coords_values[3] = bonus
    entities.update({ww_coords:ww_coords_values})

def feed(list):  # Spec 100 % and Code 90%
    """
	Description of the function
	---------------------------
    Update ww energy if food in range and update food energy

    Args:
    -----
    list : list that contains ww_coords and entity_coords - type (list)

    Raises
    ------
    IOError: if there is no food at destination coordinates
    IOError: if energy werewolf is full

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 03/03/2022)
	code : Sébastien Baudoux (v.1.0 - 03/03/2022)
	"""
    is_ww = []
    is_food = []
    if list[0] in entities:
        is_ww = entities[list[0]]
    if list[1] in entities:
        is_food = entities[list[1]]
    else:
        ...
        #print(" This entity doesn't exist on boardgame.")
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
                #print(" Your werewolf energy is already at max.")
                ...
    else:
        #print(" This is not food.")
        ...

def fight(listat, pacified_werewolves, turn_without_damage):  # Spec 100 % and Code 90%
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
    # In case of no damages done
    turn_without_damage += 1
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
                    if defender[0] == 0:
                        ...
                        #print("You can't attack food.")
                    else:
                        defender = entities[listat[1]]
                        #(Energy + bonus)/10
                        attack_strength = ((attacker[2]+attacker[3])/10)
                        defender[2] = defender[2] - attack_strength
                        if defender[2] == 0:
                            if defender[1] == "omega":
                                defender[1] == "Human"
                            else:
                                defender[1] = "human"""
                        print(" "+str(defender[1]+" loose "+str(attack_strength) +
                                    ", his energy is now : "+str(defender[2]))+"")
                        entities.update({listat[1]: defender})
                        turn_without_damage = 0
                else:
                    ...
                    #print(" Nothing to attack there.")
    return turn_without_damage

def move(listmov):  # Spec 100 % and Code 100%
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
    #print(size)
    #Check if destination is not out of the boardgame.
    dest = listmov[1]
    if (dest[0] < size[0]) and (dest[1] < size[1]) and (dest[0] > 0) and (dest[1] > 0):
        #Check is the destination is empty
        if not (listmov[1] in entities):
            x = int(abs(listmov[1][0]-listmov[0][0]))
            #print(x)
            y = int(abs(listmov[1][1]-listmov[0][1]))
            #print(y)
            if x <= 1 and y <= 1:
                #print(" Move possible")
                for key, values in entities.items():
                    if key == listmov[0]:
                        val = values
                entities.update({listmov[1]: val})
                entities.pop(listmov[0])
            else:
                #print(" Move out of range")
                ...
        else:
            #print(" Can't move there, this space is not empty.")
            ...
    else:
        #print(" Can't move out of boardgame.")
        ...

"""
===================
    U.I. ENGINE
===================
"""
n = size[0]

def welcome_screen():  # Spec 100 % and Code 100%
    """
    Description of the function
    ---------------------------
    Just a welcome screen to display the game name and the team members name.
    
    Specification: Sébastien Baudoux(v.1.0 - 25/03/2022)
    Code: Sébastien Baudoux(v.1.0 - 25/03/2022)
    """
    with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        print(term.center(term.move_y(y_middle-5) +
              term.underline_bold_green((" *-* ALPHA & OMEGA *-*"))))
        print(term.move_y(y_middle-2) +
              term.center("--------------------").rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+1) +
              term.center('Press any key to start !').rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+8) + term.center("by group 20").rstrip())
        print(term.center(term.move_y(y_middle+10) + term.coral1(
            "William Auspert - Sébastien Baudoux - Aleksander Besler - Trésor Tientcheu").rstrip()))
        term.inkey()

def end_screen():  # Spec 100 % and Code 100%
    """
    Description of the function
    ---------------------------
    Just a end screen to display the game name and the team members name.

    Specification: Sébastien Baudoux(v.1.0 - 08/04/2022)
    Code: Sébastien Baudoux(v.1.0 - 25/03/2022)
    """
    with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        print(term.center(term.move_y(y_middle-8) +
                          term.underline_bold_green((" Thanks to have tried our game."))))
        print(term.center(term.move_y(y_middle-5) +
                          term.underline_bold_green((" *-* ALPHA & OMEGA *-*"))))
        print(term.move_y(y_middle-3) + term.center("by group 20").rstrip())
        print(term.move_y(y_middle-2) +
              term.center("--------------------").rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+1) +
              term.center('Press any key to exit !').rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+10) + term.center(
            "William Auspert - Sébastien Baudoux - Aleksander Besler - Trésor Tientcheu").rstrip())
        term.inkey()

def boardgame_manager(n):  # Spec 0 % and Code 100%
    """
	Description of the function
	---------------------------


    Uses:
    -----
    ...
	
    Args:
    -----

    Arg : Description - type
	
    Returns:
    --------

	type : Description
   
	Version:
	--------
	Specification : Author (v.1.0 - dd/mm/yyyy)
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""

    #make_board
    o = n+1
    myboard = [[' ..... ' for count in range(o)] for rows in range(o)]
    #updateboard
    r = n+1
    c = n+1
    #print (r,c)
    for i in range(r):
        for j in range(c):
            coords = (i, j)
            #print(coords)
            if (i == 0) and (j == 0):
                myboard[i][j] = " \ "
                ...
            elif (i == 0) and (j < c):
                if j < 10:
                    myboard[i][j] = " "+str(j)+""
                else:
                    myboard[i][j] = ""+str(j)+""
            elif (i < r) and (j == 0):
                if i < 10:
                    myboard[i][j] = " "+str(i)+" "
                else:
                    myboard[i][j] = ""+str(i)+" "
                ...
            elif (i == r) and (j == c):
                myboard[i][j] = " /  "
                ...
            elif coords in entities:
                picture_name = entities[coords][1]
                if (entities[coords][1] == "alpha") or (entities[coords][1] == "omega"):
                    if entities[coords][0] == 2:
                        picture = " "+term.white_on_salmon+str(pics[picture_name][0])+term.normal+""
                    else:
                        picture = ""+str(pics[picture_name][0])+" "
                else:
                    if entities[coords][0] == 2:
                        picture = term.white_on_salmon +pics[picture_name][0]+term.normal
                    else:
                        picture = pics[picture_name][0]
                myboard[i][j] = picture
            else:
                myboard[i][j] = ".."
                #myboard[i][j] = ""+str(coords)+""
    #print board
    for row in myboard:
        print('|'.join(row))
    print('')

"""
*************
GAME MANAGER
*************
"""
orders_P1 = ""
orders_P2 = ""

def get_orders(orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type):  # Spec 100 % and Code 100%
    """
	Description of the function
	---------------------------


    Uses:
    -----
    ...

    Args:
    -----

    Arg : Description - type

    Returns:
    --------

	type : Description

	Version:
	--------
	Specification : Author (v.1.0 - dd/mm/yyyy)
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""
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
        orders_P1 = input(
            print("Player 1, could you please enter your orders for this turn : "))
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
        orders_P2 = input(
            print("Player 2, could you please enter your orders for this turn : "))
    else:
        orders_P2 = DAI_orders_generator(2)
    # Notify player 1, if remote, with P2 orders
    if P1_game_mode == "remote":
        notify_remote_orders(connection, orders_P2)
    print("P1 orders : "+str(orders_P1)+"")
    print("P2 orders : "+str(orders_P2)+"")
    print(" * * * * * * * * * * * * * ")
    return (orders_P1, orders_P2)

def orders_manager(orders_P1, orders_P2, turn_without_damage):  # Spec 100 % and Code 100%
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
        #print("P1 - ☮ - pacify phase.")
        while len(pacify_P1) > 0:
            # Rajouter les arguments rayon et pacified_werewolfs
            pacify(3, pacify_P1[0], pacified_werewolves)
            pacify_P1.pop(0)
    # Check if Player 2 given pacify order and run it.
    if len(pacify_P2) > 0:
        #print("P2 - ☮ - pacify phase.")
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
    #print("P1 - 💪 - bonus phase.")
    for keys in team1:
        # Send to bonus function each werewolf from team 1 dictionnary
        #coords = keys
        bonus(keys)
    # --- bonuses(P2) ---
    #Make a team_P2 dictionnary that contains all alive werewolfs from player 2
    team2 = {}
    for key, values in entities.items():
        if values[0] == 2:
            #ajouter au dictionnaire team2
            team2.update({key: values})
    #print("P2 - 💪 - bonus phase.")
    for keys in team1:
        # Send to bonus function each werewolf from team 2 dictionnary
        #coords = keys
        bonus(keys)
    # ------------------
    # --- FEED PHASE ---
    # ------------------
    # Check if Player 1 given feeds orders and run them.
    if len(feeds_orders_P1) > 0:
        #print("P1 - 🍖 - feed phase.")
        while len(feeds_orders_P1) > 0:
            #print(feeds_orders_P1)
            feed(feeds_orders_P1[0][1:3])
            feeds_orders_P1.pop(0)
    # Check if Player 2 given feeds orders and run them.
    if len(feeds_orders_P2) > 0:
        #print("P2 - 🍖 - feed phase.")
        while len(feeds_orders_P2) > 0:
            feed(feeds_orders_P2[0][1:3])
            feeds_orders_P2.pop(0)
    # --------------------
    # --- ATTACK PHASE ---
    # --------------------
    #turn_without_damage
    # Check if Player 1 given attacks orders and run them.
    if len(attacks_orders_P1) > 0:
        #print("P1 - ⚔ - attack phase.")
        while len(attacks_orders_P1) > 0:
            fight(attacks_orders_P1[0][1:3], pacified_werewolves, turn_without_damage)
            attacks_orders_P1.pop(0)
    # Check if Player 2 given attacks orders and run them.
    elif len(attacks_orders_P2) > 0:
        #print("P2 - ⚔ - attack phase.")
        while len(attacks_orders_P2) > 0:
            fight(attacks_orders_P2[0][1:3],
                  pacified_werewolves, turn_without_damage)
            attacks_orders_P2.pop(0)
    else:
        turn_without_damage += 1
    # ------------------
    # --- MOVE PHASE ---
    # ------------------
    # Check if Player 1 given move orders and run them.
    if len(move_orders_P1) > 0:
        #print("P1 - 🏃 - move phase.")
        while len(move_orders_P1) > 0:
            move(move_orders_P1[0][1:3])
            move_orders_P1.pop(0)
    # Check if Player 2 given move orders and run them.
    if len(move_orders_P2) > 0:
        #print("P2 - 🏃 - move phase.")
        while len(move_orders_P2) > 0:
            move(move_orders_P2[0][1:3])
            move_orders_P2.pop(0)
    return turn_without_damage

def end_game(winner):
    with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        print(term.center(term.move_y(y_middle-5) + term.underline_bold_green((" GAME FINISHED"))))
        if winner == 1 or winner == 2:
            print(term.move_y(y_middle-3) + term.center("PLAYER   "+str(winner)+"  win the game").rstrip())
        else:
            print(term.move_y(y_middle-3) + term.center("Both alphas lives is 0 this turn.").rstrip())
            print(term.move_y(y_middle-2) + term.center("  IT'S  A  DRAW").rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+1) + term.center('Press any key to exit !').rstrip())
        term.inkey()
    end_screen()

def totlifePlayer(Px):
    totlife = 0
    for key in entities:
        if entities[key][0] == Px:
            totlife += entities[key][2]
    return totlife

def check_alphas_life(fin):
    # Get alpha1 and alpha2 life
    alpha_1_life = 100
    alpha_2_life = 90
    for key in entities:
        if (entities[key][0] == 1) and (entities[key][1] == "alpha"):
            alpha_1_life = entities[key][2]
            print("alpha_1_life = " + str(alpha_1_life))
        if (entities[key][0] == 2) and (entities[key][1] == "alpha"):
            alpha_2_life = entities[key][2]
            print("alpha_2_life = " + str(alpha_2_life))
    # Check max life between alphas and declare winner (end game cases 2 or 3)
    if fin == 1:
        if alpha_1_life > alpha_2_life:
            winner = 1
            return end_game(winner)
        elif alpha_1_life < alpha_2_life:
            winner = 2
            return end_game(winner)
        elif alpha_1_life == alpha_2_life:
            winner = 0
            return end_game(winner)
    # Check if one of the alphas is dead and declare winner (end game cases 1)
    else:
        if alpha_1_life == 0:
            winner = 2
            return end_game(winner)
        elif alpha_2_life == 0:
            winner = 1
            return end_game(winner)
        elif alpha_1_life == 0 and alpha_2_life == 0:
            winner = 0
            return end_game(winner)

def game_loop(game_turn, turn_without_damage, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type):  # Spec 100 % and Code 33%
    """
	Description of the function
	---------------------------
    Main function of the game.
    Get orders from players, increment game_turn.
    And call him itself until a endgame condition rise

    Args:
    -----
    game_turn : Number of the game turn - int

	Version:
	--------
	Specification: Sébastien Baudoux(v.2.0 - 07/03/2022)
    Code: Sébastien Baudoux(v.2.0 - 07/03/2022)
	"""
    # End game cases
    # 1 - Check alphas life
    fin = 0
    check_alphas_life(fin)
    # 2- Check number of turns with no damage done
    if turn_without_damage == 200:
        fin = 1
        return check_alphas_life(fin)
    # (3) Check game turn - ONLY FOR TESTING PURPOSE
    if game_turn == 201:
        fin = 1
        return check_alphas_life(fin)
    else:
        # Main game loop
        with term.cbreak():
            print(term.home + term.clear + term.hide_cursor)
            print("   | - * - * - * -   GAME TURN : " +
                str(game_turn)+"  - * - * - * - | ")
            print("   |   "+g_set_pics[P1_game_mode]+" - Player 1 - " + g_set_pics[P1_type] +
                "  ||  "+g_set_pics[P2_game_mode]+" - Player 2 - " + g_set_pics[P2_type]+"   |")
            l1 = (totlifePlayer(1)/beginlifeP1)*100
            l2 = (totlifePlayer(2)/beginlifeP2)*100
            txt = "   |    ❤    :  {:.2f} %   ||   ❤    :  {:.2f} %     | "
            print(txt.format(l1, l2))
            # Print turn_without_damage
            print("   | - * - TURN WITHOUT DAMAGE : " +str(turn_without_damage)+"  - * - | ")
            print(" ----------------------------------  ")
            boardgame_manager(n)
            # Ask for orders and send them to the orders_manager
            orders_P1, orders_P2 = get_orders(
                orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)
            orders_manager(orders_P1, orders_P2, turn_without_damage)
            game_turn += 1
            print("Press any key for next turn...")
            term.inkey()
            game_loop(game_turn, turn_without_damage, orders_P1,
                      orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)

def settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):
    # Display settings menu
    with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        print(term.move_y(y_middle-4) +
            term.center(" * 🎮 * Default game settings * 🎮 *").rstrip())
        #print(term.move_y(y_middle-3) +term.center("-------------------------------------").rstrip())
        print(term.move_y(y_middle) +
            term.center("       Player 1       ||          Player 2  ").rstrip())
        print(term.move_y(y_middle+2) +
              term.center(" "+P1_game_mode+" - " +g_set_pics[P1_game_mode]+" - "+P1_type+" "+g_set_pics[P1_type]+"   ||  "+P2_game_mode+" - "+g_set_pics[P2_game_mode]+" - "+P2_type+" "+g_set_pics[P2_type]+"").rstrip())
        print(term.move_y(y_middle+3) +
              term.center("Default map path : "+str(path)+"").rstrip())
        print(term.move_y(y_middle+6) +
            term.center("Would you like to change it ?").rstrip())
        print(term.move_y(y_middle+7) +
            term.center(("Press y(es) or n(o)")).rstrip())
        with term.cbreak():
            val = ''
            blink = 0
            val = term.inkey(timeout=3)
            while val.lower() != 'y' or val.lower() != 'n':
                val = term.inkey(timeout=0.5)
                if blink ==1:
                    print(term.center (term.move_y(y_middle+8) + term.underline_bold_green(("Please press 'y' or 'n' "))))
                    #val = term.inkey(timeout=0.5)
                    blink -= 1
                else:
                    print(term.move_y(y_middle+7) + term.clear_eos)
                    #val = term.inkey(timeout=0.5)
                    blink += 1
                if val.lower() == 'y':
                    print(f"{term.home}{term.clear}")
                    path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type = game_settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
                    settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
                elif val.lower() == 'n':
                    return game_loop(game_turn, turn_without_damage, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)

# First screen
welcome_screen()
# Display game settings
settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)

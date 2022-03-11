#-*- coding: utf-8 -*-
import blessed, math, os, time
term = blessed.Terminal()
"""
EXPLANATIONS
~~~~~~~~~~~~
For a better comprehension of this file we've made an index.
Each section and functions are referenced with the line number.

Index
------
INITIALIZE
    - game_mode
    - data_import
    - Remote connection
    - Play game
U.I.
    - boardgame manager
GAME CYCLE
    - GENERIC TOOLS
        - game loop
        - hash
        - in_range
        - at_range
        - entity_at
        - finish
    - ORDER MANAGER
    - GAME FUNCTIONS
        - pacify
        - bonus
        - feed
        - fight
        - move
I.A.


-------------------------
Glossary
--------
Px = Player x
group_x = Group number of player x
Px_game_mode = Local or remote game mode of player x
Px_type = Is player x is human or I.A.
ww = werewolf
E = energy
******************************
"""
# TESTER SI ENTITES A PORTEE POUR FEED AND FIGHT
"""
========================================
            INITIALIZE
=======================================
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
def game_settings():
    """
	Description of the function
	---------------------------
    Function that ask with inputs to select all the game settings.

    Returns:
    --------
    ["P1", group_1, P1_game_mode, P1_type, "P2", group_2, P2_game_mode, P2_type]
	type : Description

	Version:
	--------
	Specification : Author (v.1.0 - dd/mm/yyyy)
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""
    # Selection player 1
    # ------------------
    #Local OR Remote
    P1_game_mode = int(
        input('Select game mode for player 1 => 0 (Local) OR 1 (Remote) : '))
    # If Remote ask for group number
    if P1_game_mode == 1:
        P1_game_mode = "remote"
        group_1 = int(input("Please enter the group number for player 1 : "))
    else:
        P1_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    P1_type = int(
        input("Select game type for player 1 => 0 (Human) OR 1 (I.A.) : "))
    if P1_type == 1:
        P1_type = "I.A."
    else:
        P1_type = "Human"
    # ------------------
    # Selection player 2
    # ------------------
    #Local OR Remote
    P2_game_mode = int(
        input("Select game mode for player 2 => 0 (Local) OR 1 (Remote) : "))
    # If Remote ask for group number
    if P2_game_mode == 1:
        P2_game_mode = "remote"
        group_2 = int(input("Please enter the group number for player 2 : "))
    else:
        P2_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    P2_type = int(
        input("Select game type for player 2 => 0 (Human) OR 1 (I.A.) : "))
    if P2_type == 1:
        P2_type = "I.A."
    else:
        P2_type = "Human"

    # P1 from group number on local/remote and it's a human/IA
    print(f"Player 1 from group : {group_1} on {P1_game_mode} and it's a {P1_type}.")
    # P2 from group number on local/remote and it's a human/IA
    print(f"Player 2 is from group : {group_2} on {P2_game_mode} and it's a {P2_type}.")

    return ["P1", group_1, P1_game_mode, P1_type, "P2", group_2, P2_game_mode, P2_type]
#print(game_settings())

# Sortir et mettre comme arguments size et entitties
def data_import():
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
    # Ask for ano file path
    path = input("Please give the path to the .ano file : ")
    # Tuple for map size
    size = ()
    # A unique dictionnary to rules them all
    entities = {}
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
                size = (int(si[0]), int(si[1]))
                continue
            j = i.split()
            # Check if line contain werewolf info or not
            if (j[3] == "alpha") or (j[3] == "omega") or (j[3] == "normal"):
                x = int(j[1])
                y = int(j[2])
                values = [int(j[0]), (j[3]), 100]
                entities.update({(x, y): values})
            else:
                x = int(j[0])
                y = int(j[1])
                # Add "0" as first list value element for food to make the "food team" identified with 0
                values = [0, (j[2]), int((j[3]))]
                entities.update({(x, y): values})
    print("Map Size : ", size)
    print("Entities :", entities)

data_import()

# create connection, if necessary
def connection():
    if P1_game_mode == 'remote':
        connection = create_connection(group_2, group_1)
    elif P2_game_mode == 'remote':
        connection = create_connection(group_1, group_2)


def play_game(map_path, group_1, type_1, group_2, type_2):
    """Play a game.

    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)

    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    If there is an external referee, set group id to 0 for remote player.
    """

"""
Mode_selection
	Input : mode selection
	Local
		Human VS Human
		Human VS I.A.
		I.A. VS I.A.
	Lan
		Human VS Human
		Human VS I.A.
		I.A. VS I.A.
"""
game_turn = 0

"""
=======================================================
                    U.I. ENGINE
=======================================================
"""
def boardgame_manager()
    ...

    """
==========================================================
                    GAME CYCLE
========================================================
"""
# Input : Orders P1 & P2
# Get orders of player 1 and notify them to player 2, if necessary
def get_orders():
    if P1_game_mode == 'remote':
        orders = get_remote_orders(connection)
    else:
        orders = get_AI_orders(..., 1)
        if P2_game_mode == 'remote':
            notify_remote_orders(connection, orders)

        # get orders of player 2 and notify them to player 1, if necessary
        if P2_game_mode == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(..., 2)
            if P1_game_mode == 'remote':
                notify_remote_orders(connection, orders)


"""
=================================
        A.I. ENGINE
=================================
def_orders_generator():
"""

    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':

        close_connection(connection)

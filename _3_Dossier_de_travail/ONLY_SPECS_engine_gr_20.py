#-*- coding: utf-8 -*-
import blessed
import math
import os
import time
import random
from remote_play import *
term = blessed.Terminal()

"""
EXPLANATIONS
~~~~~~~~~~~~
For a better comprehension of this file we've made an index.
Each section and functions are referenced with the line number.

Index
------
GLOBAL AND INITIALIZATION FUNCTIONS - line 56
    - def game_settings() - line 85 - # S 100%/ C 100%
    - def data_import() - line 146 - # S 100%/ C 100%
    - connection - line 198
    - def close_connection() - line 205 - # S 0%/ C 100%
A.I. - line 231
    - def DAI_orders_generator() - line 226 - # S 100%/ C 100%
    - def SAI_orders_generator() - # S 0%/ C 0%
GAME CYCLE - line 280
    - GENERIC TOOLS - line 283
        - def game_loop() - line 286 - # S 100%/ C 33%
        - def hash() - line 315 - # S 100%/ C 100%
        - def entity_at() - line 358 - # S 100%/ C 100%
        - def in_range() - line 389 - # S 100%/ C 100%
        - def at_range() - line 424 - # S 0%/ C 0%
        - def finish() - line  - # S 0%/ C 0%
    - GAME FUNCTIONS - line 462
        - def pacify() - line 466 - # S 100%/ C 100%
        - def bonus() - line 511 - # S 0%/ C 0%
        - def feed() - line 539 - # S 100%/ C 90%
        - def fight() - line 601 - # S 100%/ C 90%
        - def move() - line 642 - # S 100%/ C 100%
    - ORDER MANAGER - line 686
        - def get_orders() - line 692 - # S 100%/ C 100%
        - def orders_manager() - line 744 - # S 100%/ C 100%
U.I. - line 909
    - def boardgame_manager() - line 910 - # S 0%/ C 0%

-------------------------
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
******************************
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

#Next two dictionnaries are used to assign UTF-8 "pictures" with keywords
pics = {"alpha": "α", "omega": "Ω", "normal": "🐺", "human": "👤",
        "berries": "🍒", "apples": "🍎", "mice": "🐁", "rabbits": "🐇", "deers": "🦌"}
g_set_pics = {"Human": "👤", "A.I.": "🤖",
              "local": "💻", "remote": "🖧", }

def game_settings(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):  # Spec and Code 100%
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

def data_import(size, entities):  # Spec and Code 100%
    """
	Description
	---------------------------
    Update the size tuple and the entities dictionary with data in a ano file.

    Args:
    -----
    size : Tuple with 2 elements, raw number and column number - tuple
    entities : Dictionnary that contains all elements on the boardgame - dict

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 11/03/2022)
	Code : Sébastien Baudoux (v.2.0 - 10/03/2022)
	"""

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

"""
===================
    A.I. ENGINE
===================
"""
# DUMB A.I.
def DAI_orders_generator(Px):  # Spec 100 % and Code 100%
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

# SMART A.I.
def SAI_orders_generator(Px):  # Spec 0 % and Code 0%
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

def entity_at(entity_coords):  # Spec 100 % and Code 100%
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

"""
**************
GAME FUNCTIONS
**************
"""
# TESTER SI ENTITES A PORTEE POUR FEED AND FIGHT
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

def fight(listat, pacified_werewolves):  # Spec 100 % and Code 90%
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

"""
===================
    U.I. ENGINE
===================
"""
def boardgame_manager():  # Spec 0 % and Code 0%
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

def make_board(n):

def print_board(board):

def updateboard(myboard):

def test():

"""
*****************
ORDERS MANAGEMENT
*****************
"""

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

def orders_manager(orders_P1, orders_P2):  # Spec 100 % and Code 100%
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

def stop():
    print("FIN")

def startlifePlayer(Px):
    ...

def totlifePlayer(Px):
    ...

def game_loop(game_turn, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type):  # Spec 100 % and Code 33%
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
    # Vérifie l'E des Alphas
    #alpha_1_life, alpha_2_life = check_alpha_life()
    """if alpha_1_life == 0:
        print("Player 2 win the Game.")
    elif alpha_2_life == 0:
        print("Player 1 win the Game.")
    elif alpha_1_life == 0 and alpha_2_life == 0:
        print("Both alpha life is 0 this turn - DRAW")"""
    # Vérifier numéro de tour ==> Règles à vérifier
    ...


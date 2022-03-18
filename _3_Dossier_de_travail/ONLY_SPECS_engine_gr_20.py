#-*- coding: utf-8 -*-
import blessed, math, os, time
term = blessed.Terminal()
"""

========================================
            GENERIC TOOLS
=======================================
"""
def is_entity_at((x,y)):
    # indiquer un nom de liste
    """ Check if there is an entity at given position

    Uses:
    -----
    1) To populate the map
    2) To permit or not the feed
    3) To permit or not the attack
    4) To permit or not a move

    Args:
    -----

    (x,y): Coordinates where we check if an entity exist (list)

    Returns:
    --------
    list (bool, type of entity)

   	Version:
	--------
	specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)

    """
def is_in_range(ray,(x,y)):
    """
    Check and count number of entity in range

    Args:
        ray : range around the entity (int)
        (x,y) : position of the central entity (list)

    Returns:

   	Version:
	--------
	specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)

    """

# main function
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
"""
def game_mode():
    # a fusionner avec play_game
    """Game Mode selection


	Input : mode selection
	Local
		Human VS Human
		Human VS I.A.
		I.A. VS I.A.
	Lan
		Human VS Human
		Human VS I.A.
		I.A. VS I.A.


    Parameters
    ----------


    Notes
    -----

    """

    # create connection, if necessary
def connection():
    	"""Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""
    if type_1 == 'remote':
        connection = create_connection(group_2, group_1)
    elif type_2 == 'remote':
        connection = create_connection(group_1, group_2)

    """
=======================================================
                    U.I. ENGINE
=======================================================

	map creator
		def_game_mode_selection_displayer
	HUD manager
		def_display_logs
		def_update_players_totallife
		def_turn_updater
	map_updater
		def_remove_death_entities
    """

def myfunction(...):
	"""Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""


while ...:


    """
==========================================================
                    INPUT ORDERS CYCLE
========================================================
    """
	#Input : Orders Team1 & Team2

       # get orders of player 1 and notify them to player 2, if necessary
    def get_orders():
       	"""Description of the function


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
        specification : Author (v.1.0 - dd/mm/yyyy)
        code : Author (v.1.0 - dd/mm/yyyy)

        """

#orders_engine

#def_orders_cleaner
def netcut(strg):
    """Description of the function

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
	specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)

    """

#clean_orders = netcut(orders)
#print(clean_orders)

#def_orders_manager
def checkorders(liste):
    """Description of the function


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
	specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)

    """

"""
==========================================================
                    GAMERULES CYCLE
========================================================
    """

def pacifier():
    """Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""

#fct_bonuses
    def bonus((x,y)):
        """AI is creating summary for bonus
        """


#fct feeder
    def feed(loup(coords, E), food(coords, E):
    """Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""


def fight():
	"""Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""

def being_human():
    """Description of the function


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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""

def move((r1,c1),(r2,c2)):
    """
    Move a werewolf

        Parameters
        ----------
        start_coord : Origin coordinates (list)
        dest_coord : Destination coordinates (list)

        Returns
        -------
        Nothing

        Raises
        ------
        IOError: if there is no werewolf at origin coordinates
        IOError: if the destinations coordinates are further than 1
        IOError: if the destinations coordinates are occupied by an entity
    """


"""
    =================================
                    A.I. ENGINE
    =================================
"""
def orders_generator():
    """Description of the function


    Uses:
    -----
    ...

    Args:
    -----

    Arg: Description - type

    Returns:
    --------

    type: Description

    Version:
    --------
    specification: Author(v.1.0 - dd/mm/yyyy)
    code: Author(v.1.0 - dd/mm/yyyy)

    """




    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':

        close_connection(connection)



def pacification(is_in_range,wolf_energy ,entity_at):
    # Il n'est pas nécessaire d'avoir l'énergie  ;)
    
    """to pacify the enermy.
    parameters
    ----------
    is_in_range:the number of entity around (str)
    wolf_energy : the energy of the omega(int)
    entity_at:the type of entity in the range (str)
    Returns
    --------
    result : stops the enemy from attacking and reduces the omega energy(int)
    Version:
	--------
	specification : Author (v.1.0 - dd/mm/yyyy)
    """
        ...

#fct_bonuses
    def bonus(loup(coords, E),food):
            # Il ne faut pas la fct food mais bien is_in_range  ;)
        """tells us the bonus gain.
        parameters
        ----------
        loup(coords,E: the position the entity(int)
        food: the type of food(str)
        returns
        -------
        result : energy increase(int)
        Version:
	    --------
	    specification : Author (v.1.0 - dd/mm/yyyy)
        """
        #####
    def fight(wolf_energy ,is_in_range,bonus):
           """combat each other.
        parameters:
        ----------
        is_in_range :the number of entity around (str)

        wolf_energy  : the energy of wolf(int)
        bonus : the gain point of wolf(int)

        Returns:
        --------
        result : reduces wolf energy

        type : Description

        Version:
        --------
        specification : Author (v.1.0 - dd/mm/yyyy)
        """

    def being_human(wolf_energy):
        """ turns to human form.
        parameters
        ----------
        wolf_energy : the energy of wolf(int)
        Returns:
        --------
        result : reduces wolf energy

        Version:
        --------
        specification : Author (v.1.0 - dd/mm/yyyy)
        """
    def wolf_energy(energy=100):
        """ the wolfs energy.
        parameters
        ----------
        energy: the energy of wolf (int; default :100)
        Returns:
        --------
        result : reduces wolf energy

        Version:
        --------
        specification : Author (v.1.0 - dd/mm/yyyy)
        
       """

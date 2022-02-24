#-*- coding: utf-8 -*-
import blessed, math, os, time

"""
Index
------
- Generic Tools
    - is_entity_at
    - range
- Game Functions
    - pacify
    - bonus
    - feed
    - attack
    - move
-------------------------
-------------------------
Glossary
--------
ww = werewolf = loup-garou

"""

"""
========================================
            GENERIC TOOLS
=======================================
"""


def is_entity_at(ww_coords):
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

    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
    list (bool, type of entity)

   	Version:
	--------
	specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
    """

def range(ray,(x,y)):
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

"""
==========================================================
                    GAMERULES CYCLE
========================================================
    """
def pacify():
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

def bonus((x,y)):
        """AI is creating summary for bonus
        """


def feed(loup(coords, E), food(coords, E):
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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""


    def fight(ww_coords_1, ww_coords_2):
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
	specification : Author (v.1.0 - dd/mm/yyyy)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""

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
	specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)

	"""

    def move(start_coord, dest_coord):
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
	Code : Author (v.1.0 - dd/mm/yyyy)

    """

"""
Fonctions créés par Trésor 

"""
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

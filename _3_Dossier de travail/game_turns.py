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






    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':

        close_connection(connection)


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

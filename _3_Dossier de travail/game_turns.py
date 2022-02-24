#-*- coding: utf-8 -*-
"""
Index
------
- Generic Tools
    - entity_at
    - range
    - energy
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

========================================
            GENERIC TOOLS
=======================================
"""
def entity_at(ww_coords):
    # indiquer un nom de liste
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
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
    boolean

   	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
    """

def range(ray, ww_coords):
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

def energy(ww_coords):
	"""
	Description of the function
	---------------------------
    Return the energy of the werewolf at given position

    Uses:
    -----
    - For Omega to launch pacify
    - After an attack
        => If Alpha E == 0 ==> Game finished
        => If E of a ww ==0 ==> being-human

    Args:
    -----
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	int : energy of the werewolf

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 21/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

"""
==========================================================
                    GAMERULES CYCLE
========================================================
    """

def pacify(ww_coords):
    """
	Description of the function
	---------------------------
    Launch "Pacify" on all arounds and in range werewolf
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

def feed(ww_coords):
    """
	Description of the function
	---------------------------
    Update/Upgrade ww energy if food in range

    Args:
    -----
    ww_coords : Coordinates - (x, y) - type (list)

    Returns:
    --------
	type : Description

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
	code : Author (v.1.0 - dd/mm/yyyy)
	"""

def fight(ww_coords_Attack, ww_coords_Defend):
	"""
	Description of the function
	---------------------------
    Make damage to ww2 from ww1
    ** Reminder
    * Strenght = E/10 (rounded nearest)

    Args:
    -----
    ww_coords_Attack : Coordinates of the attacker - (x, y) - type (list)
    ww_coords_Defend : Coordinates of the defender -  (x, y) - type (list)

    Returns:
    --------
	Nothing or just a log message.

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
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
	Specification : Sébastien Baudoux (v.1.0 - 24/02/2022)
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
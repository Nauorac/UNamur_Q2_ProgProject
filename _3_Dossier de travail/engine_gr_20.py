#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

# other functions
"""
========================================
            GENERIC TOOLS
=======================================
"""
def is_entity_at((x,y)):

def is_in_range(ray,(x,y)):

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


    # create connection, if necessary
def connection():
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


while ...:


    """
==========================================================
                    INPUT ORDERS CYCLE
========================================================
    """
	#Input : Orders Team1 & Team2

       # get orders of player 1 and notify them to player 2, if necessary
    def get_orders():
        if type_1 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(..., 1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)

            # get orders of player 2 and notify them to player 1, if necessary
            if type_2 == 'remote':
                orders = get_remote_orders(connection)
            else:
                orders = get_AI_orders(..., 2)
                if type_1 == 'remote':
                    notify_remote_orders(connection, orders)



		#orders_engine

			#def_orders_cleaner
            def netcut(strg):
                #Retirer les espaces
                netorders=orders.strip()
                print(netorders)
                #Split dans une liste
                cutorders=orders.split()
                return cutorders

            #clean_orders = netcut(orders)
            #print(clean_orders)

			#def_orders_manager
            def checkorders(liste):
                i=0
                nbrordes=0
                move_order=0
                attack_order=0
                feed_order=0
                while i < len(liste):
                    if ((len(liste[i])) < 12):
                        print("The order num "+str(i+1)+" is invalid")
                    else:
                        nbrordes += 1
                        # Reconvertir les elmts de la liste en string pour profiter des méthodes sur les string
                        current_order=liste[i]
                        if (current_order[6])=="@":
                            move_order+=1
                        elif (current_order[6]) == "<":
                            feed_order += 1
                        elif (current_order[6]) == "*":
                            attack_order += 1
                        else:
                            print("Et un ordre de pacification.")
                    i += 1
                #print("Il y a "+str(nbrordes)+" orders encode(s)")
                #print(" - "+str(move_order)+" de deplacement.")
                #print(" - "+str(feed_order)+" de nourrissage.")
                #print(" - "+str(attack_order)+" d'attaque.")

    """
==========================================================
                    GAMERULES CYCLE
========================================================
    """

    def pacifier():
        ...

#fct_bonuses
    def bonus(loup(coords, E)):
        check nbr-ami rayon 2
        + 10 * nbr_ami
        check alpha rayon 4

#fct feeder
    def feed(loup(coords, E), food(coords, E):

        return loup(coords, E), food(coords, E)

def fighter():
    ...

def being_human():
    ...

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

    def_orders_generator():

"""

    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':

        close_connection(connection)

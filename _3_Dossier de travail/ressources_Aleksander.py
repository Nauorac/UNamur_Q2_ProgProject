def load_map(maplink):
    """Creates a map / Shows the map to the players by using the information that are containted in the cpx file.
    
    Parameters
    ----------
    map_link: file that will contain the map info (file)

    Notes
    -----
	map_link should be a .txt file

    Returns
    -------
    map: the map (dict)

    Version 
	−−−−−−−
	specification : Aleksander Besler (v.1 17/02/22)
    """ 

def map_update({map}, {map_size}, {wolf}):
    """Updates the map to the current state of the game.
    
    Parameters
    ----------
    map: the map (dict)
    map_size: size of the map (dict)
    wolf: data concerning the werewolves (dict)

    Notes
    -----

    Returns
    -------
    map: the map (dict)

    Version 
	−−−−−−−
	specification : Aleksander Besler (v.1 17/02/22)
    """ 

def move({map}, {wolf}, turn):
    """This function allows the player to move his werewolves when it's his turn.
    
    Parameters
    ----------
    map: the map (dict)
    wolf: data concerning the werewolves (dict)
    turn:  Tells wich player has his turn now(int)
    
    Notes
    -----
    - Will call turn 
    - Will call map_update

    Returns
    -------
    map: the map (dict)
    wolf: data concerning the werewolves (dict)

    Version 
	−−−−−−−
	specification : Aleksander Besler (v.1 17/02/22)

    """

def start_game(maplink, player2type):

    """ This function starts the game.
    Parameters
    -------------
    maplink : link to the map file: (str)
    player2type: 0 if it's a human and 1 if it's a AI (bool)

    Returns
    --------
    turn_count: Counts how many turn has been taken(int)
    player_turn: wich player currently has his turn (int)       

    Notes 
    -------
    This function starts the game

    Version
    -------
    specification : Aleksander Besler (v.1 17/02/22)

    """

def victory({map}, turn count):
    """Checks if all the necessary winning conditions are checked if yes then starts the win procedure.
    
    Parameters
    ----------
	map: the map (dict)
    turn_count: Counts how many turn has been taken(int)

    Notes
    -----
    
    Returns
    -------
    game_over:  State of the game(bool)

    Version
    -------
    specification : Aleksander Besler (v.1 17/02/22)

    """

def distance_calculator (target_1, target_2):
    """The fonction calculates the distance between 2 targets"
    
    Parameters
    ----------
    target_1 : The position of the players wolf (int)
    target_2 : The position of the enemies wolf (int)

    Returns
    -------
    distance: Returns the distance between the chosen targets (int)

    Version
    -------
    specification : Aleksander Besler (v.1 17/02/22)

    """

def energy ({wolf}):
    """checks how much energy the wolf has left"
    
    Parameters
    ----------
    wolf: data concerning the werewolves (dict)

    Returns
    -------
    energy_result: Returns the energy the werwolve has left (int)

    Version
    -------
    specification : Aleksander Besler (v.1 19/02/22)

    """

def recharge ({wolf}, {food}):
    """Makes the werevolve eat the food next to him making him recharge his energy"
    
    Parameters
    ----------
    wolf: data concerning the werewolves (dict)
    food : data concerning the food present on the map (dict)

    Returns
    -------
    energy: Returns the energy the werewolve has left (int)

    Version
    -------
    specification : Aleksander Besler (v.1 19/02/22)

    """

def order ( turn_count, player_turn ):
    """Keeps the order in wich the players play in order"
    
    Parameters
    ----------
    turn_count: Counts how many turn has been taken(int)
    player_turn: wich player currently has his turn (int)

    Returns
    -------
    energy: Returns the energy the werewolve has left (int)

    Version
    -------
    specification : Aleksander Besler (v.1 19/02/22)

    """

def end_turn ( player, player_turn ):
    """Ends the turn of the curent player"
    
    Parameters
    ----------
    player: the player that currently plays (str)

    Returns
    -------
    player_turn: wich player currently has his turn (int)

    Version
    -------
    specification : Aleksander Besler (v.1 19/02/22)

    """

def attack (target_1, target_2):
    """This function wil make the first target attack the second one 
    after checking if all prenecessary parameters where accomplished"
    
    Parameters
    ----------
    target_1 : The position of the players wolf (int)
    target_2 : The position of the enemies wolf (int)

    Returns
    -------
    wolf: data concerning the werewolves (dict)
    succesful: returns 1 if the attack was a succes and 0 if it couldn't happen (bool)

    Version
    -------
    specification : Aleksander Besler (v.1 21/02/22)

    """

def bonus ({wolf}, target):
    """This function will check if the werwolve has the bonus granted from the "Alpha" werwolve
    and if so will grant the bonus.
    
    Parameters
    ----------
    wolf: data concerning the werewolves (dict)    
    target : The position of the targeted wolf (str)

    Returns
    -------
    bonus: Returns 1 if the bonus is granted and 0 if it isn't (bool)

    Version
    -------
    specification : Aleksander Besler (v.1 21/02/22)

    """

def map_check ({map}):
    """This function will check if the map was loaded properly.
    
    Parameters
    ----------
    map: the map (dict)

    Returns
    -------
    load: Returns 1 if the map was loaded properly and 0 if it wasn't (bool)

    Version
    -------
    specification : Aleksander Besler (v.1 21/02/22)

    """
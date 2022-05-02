def ww_danger(ww_pos):  # Alesk
    """
	Description of the function
	---------------------------
    Ckeck if there is any danger around the wolf

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
    else:
        team = 1
    # Indicates wich team has to be attacked
    danger_spaces = []
    if x - 1 > 0 and x + 1 < 21:
        # Checks if the target is in boarder
        if (x+1, y) in entities:
            # Checks if the target exists
            if entities[x+1, y][0] == team:
                # Verifies if the target is of the opposing team
                danger_spaces.append((x+1, y))
                # Puts the target in the danger list
        if (x-1, y) in entities:
            if entities[x-1, y][0] == team:
                danger_spaces.append((x-1, y))
    if y - 1 > 0 and y + 1 < 21:
        if (x, y-1) in entities:
            if entities[x, y-1][0] == team:
                danger_spaces.append((x, y-1))
        if (x, y+1) in entities:
            if entities[x, y+1][0] == team:
                danger_spaces.append((x, y+1))
    if y - 1 > 0 and y + 1 < 21 and x - 1 > 0 and x + 1 < 21:
        if (x+1, y+1) in entities:
            if entities[x+1, y+1][0] == team:
                danger_spaces.append((x+1, y+1))
        if (x-1, y+1) in entities:
            if entities[x-1, y+1][0] == team:
                danger_spaces.append((x-1, y+1))
        if (x-1, y-1) in entities:
            if entities[x-1, y-1][0] == team:
                danger_spaces.append((x-1, y-1))
        if (x+1, y-1) == team:
            if entities[x+1, y-1][0] in entities:
                danger_spaces.append((x+1, y-1))
    return danger_spaces

def lowest_health(danger_spaces): # Alesk
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
    count = get_number_of_elements(danger_spaces)
    # Counts number of entities in a list
    danger1 = entities[danger_spaces[0]]
    lowhealth = danger1[2]
    lowhealthwolf = danger_spaces[0]
    # Puts the first wolf as the lowest health one to have a base to compare on
    for i in range(count):
        if lowhealth > danger1[2]:
            # Compares each wolfs health and takes the one with the lowest health
            lowhealth = danger1[2]
            lowhealthwolf = danger_spaces[i]
    return lowhealthwolf

def get_number_of_elements(list): # Alesk
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

def distance(position_x1, position_y1, position_x2, position_y2):  # Trésor
    if abs(position_x2 - position_x1) > abs(position_y2-position_y1):
        return abs(position_x2-position_x1)
    else:
        return abs(position_y2-position_y1)

def move_wolves(Px):  # Alesk
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
                    if dir in current_empty_spaces:  # Cool, move, add the move to string
                        move_orders = "" + \
                            str(key[0])+"-"+str(key[1])+":@" + \
                            str(dir[0])+"-"+str(dir[1])+" "
                        current_team[key][0] = 1
                        nbr_flags += 1
                        print(nbr_flags, Ealpha_pos, dir, current_team)

"""
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
"""
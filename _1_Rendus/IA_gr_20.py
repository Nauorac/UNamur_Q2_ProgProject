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




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
    # for each ww from Playerx in entities
    # get position and add to str
    AI_orders = ""
    for key, values in entities.items():
        if values[0] == Px:
            orig = key
            AI_orders = AI_orders + str(orig[0]) + "-" + str(orig[1]) + ":"
            #rand an order and add to str
            order_type = random.choice(["@", "*", "<", "pacify "])
            AI_orders = AI_orders + order_type
            # for x
            if order_type == "pacify ":
                #print(AI_orders)
                ...
            else:
                dest = [0, 0]
                stepx = random.choice([+1, -1, 0])
                dest[0] = orig[0] + stepx
                stepy = random.choice([+1, -1, 0])
                dest[1] = orig[1] + stepy
                AI_orders = AI_orders + str(dest[0]) + "-" + str(dest[1]) + " "
    #print(AI_orders)
    return AI_orders

# -------------------------------------------------------
# SMART A.I.
# PART 1
# Multiple usefull functions
# PART 2
# Final actions functions for each type of werewolf/human
# -------------------------------------------------------
# PART 1


# Next 2 dictionnaires are used to store cardinal directions and their coordinates modificators
going_to = {"N": [-1, 0], "NE": [-1, +1], "E": [0, +1], "SE": [+1, +1],
            "S": [+1, 0], "SW": [+1, -1], "W": [0, -1], "NW": [-1, -1]}

alt_dir = {"N": ["NW", "NE"], "S": ["SW", "SE"], "E": ["NE", "SE"], "W": [
    "NW", "SW"], "NE": ["N", "E"], "SE": ["S", "E"], "NW": ["N", "W"], "SW": ["S", "W"]}

def get_team(Px):  # Alesk - OK
    team = {}
    for cle in entities:
        if entities[cle][0] == Px:
            team[cle] = entities[cle]
    return team

def looking_for_food(ww_pos):  # Seb - OK
    # Use in_range function to find food
    food_pos = ()
    i = 1
    while food_pos == () and i < 21:
        entities_in_range = in_range(i, ww_pos)
        for entity in entities_in_range:
            if entities[entity][0] == 0:
                food_pos = entity
            else:
                i += 1
    return food_pos

def empty_places(ww_pos):  # Alesk - OK
    empty_cases = []
    for key in going_to:
        x = ww_pos[0] + going_to[key][0]
        y = ww_pos[1] + going_to[key][1]
        if (x, y) not in entities:
            empty_cases.append((x, y))
    return empty_cases

def ennemies_in_range(ww_pos):  # Alesk/Seb
    entities_at_range = in_range(1, ww_pos)
    ennemies_in_range = []
    for entity in entities_at_range:
        if entities[entity][0] != entities[ww_pos][0] and entities[entity][0] != 0:
            ennemies_in_range.append(entity)
    return ennemies_in_range

def lowest_health(ww_pos):  # Alesk/Seb
    """
    Description of the function
    ---------------------------
    Ckecks wich wolf has the lowest health from the dangerous spaces list
    This function is used to check if the wolf is in the same line as the player
    and if he is, it will move to the next line

    Args:
    -----
    danger_spaces : list of units that are from the opposing team - list

    Returns:
    --------
    lowhealthwolf : Coordinates of the lowest health wolf found - str
    """
    ennemies = ennemies_in_range(1, ww_pos)
    lowenemy = entities[ennemies[0]]
    lowhealth = lowenemy[2]
    lowhealthwolf = ennemies[0]
    for i in range(len(ennemies)):
        if lowhealth > entities[ennemies[i]][2]:
            lowhealth = entities[ennemies[i]][2]
            lowhealthwolf = ennemies[i]
    return lowhealthwolf

def target_Ealpha(Px):  # Trésor - OK - Return position (x, y)
    Ealpha_pos = []
    for cle in entities:
        # Check if it's an opposite alpha of the entities in argument
        if(entities[cle][0] != Px and entities[cle][0] != 0 and entities[cle][1] == "alpha"):
            Ealpha_pos.append(cle[0])
            Ealpha_pos.append(cle[1])
    return Ealpha_pos

# -------------------------------------------------------

def target_direction(ww_coords, target_coords):  # Seb - OK - Return direction (string)
	# xf = Horizontal distance between ww and target
    # yf = Vertical distance between ww and target
    xf = target_coords[0] - ww_coords[0]
    yf = target_coords[1] - ww_coords[1]
    if xf > 0:
        if yf > 0:
            dirf = "SE"
        elif yf < 0:
            dirf = "SW"
        else:
            dirf = "S"
    elif xf < 0:
        if yf > 0:
            dirf = "NE"
        elif yf < 0:
            dirf = "NW"
        else:
            dirf = "N"
    else:
        if yf > 0:
            dirf = "E"
        elif yf < 0:
            dirf = "W"
    return dirf

def moveAI(ww_coords, target_coords):  # Seb - OK
    temp_target_dir = target_direction(ww_coords, target_coords)
    xtemp = ww_coords[0] + going_to[temp_target_dir][0]
    ytemp = ww_coords[1] + going_to[temp_target_dir][1]
    current_empty_spaces = empty_places(ww_coords)
    while (xtemp, ytemp) not in current_empty_spaces:
        new_direction = random.choice(alt_dir[temp_target_dir])
        #print("New direction = "+new_direction)
        xtemp = ww_coords[0] + going_to[new_direction][0]
        ytemp = ww_coords[1] + going_to[new_direction][1]
        #print("New target case = ("+str(xtemp)+","+str(ytemp)+")")
	#Return final possible coordinates for move
    return (xtemp, ytemp)

"""
def normal_wolves_orders(Px): # Seb
    wolves_orders = ""
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
            current_ww_pos = [key[0], key[1]]
            #Check if current wolf flag is set to 1
            if current_team[key][0] == 0:
                # --------------------------------------------------------------
                # Check for fight

                #Check if ennemy alpha is in range to attack
                ww_in_range = in_range(1, key)
                for key in ww_in_range:
                    if key[1] == "alpha" and key[0] == ennemy:
                        Ealpha_pos = target_Ealpha(ennemy)
                        wolves_orders = " "+str(current_ww_pos[0])+"-"+str(current_ww_pos[1])+":*"+str(Ealpha_pos[0])+"-"+str(Ealpha_pos[1])+" "
                        current_team[key][0] = 1
                        nbr_flags += 1
                #Check if other ennemy is in range to attack
                for key in ww_in_range:
                    if key[0] == ennemy:
                        wolves_orders = " "+str(current_ww_pos[0])+"-"+str(current_ww_pos[1])+":*"+str(key[0])+"-"+str(key[1])+" "
                        current_team[key][0] = 1
                        nbr_flags += 1
                # --------------------------------------------------
                # Check for move

                #Check if empty place is in range to move
                current_empty_spaces = empty_places(key)
                if current_empty_spaces != []:
                    #If empty space around, move to ennemy alpha
                    dir = direction(key, Ealpha_pos)
                    #Check if the move is possible
                    if dir in current_empty_spaces: #Cool, move, add the move to string
                        wolves_orders = ""+str(key[0])+"-"+str(key[1])+":@"+str(dir[0])+"-"+str(dir[1])+" "
                        current_team[key][0] = 1
                        nbr_flags += 1
                    else: # If not, check if another empty space is available in the "same" direction
"""
# --------------------------------------------------
# PART 2
"""
Each type of entity has a different strategy.
"""

def smart_alpha(key, ennemy):
    ennemies = ennemies_in_range(key)
    # Check life of werewolf, if lower than 50, looking for food
    if entities[key][2] < 50:
        food_pos = looking_for_food(key)
        if food_pos in in_range(1, key):
            #eat
            return ""+str(key[0])+"-"+str(key[1])+":<"+str(food_pos[0])+"-"+str(food_pos[1])+" "
        else:
            #move
            destination = moveAI(key, food_pos)
            return ""+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # Check if there is any ennemy in range, if not target ennemy alpha and move
    elif ennemies == []:
        #Move
        target_alpha = target_Ealpha(ennemy)
        destination = moveAI(key, target_alpha)
        return " "+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # If there is an ennemy in range, target him and attack the lowest health one
    else:
        lowenemy = lowest_health(ennemies)
        return " "+str(key[0])+"-"+str(key[1])+":*"+str(lowenemy[0])+"-"+str(lowenemy[1])+" "

def smart_omega(key):
    ...
    return "Test omega"

def smart_human(key):  # Seb - OK
    food_pos = looking_for_food(key)
    if food_pos in in_range(1, key):
        #eat
        return ""+str(key[0])+"-"+str(key[1])+":<"+str(food_pos[0])+"-"+str(food_pos[1])+" "
    else:
        #move
        destination = moveAI(key, food_pos)
        return ""+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "

def smart_wolves(key):
    danger_spaces = ww_danger(key)
    # checks for any danger around the werewolf
    if danger_spaces == []:
        if entities[key][2] > 25:
            Ealpha_pos = target_Ealpha(Px)
            orig = key
            #print(entities[key][0])
            AI_orders = AI_orders + str(orig[0]) + "-" + str(orig[1]) + ":"
            #rand an order and add to str
            order_type = random.choice(["@", "<", "pacify "])
            AI_orders = AI_orders + order_type
            # for x
            if order_type == "pacify ":
                #print(AI_orders)
                ...
            else:
                dest = [0, 0]
                stepx = random.choice([+1, -1, 0])
                dest[0] = orig[0] + stepx
                stepy = random.choice([+1, -1, 0])
                dest[1] = orig[1] + stepy
                AI_orders = AI_orders + str(dest[0]) + "-" + str(dest[1]) + " "
            return AI_orders
    else:
        #print(danger_spaces)
        lowhealthwolf = lowest_health(danger_spaces)
        if entities[key][2] > 25:
            x1, y1 = key
            x2, y2 = lowhealthwolf
            AI_orders = AI_orders + str(x1) + "-" + str(y1) + ":"
            order_type = "*"
            AI_orders = AI_orders + order_type
            AI_orders = AI_orders + str(x2) + "-" + str(y2) + " "
            return AI_orders

def smart_wolves2(key, ennemy):
    ennemies = ennemies_in_range(key)
    # Check life of werewolf, if lower than 30, looking for food
    if entities[key][2] < 30:
        food_pos = looking_for_food(key)
        if food_pos in in_range(1, key):
            #eat
            return ""+str(key[0])+"-"+str(key[1])+":<"+str(food_pos[0])+"-"+str(food_pos[1])+" "
        else:
            #move
            destination = moveAI(key, food_pos)
            return ""+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # Check if there is any ennemy in range, if not target ennemy alpha and move
    elif ennemies == []:
        #Move
        Ealpha_pos = target_Ealpha(ennemy)
        destination = moveAI(key, Ealpha_pos)
        return " "+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # If there is an ennemy in range, target him and attack the lowest health one
    else:
        lowenemy = lowest_health(ennemies)
        return " "+str(key[0])+"-"+str(key[1])+":*"+str(lowenemy[0])+"-"+str(lowenemy[1])+" "

# ----  Main smart AI function ----

def SAI_orders_generator(Px):
    if Px == 1:
        ennemy = 2
    else:
        ennemy = 1
    # Get the members of the team
    current_team = get_team(Px)
    SAI_orders = ""
    for key in current_team.items():
        if current_team[key][1] == "alpha":
            SAI_orders += smart_alpha(key, ennemy)
        elif current_team[key][1] == "omega":
            SAI_orders += smart_omega(key)
        elif current_team[key][1] == "normal":
            SAI_orders += smart_wolves2(key, ennemy)
        else:
            # It's a human
            SAI_orders += smart_human(key)
    return SAI_orders

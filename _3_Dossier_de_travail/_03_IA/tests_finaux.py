#-*- coding: utf-8 -*-
import blessed
import math
import os
import time
import random

entities = {
    (2, 2): [1, 'alpha', 86, 0], 
    (1, 1): [1, 'omega', 100, 0], 
    (1, 2): [1, 'normal', 100, 0], 
    (2, 1): [1, 'normal', 100, 0], 
    (1, 3): [1, 'normal', 100, 0], 
    (2, 3): [1, 'human', 100, 0], 
    (3, 3): [1, 'normal', 100, 0], 
    (3, 2): [1, 'normal', 100, 0], 
    (3, 1): [1, 'normal', 100, 0],
    
    (19, 19): [2, 'alpha', 86, 0], 
    (20, 20): [2, 'omega', 100, 0], 
    (20, 19): [2, 'normal', 100, 0], 
    (19, 20): [2, 'normal', 100, 0], 
    (20, 18): [2, 'normal', 100, 0], 
    (19, 18): [2, 'normal', 100, 0], 
    (18, 18): [2, 'normal', 100, 0], 
    (18, 19): [2, 'normal', 100, 0], 
    (18, 20): [2, 'normal', 100, 0],
    
    (4, 4): [0, 'berries', 10, 0], 
    (4, 5): [0, 'berries', 10, 0], 
    (5, 4): [0, 'berries', 10, 0], 
    (5, 5): [0, 'berries', 10, 0], 
    (16, 16): [0, 'berries', 10, 0], 
    (16, 17): [0, 'berries', 10, 0], 
    (17, 16): [0, 'berries', 10, 0], 
    (17, 17): [0, 'berries', 10, 0], 
    (1, 4): [0, 'apples', 30, 0], 
    (1, 5): [0, 'apples', 30, 0], 
    (20, 16): [0, 'apples', 30, 0], 
    (20, 17): [0, 'apples', 30, 0], 
    (4, 1): [0, 'mice', 50, 0], 
    (5, 1): [0, 'mice', 50, 0], 
    (16, 20): [0, 'mice', 50, 0], 
    (17, 20): [0, 'mice', 50, 0], 
    (5, 7): [0, 'rabbits', 100, 0], 
    (7, 5): [0, 'deers', 500, 0], 
    (16, 14): [0, 'rabbits', 100, 0], 
    (14, 16): [0, 'deers', 500, 0]
    }

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
            # Création du flag d'action
            team[cle][0] = 0
    return team


def get_team2(Px):  # Alesk - OK
    team = {}
    for cle in entities:
        if entities[cle][0] == Px:
            team[cle] = values
    return team

print(get_team(1))

def smart_alpha(key):
    ...
    return "Test alpha"

def smart_omega(key):
    ...
    return "Test omega"

def smart_wolves(Px, key, AI_orders):
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

def smart_human(key):
    ...
    return "Test human"
    #get food

def SAI_orders_generator(Px):
    current_team = get_team(Px)
    SAI_orders = ""
    for key, values in current_team.items():
        if current_team[key][1] == "alpha":
            SAI_orders += smart_alpha(key)
        elif current_team[key][1] == "omega":
            SAI_orders += smart_omega(key)
        elif current_team[key][1] == "normal":
            SAI_orders += smart_wolves2(key)
        else:
            # It's a human
            SAI_orders += smart_human(key)
    return SAI_orders

#print(SAI_orders_generator(1))

def empty_places(ww_pos):  # Alesk - OK
    x = ww_pos[0]
    y = ww_pos[1]
    empty_spaces = []
    if (x+1, y) not in entities:
        empty_spaces.append((x+1, y))
    elif (x, y+1) not in entities:
        empty_spaces.append((x, y+1))
    elif (x+1, y+1) not in entities:
        empty_spaces.append((x+1, y+1))
    elif (x-1, y+1) not in entities:
        empty_spaces.append((x-1, y+1))
    elif (x-1, y-1) not in entities:
        empty_spaces.append((x-1, y-1))
    elif (x+1, y-1) not in entities:
        empty_spaces.append((x+1, y-1))
    elif (x-1, y) not in entities:
        empty_spaces.append((x-1, y))
    elif (x, y-1) not in entities:
        empty_spaces.append((x, y-1))
    return empty_spaces

def empty_places2(ww_pos):
    empty_cases = []
    for key in going_to:
        x = ww_pos[0] + going_to[key][0]
        y = ww_pos[1] + going_to[key][1]
        if (x, y) not in entities:
            empty_cases.append((x, y))
    return empty_cases

#print(empty_places2((18, 18)))

def test_move(ww_coords, temp_target_dir):  # Seb - OK
    xtemp = ww_coords[0] + going_to[temp_target_dir][0]
    ytemp = ww_coords[1] + going_to[temp_target_dir][1]
    current_empty_spaces = empty_places2(ww_coords)
    while (xtemp, ytemp) not in current_empty_spaces:
        #print("Current target case = ("+str(xtemp)+","+str(ytemp)+")")
        #print("----")
        new_direction = random.choice(alt_dir[temp_target_dir])
        print("New direction = "+new_direction)
        xtemp = ww_coords[0] + going_to[new_direction][0]
        ytemp = ww_coords[1] + going_to[new_direction][1]
        print("New target case = ("+str(xtemp)+","+str(ytemp)+")")
	#print("Final direction = "+new_direction)
	#Return final coordinates
    return (xtemp, ytemp)

#print(test_move((18, 18), "N"))


def in_range(range, ww_coords):  # Spec 100 % and Code 100%
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
    ww_in_range = {}
    for key, values in entities.items():
        if values[0] != 0:
            x = abs((key[0]) - (ww_coords[0]))
            y = abs((key[1]) - (ww_coords[1]))
            if x == 0 and y == 0:
                ...  # current wolf
            elif (x <= range) and (y <= range):
                ww_in_range.update({key: values})
    return ww_in_range

#print(in_range(1, (18, 18)))


def target_direction(ww_coords, target):  # Seb - OK - Return direction (string)
    
    xf = target[0] - ww_coords[0]
    print("xf = "+str(xf))
    
    yf = target[1] - ww_coords[1]
    print("yf = "+str(yf))
    
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

#print(target_direction((18, 18), (20, 20)))

def smart_wolves2(key):
    ennemies = ennemies_in_range(key)
    # Check life of werewolf, if lower than 30, looking for food
    if entities[key][2] < 30:
        food_pos = looking_for_food(key)
        if food_pos in in_range(1, key):
            #eat
            return ""+str(key[0])+"-"+str(key[1])+":<"+str(food_pos[0])+"-"+str(food_pos[1])+" "
        else:
            #move
            food_direction = target_direction(key, food_pos)
            destination = test_move(key, food_direction)
            return ""+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # Check if there is any ennemy in range, if not target ennemy alpha and move
    elif ennemies == []:
        #Move
        target_alpha = target_Ealpha(Px)
        destination = test_move(key, target_alpha)
        return " "+str(key[0])+"-"+str(key[1])+":@"+str(destination[0])+"-"+str(destination[1])+" "
    # If there is an ennemy in range, target him and attack the lowest health one
    else:
        lowenemy = lowest_health2(ennemies)
        return " "+str(key[0])+"-"+str(key[1])+":*"+str(lowenemy[0])+"-"+str(lowenemy[1])+" "




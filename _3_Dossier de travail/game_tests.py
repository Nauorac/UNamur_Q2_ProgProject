#-*- coding: utf-8 -*-

from game_turns import *

"""
Dictionnaires de tests basés sur le fichier "Short example.ano"
"""
team1 = {(2, 1): ["alpha", 100], (1, 1): ["omega", 60], (2, 2): ["normal", 100]}
team2 = {(5, 5): ["alpha", 100], (6, 6): ["omega", 100], (6, 5): ["normal", 100]}

foods = {(2, 4): ["berries", 10], (6, 1): ["apples", 30], (5, 3): ["mice", 50], (1, 6): ["rabbits", 75], (4, 4): ["deers", 100]}

teams = {(2, 1): [1, "alpha", 60], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
         (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100]}

def entity_at(entity_coords):

    # Validée
    for key, values in foods.items():
        if key == entity_coords:
            return ["foods", values[0], values[1],]
    for key, values in teams.items():
        if key == entity_coords:
            return [values[0], values[1], values[2],]
    return False

print(entity_at((2,1)))
print(entity_at((6,1)))
print(foods)

def feed(ww_coords, entity_coords):
    check_food = entity_at(entity_coords)
    check_ww = entity_at(ww_coords)
    # Test if food exist
    if check_food != False:
        # Test si le ww existe, et si son energie est en dessous de 100
        if (check_ww != False) and (check_ww[0] != "foods") and (check_ww[2] < 100):
            food_E = check_food[2]
            ww_E = check_ww[2]
            while (food_E > 0) and (ww_E < 100):
                food_E -= 1
                #print(food_E)
                ww_E += 1
            if food_E == 0:
                print("The "+check_food[1]+" have been completely eaten.")
                foods.pop(entity_coords)
            else:
                check_food[2] = food_E
            check_food.pop(0)
            check_ww[2] = ww_E
            foods.update({entity_coords: check_food})
            teams.update({ww_coords: check_ww})
        else:
            print("There is no food there.")


feed((2,1), (6,1))

print(entity_at((2, 1)))
print(entity_at((6,1)))
print(foods)
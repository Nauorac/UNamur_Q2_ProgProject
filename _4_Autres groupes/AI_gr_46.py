from copy import deepcopy

#################
#               #
#   STRATEGY    #
#               #
#################

def final_attack(board, board_copy, team1, team2):
    """
    Manage the final attack (if alpha ennemy has less than 50 energy, or three werewolves enemy are human)
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Nathan Lambrechts (v.1 28/03/2022)
    Implementation : Nathan Lambrechts (v.3 30/04/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #we work with a deepcopy because we can't change keys of a dictionnary during the loop who iterate on
    board_copy_t1 = deepcopy(board_copy[team1])

    #all normal wolves aim at the opposing alpha to finish him off
    for werewolf in board_copy_t1:

        #if the wolf is a normal wolf and has not taken any action yet
        if werewolf not in board["already_action"] and "alpha" not in board_copy[team1][werewolf][0]:

            #human wolves will not attack the alpha
            if "human" not in board_copy[team1][werewolf][0]:
                
                #if they are too far they approach, otherwise they attack
                if distance(werewolf, board_copy["alpha"][team2-1]) > 1:
                    destination = move(board_copy, werewolf,board_copy["alpha"][team2-1], team1, team2)

                    #if it is possible to move
                    if destination != "":

                        #add to the list of wolves that have already done an action
                        board["already_action"].append(destination)

                        #modify the copy of the board to have the up-to-date positions
                        board_copy[team1][destination] = board_copy[team1][werewolf]
                        del board_copy[team1][werewolf]

                        #update the actions
                        action = action + werewolf.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

                #if he is close enough, the werewolf attacks
                else:

                    #add to the list of wolves that have already done an action
                    board["already_action"].append(werewolf)

                    #update the actions
                    action = action + werewolf.replace(" ", "-") + ":*" + board["alpha"][team2-1].replace(" ", "-") + " "

            #humans will feed        
            else:

                #predefining two lists
                foods_distance = []
                foods = []
    
                #for each food
                for food in board["food"]:

                    #add the position of food in the list 'foods' and the distance between the food and the werewolf in the list 'foods_distance'
                    if board_copy['food'][food][1] > 0:
                        foods.append(food)
                        foods_distance.append(distance(werewolf, food))

                if foods != []:
                    #the final food is the nearest
                    food = min(foods_distance)
                    index = foods_distance.index(food)
                    final_food = foods[index]

                    #approaches the food until it can be eaten
                    if distance(werewolf, final_food) > 1:
                        destination = move(board_copy, werewolf, final_food, team1, team2)

                        #if it is possible to move
                        if destination != "":

                            #add to the list of wolves that have already done an action
                            board["already_action"].append(destination)

                            #modify the copy of the board to have the up-to-date positions
                            board_copy[team1][destination] = board_copy[team1][werewolf]
                            del board_copy[team1][werewolf]

                            if 'omega' in board_copy[team1][destination][0]:
                                board_copy["omega"][team1-1] = destination

                            #update the actions
                            action = action + werewolf.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "
                    
                    #eat if werewolf is close enough
                    else:

                        #if werewolf needs to eat
                        if board_copy[team1][werewolf][1] < 100:

                            #add to the list of wolves that have already done an action
                            board["already_action"].append(werewolf)

                            #update energy of werewolf and of food
                            for energy in range(board_copy["food"][final_food][1]):
                                if board_copy[team1][werewolf][1] != 100:
                                    if board['food'][final_food][1] > 0:       
                                        board_copy["food"][final_food][1] -= 1
                                        board_copy[team1][werewolf][1] += 1

                            #update the actions
                            action = action + werewolf.replace(" ", "-") + ":<" + final_food.replace(" ", "-") + " "

    #danger around the alpha of team one
    danger = danger_level(board, team1, team2)

    #if it is possible to move
    destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], danger.index(min(danger))), team1, team2)
    if board_copy['alpha'][team1-1] not in board["already_action"] and destination != "":

        #update the actions
        action = action + board_copy['alpha'][team1-1].replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

        #modify the copy of the board to have the up-to-date positions
        board_copy[team1][destination] = board_copy[team1][board_copy["alpha"][team1-1]]
        del board_copy[team1][board_copy["alpha"][team1-1]]
        board_copy['alpha'][team1-1] = destination

        #add to the list of wolves that have already done an action
        board["already_action"].append(destination)

    return action

def grouping(board, board_copy, team1, team2):
    """
    Manage the grouping.
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Mohamed Ait Hassou (v.1 25/03/2022)
    Implementation : Mohamed Ait Hassou (v.3 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #finds werewolves around alpha
    on_good_position = ww_around_alpha(board, team1, team2)

    #find the urgency of each tile around alpha
    danger_around_alpha = danger_level(board, team1, team2)

    #checks what is around alpha
    around_alpha = what_around(board_copy['alpha'][team1-1], board, team1, team2)

    #find the indexs of walls
    walls = several_index(around_alpha,0)

    #if there are wall(s) and alpha can move
    if walls != [] and board_copy["alpha"][team1-1] not in board["already_action"]:

        #if wall on top, top right, and right
        if 0 in walls and 1 in walls and 2 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 5), team1, team2)

        #if wall on right, bellow on right, and bellow
        elif 2 in walls and 3 in walls and 4 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 7), team1, team2)

        #if wall bellow, bellow on left, and on left
        elif 4 in walls and 5 in walls and 6 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 1), team1, team2)

        #if wall on left, on top left, and on top
        elif 6 in walls and 7 in walls and 0 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 3), team1, team2)

        #if wall on top
        elif 0 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 4), team1, team2)

        #if wall on right
        elif 2 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 6), team1, team2)

        #if wall bellow
        elif 4 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 0), team1, team2)

        #if wall on left
        elif 6 in walls:
            destination = move(board_copy, board_copy['alpha'][team1-1], index_to_tile(board_copy['alpha'][team1-1], 2), team1, team2)

        #if alpha can move
        if destination != "":

            #add to the list of wolves that have already done an action
            board["already_action"].append(destination)

            #modify the copy of the board to have the up-to-date positions
            board_copy[team1][destination] = board_copy[team1][board_copy["alpha"][team1-1]]
            del board_copy[team1][board_copy["alpha"][team1-1]]
            board_copy['alpha'][team1-1] = destination

            #update the actions
            action = action + board["alpha"][team1-1].replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

    #if alpha is not near a wall
    else:

        #index of the less dangerous tile around the alpha
        index = danger_around_alpha.index(max(danger_around_alpha))

        #destination to the less dangerous tile
        destination = move(board_copy, board_copy["omega"][team1-1], index_to_tile(board["alpha"][team1-1], index), team1, team2)

        #if omega can move
        if destination != "" and board_copy["omega"][team1-1] not in board["already_action"]:

            #modify the copy of the board to have the up-to-date positions
            board_copy[team1][destination] = board_copy[team1][board_copy["omega"][team1-1]]
            del board_copy[team1][board_copy["omega"][team1-1]]
            board_copy["omega"][team1-1] = destination

            #add to the list of wolves that have already done an action
            board["already_action"].append(destination)

            #update the actions
            action = action + board["omega"][team1-1].replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

        #we work with a deepcopy because we can't change keys of a dictionnary during the loop who iterate on
        board_copy_t1 = deepcopy(board_copy[team1])

        #for each werewolf on team one
        for werewolf in board_copy_t1:

            #if the werewolf is not on the more dangerous position and he is not alpha or omega and he can do an action
            if werewolf not in on_good_position and "alpha" not in board_copy[team1][werewolf][0] and "omega" not in board_copy[team1][werewolf][0] and werewolf not in board["already_action"]:

                #index of the more dangerous tile around the alpha
                index = danger_around_alpha.index(min(danger_around_alpha))

                #destination to good tile near alpha
                destination = move(board_copy, werewolf, index_to_tile(board_copy["alpha"][team1-1], index), team1, team2)

                #if alpha can move
                if destination != "":

                    #modify the copy of the board to have the up-to-date positions
                    board_copy[team1][destination] = board_copy[team1][werewolf]
                    del board_copy[team1][werewolf]

                    #add to the list of wolves that have already done an action
                    board["already_action"].append(destination)

                    #update the actions
                    action = action + werewolf.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "
    return action

def eat_around(board, board_copy, team1):
    """
    Allows werewolves to feed.
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Virgile Devolder (v.1 30/04/2022)
    Implementation : Virgile Devolder (v.2 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""
    
    #for each werewolf
    for werewolf in board_copy[team1]:

        #best food around the werewolf
        best_food = best_food_around(board_copy, werewolf)

        if best_food != "" and werewolf not in board['already_action'] and board_copy[team1][werewolf][1] < 100:

            #add to the list of wolves that have already done an action
            board['already_action'].append(werewolf)

            #update the actions
            action = action + werewolf.replace(" ", "-") + ":<" + best_food.replace(" ", "-") + " "

            #update energy of werewolf and of food
            for energy in range(board_copy["food"][best_food][1]):
                if board_copy[team1][werewolf][1] != 100:
                    if board['food'][best_food][1] > 0:       
                        board_copy["food"][best_food][1] -= 1
                        board_copy[team1][werewolf][1] += 1

    return action

def defense(board, board_copy, team1, team2):
    """
    Manage the defense.
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Alexandre Wenkin (v.1 22/03/2022)
    Implementation : Alexandre Wenkin (v.4 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #for werewolves around the alpha
    for werewolf in board_copy[team1]:

        #if werewolf is not a human
        if "human" not in board_copy[team1][werewolf][0]:
        
            #if there are a ennemy, werewolf attacks
            if werewolf not in board['already_action']:

                #find the best ennemy to attack
                ennemy = best_to_attack(werewolf, board_copy, team1, team2)
                
                #if there are a ennemy around
                if ennemy != "":

                    #add to the list of wolves that have already done an action
                    board['already_action'].append(werewolf)

                    #update the actions
                    action = action + werewolf.replace(" ", "-") + ":*" + ennemy.replace(" ", "-") + " "

                    #update life of werewolf ennemy
                    bonus(board_copy, 1)
                    board_copy[team2][ennemy][1] -= round(((board_copy[team1][werewolf][2] + board_copy[team1][werewolf][1]))/10)
                    if board_copy[team2][ennemy][1] < 0:
                        board_copy[team2][ennemy][1] = 0
                    bonus(board_copy, 0)

        else:
            best_food = best_food_around(board_copy, werewolf)
            if best_food != "" and werewolf not in board['already_action'] and board_copy[team1][werewolf][1] < 100:

                #add to the list of wolves that have already done an action
                board['already_action'].append(werewolf)

                #update the actions
                action = action + werewolf.replace(" ", "-") + ":<" + best_food.replace(" ", "-") + " "

                #update energy of werewolf and of food
                for energy in range(board_copy["food"][best_food][1]):
                    if board_copy[team1][werewolf][1] != 100:
                        if board['food'][best_food][1] > 0:       
                            board_copy["food"][best_food][1] -= 1
                            board_copy[team1][werewolf][1] += 1

    return action

def no_ennemy_attack(board, board_copy, team1, team2):
    """
    Handles the case where the enemy does not attack.
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Alexandre Wenkin (v.1 22/04/2022)
    Implementation : Alexandre Wenkin (v.3 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #average position of the ennemy
    ennemy = position_ennemy(board, team2)
    
    #predefining two lists
    werewolves_to_move = []
    distances = []

    #for each werewol in team one
    for werewolf in board_copy[team1]:

        #append the distance between the ennemy and the werewolf
        distances.append(distance(werewolf, ennemy))

        #append the werewolf
        werewolves_to_move.append(werewolf)

    #sort distances
    distances_sorted = sorted(distances)

    #for each werewolf in the formation
    for iteration, ww in enumerate(distances_sorted):

        #moves the werewolf nearest the ennemy
        ww_to_move = werewolves_to_move[distances.index(ww)]

        #if there are an ennemy around the werewolf
        if 2 in what_around(ww_to_move, board, team1, team2):

            #if werewolf can do an action
            if ww_to_move not in board["already_action"]:

                #the best werewolf to attack
                ennemy_to_attack = best_to_attack(ww_to_move, board_copy, team1, team2)

                if ennemy_to_attack != "":

                    #add to the list of wolves that have already done an action
                    board['already_action'].append(ww_to_move)

                    #update the actions
                    action = action + ww_to_move.replace(" ", "-") + ":*" + ennemy_to_attack.replace(" ", "-") + " "

                    #update life of werewolf ennemy
                    bonus(board_copy, 1)
                    board_copy[team2][ennemy_to_attack][1] -= round(((board_copy[team1][ww_to_move][2] + board_copy[team1][ww_to_move][1]))/10)
                    if board_copy[team2][ennemy_to_attack][1] < 0:
                        board_copy[team2][ennemy_to_attack][1] = 0
                    bonus(board_copy, 0)
        
        #if no ennemy around the werewolf
        else:

            #moves the alpha second if he can move
            if iteration == 1 and board_copy['alpha'][team1-1] not in board["already_action"]:

                #destination to the ennemy
                destination = move(board_copy, board_copy['alpha'][team1-1], ennemy, team1, team2)

                #if he can move
                if destination != '':

                    #modify the copy of the board to have the up-to-date positions
                    board_copy[team1][destination] = board_copy[team1][board_copy['alpha'][team1-1]]
                    del board_copy[team1][board_copy['alpha'][team1-1]]
                    board_copy['alpha'][team1-1] = destination
                    
                    #add to the list of wolves that have already done an action
                    board["already_action"].append(destination)

                    #update the actions
                    action = action + board["alpha"][team1-1].replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

            #we put 1000, so he can no longer be chosen as the closest wolf
            distances[distances.index(ww)] = 1000

            #destination to the ennemy
            destination = move(board_copy, ww_to_move, ennemy, team1, team2)

            #if werewolf can move and he is not the alpha 
            if ww_to_move not in board["already_action"] and destination != "" and "alpha" not in board[team1][ww_to_move][0]:

                #modify the copy of the board to have the up-to-date positions
                board_copy[team1][destination] = board_copy[team1][ww_to_move]
                del board_copy[team1][ww_to_move]

                if 'omega' in board_copy[team1][destination][0]:
                    board_copy["omega"][team1-1] = destination

                #add to the list of wolves that have already done an action
                board["already_action"].append(destination)

                #update the actions
                action = action + ww_to_move.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "
    
    return action

def go_on_food(board, board_copy, team1, team2):
    """
    Brings training to the nearest most profitable food source.

    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    board_copy : copy of board (dict)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Virgile Devolder (v.1 28/04/2022)
    Implementation : Virgile Devolder (v.2 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #find the best source of food on the map 
    best_food = find_best_food(board, team1)

    if best_food != []:

        #checks the werewolves around the alpha of team one
        ww_near_alpha = ww_around_alpha(board_copy, team1, team2)

        #if there are werewolves around alpha
        if ww_near_alpha != []:

            #for the werewolves around alpha
            for werewolf in ww_near_alpha:

                #if the werewolf is on the position of the best food and he is not the alpha
                if werewolf == best_food and "alpha" not in board_copy[team1][werewolf][0]:

                    #checks what is around the werewolf to find a empty tile
                    around_ww = what_around(werewolf, board_copy, team1, team2)

                    #if there are space are werewolf
                    if 3 in around_ww:

                        #move the werewolf to a empty tile around
                        destination = move(board_copy, werewolf, index_to_tile(werewolf, around_ww.index(3)), team1, team2)

                        #if the werewolf can move
                        if destination != "" and werewolf not in board["already_action"] and board_copy["alpha"][team1-1] not in board["already_action"]:

                            #modify the copy of the board to have the up-to-date positions
                            board_copy[team1][destination] = board_copy[team1][werewolf]
                            del board_copy[team1][werewolf]
                            board_copy[team1][best_food] = board_copy[team1][board_copy["alpha"][team1-1]]
                            del board_copy[team1][board_copy["alpha"][team1-1]]

                            #update the actions
                            action = action + werewolf.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "
                            action = action + board['alpha'][team1-1].replace(" ", "-") + ":@" + best_food.replace(" ", "-") + " "

                            #add to the list of wolves that have already done an action
                            board['already_action'].append(destination)
                            board['already_action'].append(best_food)

                            #modify the copy of the board to have the up-to-date positions
                            board_copy["alpha"][team1-1] = best_food

                            if 'omega' in board_copy[team1][destination][0]:
                                board_copy["omega"][team1-1] = destination

            #predefining a list that will contain the distances
            distances = []

            #for each werewolf near the alpha of team one 
            for werewolf in ww_near_alpha:

                #distance between the werewolf and the food's position
                distances.append(distance(werewolf, best_food))

            #sort the distances
            distances_sorted = sorted(distances)

            #for each werewolf in the formation
            for iteration, ww in enumerate(distances_sorted):

                #alpha moves second
                if iteration == 1 and board_copy['alpha'][team1-1] not in board["already_action"]:
                    
                    #desination to the food
                    destination = move(board_copy, board_copy['alpha'][team1-1], best_food, team1, team2)

                    #if the alpha can move
                    if destination != '':

                        #modify the copy of the board to have the up-to-date positions
                        board_copy[team1][destination] = board_copy[team1][board_copy['alpha'][team1-1]]
                        del board_copy[team1][board_copy['alpha'][team1-1]]
                        board_copy["alpha"][team1-1] = destination

                        #add to the list of wolves that have already done an action
                        board["already_action"].append(destination)

                        #update the actions
                        action = action + board["alpha"][team1-1].replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

                #we move the werewole nearest the food
                ww_to_move = ww_near_alpha[distances.index(ww)]

                #we put 1000, so he can no longer be chosen as the closest wolf
                distances[distances.index(ww)] = 1000

                #destination to the food
                destination = move(board_copy, ww_to_move, best_food, team1, team2)

                #if werewolf can move
                if ww_to_move not in board["already_action"] and destination != "":

                    #modify the copy of the board to have the up-to-date positions
                    board_copy[team1][destination] = board_copy[team1][ww_to_move]
                    del board_copy[team1][ww_to_move]

                    if 'omega' in board_copy[team1][destination][0]:
                        board_copy["omega"][team1-1] = destination

                    #add to the list of wolves that have already done an action
                    board["already_action"].append(destination)

                    #update the actions
                    action = action + ww_to_move.replace(" ", "-") + ":@" + destination.replace(" ", "-") + " "

    return action

def pacification(board, board_copy, team1):
    """
    Manages pacification. Omega pacifies everyone around and other werewolves eat. 
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team1 : number of team1 (int)

    return
    -------
    action : actions of werewolves (str)
        
    version
    -------
    Specification : Mohamed Ait Hassou (v.1 28/04/2022)
    Implementation : Mohamed Ait Hassou (v.2 01/05/2022)
    """

    #predefinition of the string which will contain the actions of the werewolves
    action = ""

    #position of omega
    omega = board_copy['omega'][team1-1] 

    #if the omega has not yet taken action
    if omega not in board['already_action']:

        #add to the list of wolves that have already done an action
        board['already_action'].append(omega)

        #update the actions
        action = action + omega.replace(" ", "-") + ":pacify" + " "

    #for each werewolf in team one
    for ally in board_copy[team1]:

        #if werewolf is an human
        if 'human' in board_copy[team1][ally][0]:

            #find the best found around the werewolf
            best_food = best_food_around(board_copy, ally)

            #if the werewolf can move and has not yet taken action
            if best_food != "" and ally not in board["already_action"] and board_copy[team1][ally][1] < 100:

                #add to the list of wolves that have already done an action
                board["already_action"].append(ally)

                #update the actions
                action = action + ally.replace(" ", "-") + ":<" + best_food.replace(" ", "-") + " "

                #update energy of werewolf and of food
                for energy in range(board_copy["food"][best_food][1]):
                    if board_copy[team1][ally][1] != 100:
                        if board['food'][best_food][1] > 0:       
                            board_copy["food"][best_food][1] -= 1
                            board_copy[team1][ally][1] += 1

    #for each werewolf in team one
    for ally in board_copy[team1]:

        #if the werewolf has not yet taken action
        if ally not in board["already_action"]:

            #find the best food around the werewolf
            best_food = best_food_around(board_copy, ally)

            #if the werewolf can move
            if best_food != "" and board_copy[team1][ally][1] < 100:

                #add to the list of wolves that have already done an action
                board["already_action"].append(ally)

                #update the actions
                action = action + ally.replace(" ", "-") + ":<" + best_food.replace(" ", "-") + " "

                #update energy of werewolf and of food
                for energy in range(board_copy["food"][best_food][1]):
                    if board_copy[team1][ally][1] != 100:
                        if board['food'][best_food][1] > 0:       
                            board_copy["food"][best_food][1] -= 1
                            board_copy[team1][ally][1] += 1

    return action

##############
#            #
#   TOOLS    #
#            #
##############

def move(board_copy, position, destination, team1, team2):
    """
    Make a werewolf move from point A to point Z. Try to go the shortest way, go around if it's impossible.

    Parameters
    -------
    board_copy : copy of board (dict)
    position : position of werewolf to move (str)
    destination : destination of the werewolf (str)
    team1 : number of team1 (int)
    team2: tumber of team2 (int)

    return
    -------
    tile : position of tile (str)
        
    version
    -------
    Specification : Virgile Devolder (v.1 20/03/2022)
    Implementation : Virgile Devolder (v.2 28/04/2022)
    """

    #splits the position string and the destination string into two integers (rows and columns)
    position2 = position.split(" ")
    destination2 = destination.split(" ")

    #definition of the posiiton and the destination
    r1, r2 = int(position2[0]), int(destination2[0])
    c1, c2 = int(position2[1]), int(destination2[1])

    #checks if there are anything around the werewolf
    around_werewolf = what_around(position, board_copy, team1, team2)
    
    #destination is on top left
    if r1 > r2 and c1 > c2:

        #first choice : top left
        if around_werewolf[7] == 3:
            return index_to_tile(position, 7)

        #second choice : on left 
        elif around_werewolf[6] == 3:
            return index_to_tile(position, 6)
        
        #third choice : on top
        elif around_werewolf[0] == 3:
            return index_to_tile(position, 0)

        #if the three choices are impossible
        else:
            return ""

    #destination is bellow on left
    elif r1 < r2 and c1 > c2:

        #first choice : bellow on left
        if around_werewolf[5] == 3:
            return index_to_tile(position, 5)
        
        #second choice : bellow
        elif around_werewolf[4] == 3:
            return index_to_tile(position, 4)

        #third choice : on left
        elif around_werewolf[6] == 3:
            return index_to_tile(position, 6)

        #if the three choices are impossible
        else:
            return ""

    #destination is bellow on right
    elif r1 < r2 and c1 < c2:

        #first choice : bellow on right
        if around_werewolf[3] == 3:
            return index_to_tile(position, 3)

        #second choice : on right
        elif around_werewolf[2] == 3:
            return index_to_tile(position, 2)

        #third choice : bellow
        elif around_werewolf[4] == 3:
            return index_to_tile(position, 4)

        #if the three choices are impossible
        else:
            return ""

    #destination is on top right
    elif r1 > r2 and c1 < c2:

        #first choice : top on right
        if around_werewolf[1] == 3:
            return index_to_tile(position, 1)

        #second choice : on top
        elif around_werewolf[0] == 3:
            return index_to_tile(position, 0)

        #third choice : on right
        elif around_werewolf[2] == 3:
            return index_to_tile(position, 2)

        #if the three choices are impossible
        else:
            return ""

    #destination is on top
    elif r1 > r2:

        #first choice : on top
        if around_werewolf[0] == 3:
            return index_to_tile(position, 0)

        #second choice : top on left
        elif around_werewolf[7] == 3:
            return index_to_tile(position, 7)

        #third choice : top on right
        elif around_werewolf[1] == 3:
            return index_to_tile(position, 1)

        #if the three choices are impossible
        else:
            return ""
    
    #destination is bellow
    elif r1 < r2:

        #first choice : bellow
        if around_werewolf[4] == 3:
            return index_to_tile(position, 4)

        #second choice : bellow on right
        elif around_werewolf[3] == 3:
            return index_to_tile(position, 3)

        #third choice : bellow on left
        elif around_werewolf[5] == 3:
            return index_to_tile(position, 5)

        #if the three choices are impossible
        else:
            return ""

    #destination is on right
    elif c1 > c2:

        #first choice : on left
        if around_werewolf[6] == 3:
            return index_to_tile(position, 6)

        #second choice : bellow on left
        elif around_werewolf[5] == 3:
            return index_to_tile(position, 5)

        #third choice : top on left
        elif around_werewolf[7] == 3:
            return index_to_tile(position, 7)

        #if the three choices are impossible
        else:
            return ""

    #destination is on right
    elif c1 < c2:

        #first choice : on right
        if around_werewolf[2] == 3:
            return index_to_tile(position, 2)

        #second choice : top on right
        elif around_werewolf[1] == 3:
            return index_to_tile(position, 1)
        
        #third choice : bellow on right
        elif around_werewolf[3] == 3:
            return index_to_tile(position, 3)

        #if the three choices are impossible
        else:
            return ""

    #if it's the same tile
    else:
        return ''

def bonus(board_copy, choice):
    """
    Give bonus to werewolves.
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    choice : 0 to delete the bonus, 1 to calculate bonus (int)

    version
    -------
    Specification : Mohamed Ait Hassou (v.2 25/02/2022)
    Implementation : Mohamed Ait Hassou (v.1 28/02/2022)
    """

    #add bonus
    if choice == 1:
        #for team 1 then team 2
        for team in range(1,3):

            #empty list who is going to contains positions
            positions = [] 

            #fill the list of positions with board
            for position in board_copy[team]:     
                positions.append(position)
            
            #two loops to compare each werewolf
            for position1 in positions: 

                #initialize the bonus to 0 for each werewolf
                bonus = 0 
                for position2 in positions:

                    #not compare a werewolf to himself
                    if position1 != position2: 

                        #add bonus link to alpha and to normal werewolves
                        if distance(position1,position2) <= 4 and board_copy[team][position2][0] == "alpha":
                            bonus += 30           
                        elif distance(position1,position2) <= 2 and board_copy[team][position2][0] != "alpha" and 'human' not in board_copy[team][position2][0]: 
                            bonus += 10

                #add bonus to board    
                board_copy[team][position1].append(bonus)

    #delete bonus
    elif choice == 0:

        #for team 1 then team 2
        for team in range(1,3):

            #del bonus for each werewolf
            for werewolf in board_copy[team]:
                del(board_copy[team][werewolf][2])

def best_to_attack(position, board_copy, team1, team2):
    """
    Gives the best werewolf to attack around a position.

    Parameters
    -------
    position : position of the central tile (str)
    board_copy : copy of board (dict)
    team1 : team of the central werewolf (int)
    team2 : adeverse team (int)

    return
    -------
    position : position of the best werewolf to attack (str)
    
    version
    -------
    Specification : Virgile Devolder (v.1 01/05/2022)
    Implementation : Virgile Devolder (v.2 01/05/2022)
    
    """

    #cehcks what is around a werewolf to find ennemies
    around_position = what_around(position, board_copy, team1, team2)

    #predefining two lists
    around = []
    around_energy = []

    #adds positions and energies to a list
    for index, tile in enumerate(around_position):
        if tile == 2 and "human" not in board_copy[team2][index_to_tile(position, index)][0]:
            around.append(index_to_tile(position, index))
            around_energy.append(board_copy[team2][index_to_tile(position, index)][1])

    #attack the werewolf with the smallest life
    if around != []:
        for werewolf in around_energy:
            if werewolf == 0:
                werewolf = 1000
        return around[around_energy.index(min(around_energy))]
    else:
        return ''

def what_around(position, board, team1, team2):
    """
    Check what is around a werewolf.

    Parameters
    -------
    position : position of the central tile (str)
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team1 : team of the central werewolf (int)
    team2 : adeverse team (int)

    return
    -------
    around : gives 8 elements for the 8 tiles around the werewolf : 0 if there are a wall, 1 if there are a werewolf in same team, 2 if there are a werewolf in adverse team, 3 if there are nothing. (tuple)
    
    version
    -------
    Specification : Nathan Lambrechts (v.1 17/03/2022)
    Implementation : Nathan Lambrechts(v.2 31/03/2022)
    """

    #splits the position string into two integers (rows and columns)
    position2 = position.split(" ")
    row, column = position2
    row = int(row)
    column = int(column)

    #predefining a list
    around = []

    #top tile (index 0)
    #1 if werewolf ally
    if (str(row-1) + ' ' + str(column)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row-1) + ' ' + str(column)) in board[team2] and "human" in board:
        around.append(2)
    #0 if wall
    elif row-1 == 0:
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #top tile on right (index 1)
    #1 if werewolf ally
    if (str(row-1) + ' ' + str(column+1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row-1) + ' ' + str(column+1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif row-1 == 0 or column+1 > int(board["size"][1]):
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #tile on right (index 2)
    #1 if werewolf ally
    if (str(row) + ' ' + str(column+1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row) + ' ' + str(column+1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif column+1 > int(board["size"][1]):
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #tile bellow on right (index 3)
    #1 if werewolf ally
    if (str(row+1) + ' ' + str(column+1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row+1) + ' ' + str(column+1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif row+1 > int(board["size"][0]) or column+1 > int(board["size"][1]):
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #tile bellow (index 4)
    #1 if werewolf ally
    if (str(row+1) + ' ' + str(column)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row+1) + ' ' + str(column)) in board[team2]:
        around.append(2)
    #0 if wall
    elif row+1 > int(board["size"][0]):
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #tile bellow on left (index 5)
    #1 if werewolf ally
    if (str(row+1) + ' ' + str(column-1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row+1) + ' ' + str(column-1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif row+1 > int(board["size"][0]) or column-1 == 0:
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #tile on left (index 6)
    #1 if werewolf ally
    if (str(row) + ' ' + str(column-1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row) + ' ' + str(column-1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif column-1 == 0:
        around.append(0)
    #3 if nothing
    else:
        around.append(3)

    #top tile on left (index 7)
    #1 if werewolf ally
    if (str(row-1) + ' ' + str(column-1)) in board[team1]:
        around.append(1)
    #2 if ennemy werewolf
    elif (str(row-1) + ' ' + str(column-1)) in board[team2]:
        around.append(2)
    #0 if wall
    elif row-1 == 0 or column-1 == 0:
        around.append(0)
    #3 if nothing
    else:
        around.append(3) 

    return tuple(around)

def food_around(position, board):
    """
    Check what is around a werewolf.

    Parameters
    -------
    position : position of the central tile (str)
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    
    return
    -------
    around : gives 8 elements for the 8 tiles around the werewolf : 0 if there are a wall, 1 if there are a werewolf in same team, 2 if there are a werewolf in adverse team, 3 if there are nothing. (tuple)
    
    version
    -------
    Specification : Nathan Lambrechts (v.1 31/03/2022)
    Implementation : Nathan Lambrechts(v.1 31/03/2022)
    """

    #splits the position string into two integers (rows and columns)
    position = position.split(" ")
    row, column = position  
    row = int(row)
    column = int(column)

    #predefining a list
    around = []

    #if there is food on the top tile (index 0)
    if (str(row-1) + ' ' + str(column)) in board['food']:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the top tile on right (index 1)
    if (str(row-1) + ' ' + str(column+1)) in board['food']:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the tile on right (index 2)
    if (str(row) + ' ' + str(column+1)) in board["food"]:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the tile bellow on right (index 3)
    if (str(row+1) + ' ' + str(column+1)) in board["food"]:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the tile bellow (index 4)
    if (str(row+1) + ' ' + str(column)) in board["food"]:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the tile bellow on left (index 5)
    if (str(row+1) + ' ' + str(column-1)) in board["food"]:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the tile on left (index 6)
    if (str(row) + ' ' + str(column-1)) in board["food"]:
        around.append(1)
    else:
        around.append(0)

    #if there is food on the top tile on left (index 7)
    if (str(row-1) + ' ' + str(column-1)) in board["food"]:
        around.append(1)
    else:
        around.append(0) 

    return tuple(around)

def best_food_around(board_copy, position):
    """
    Checks the best food around a position.

    Parameters
    -------
    position : position of the central tile (str)
    board_copy : copy of board (dict)
   
    return
    -------
    position : position of the best food. (str) 

    version
    -------
    Specification : Virgile Devolder (v.1 08/04/2022)
    Implementation : Virgile Devolder (v.3 1/05/2022)
    """

    #gives in a list (around_ww) for each tile around if there are food or not
    around_ww = food_around(position, board_copy)

    #predefining two lists
    positions = []
    values = []

    #loop who adds in a list all foods around a positon
    for index, tile in enumerate(around_ww):
        if tile == 1:
            values.append(board_copy["food"][index_to_tile(position, index)][1])
            positions.append(index_to_tile(position, index))

    #return the position of the best food
    if values != []:
        return positions[values.index(max(values))]

    #return a emtpy string of no food around
    else:
        return ""

def index_to_tile(position, index):
    """
    Transforms a index into a tile.

    Parameters
    -------
    position : position of the central tile (str)
    index : index of the tile (int)

    return
    -------
    position : position of the tile. (str) 

    version
    -------
    Specification : Virgile Devolder (v.1 29/03/2022)
    Implementation : Virgile Devolder (v.1 29/03/2022)
    """

    #splits the position string into two integers (rows and columns)
    position = position.split(" ")
    position[0] = int(position[0])
    position[1] = int(position[1])

    #if the index is 0, it's the tile above
    if index == 0:
        position[0] -= 1 

    #if the index is 1, it's the top tile on the right
    elif index == 1:
        position[0] -= 1
        position[1] += 1

    #if the index is 2, it's the tile on the right
    elif index == 2:
        position[1] += 1

    #if the index is 3, it's the tile below on the right
    elif index == 3:
        position[0] += 1
        position[1] += 1

    #if the index is 4, it's the tile below
    elif index == 4:
        position[0] += 1
    
    #if the index is 5, it's the tile below on the left
    elif index == 5:
        position[0] += 1
        position[1] -= 1
    
    #if the index is 6, it's the tile on the left
    elif index == 6:
        position[1] -= 1

    #if the index is 7, it's the top tile on the left
    elif index == 7:
        position[0] -= 1
        position[1] -= 1

    #return the position in a string
    return str(position[0]) + " " + str(position[1])

def ww_around_alpha(board, team1, team2):
    """
    Gives a list of werewolves around alpha of team1.

    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team1 : team of the central werewolf (int)
    team2 : adeverse team (int)

    return
    -------
    near_alpha : werewolves around alpha of team one (list)

    version
    -------
    Specification : Nathan Lambrechts (v.1 28/04/2022)
    Implementation : Nathan Lambrechts (v.1 28/04/2022)
    """

    #list which will contain wolves near alpha
    near_alpha = []
    around_alpha = what_around(board["alpha"][team1-1], board, team1, team2)

    #the loop looks at which tiles around are occupied by allies, and notes these tiles in the list
    for index, tile in enumerate(around_alpha):
        if tile == 1:
            near_alpha.append(index_to_tile(board["alpha"][team1-1], index))

    return near_alpha

def position_ennemy(board, team2):
    """
    Gives the enemy's average position.

    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team2 : adeverse team (int)

    return
    -------
    position : enemy's average position (str)

    version
    -------
    Specification : Alexandre Wenkin (v.1 12/04/2022)
    Implementation : Alexandre Wenkin (v.1 12/04/2022)
    """

    #predefining two lists
    werewolves_r = []
    werewolves_c = []

    #loop that looks at each werewolf in adverse team on the game board
    for werewolf in board[team2]:

        #splits the position string into two integers (rows and columns)
        werewolf = werewolf.split(" ")
        r = int(werewolf[0])
        c = int(werewolf[1])

        #adds rows and columns in lists
        werewolves_r.append(r)
        werewolves_c.append(c)
    
    #average the positions of the opposing werewolves to establish a danger zone
    position_r_danger = round(sum(werewolves_r)/len(werewolves_r))
    position_c_danger = round(sum(werewolves_c)/len(werewolves_c))

    return str(position_r_danger)+ " " + str(position_c_danger)

def danger_level(board, team1, team2):
    """
    Gives an order of priorities on the boxes to be filled around the alpha to protect it, according to the position of the enemies.

    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team1 : team of the AI (int)
    team2 : adeverse team (int)

    return
    -------
    danger_around_alpha : list of distance between the tile and the central position of ennemy (list)

    version
    -------
    Specification : Mohamed Ait Hassou (v.1 12/04/2022)
    Implementation : Mohamed Ait Hassou (v.2 28/04/2022)
    """

    #take the enemy's average position
    position_danger = position_ennemy(board, team2)

    #predefining of one list
    danger_around_alpha = []

    #gives a danger level for each square around the alpha depending on the distance from the opponent
    for index in range(8):
        danger_around_alpha.append(distance(index_to_tile(board["alpha"][team1-1],index), position_danger))

    #the largest number (the least dangerous place) is replaced by an "inf", the omega will go on this box
    index = danger_around_alpha.index(max(danger_around_alpha))
    danger_around_alpha[index] = 10000

    #if a werewolf already occupies a space, we put the value 1000 there, so the space is no longer a priority
    around_alpha = what_around(board["alpha"][team1-1], board, team1, team2)
    for index, tile in enumerate(around_alpha):
        if tile == 1:
            danger_around_alpha[index] = 1000

    return danger_around_alpha
    
def find_best_food(board, team1):
    """
    Calls differents_foods() with differents type of food.

    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    team1 : team of the AI (int)

    return
    -------
    food : position of the best place to eat. (str)

    version
    -------
    Specification : Alexandre Wenkin (v.1 12/04/2022)
    Implementation : Alexandre Wenkin, Nathan Lambrechts (v.2 26/04/2022)
    """

    def differents_foods(name_food, board, team1):
        """
        Find the place with the most food nearby. 

        Parameters
        -------
        name_food : type of food (str)
        board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
        team1 : team of the AI (int)

        return
        -------
        food : position of the best place to eat. (str)

        version
        -------
        Specification : Alexandre Wenkin (v.1 26/04/2022)
        Implementation : Alexandre Wenkin, Nathan Lambrechts (v.1 26/04/2022)
        """

        #predefining of one list
        global_food = []

        #for each food
        for food in board['food']:

            #lists that will contain the positions (rows and columns)
            food_r = []
            food_c = []

            #predefining a list and two starting values
            food_value = []
            position_r_food = 0
            position_c_food = 0

            #looking for a central food (deers, rabbits, mice, apples or berries in order of priority)
            if board['food'][food][0] == name_food:

                #the food is the central position
                central = food
                
                #loop that finds the perfect position to put around the deer to enjoy a maximum of food
                for food2 in board["food"]:

                    #takes food into account in the calculation if it is at most two away
                    if distance(central, food2) <= 2:
                        food_separate = food2.split(" ")
                        food_r.append(int(food_separate[0]))
                        food_c.append(int(food_separate[1]))
                        food_value.append(board["food"][food2][1])

                #if no food around the central food, the position is that of the food
                if food_r == []:
                    global_food.append(central)

                #position average
                else:

                    #average that takes into account the position and value of each food source in the calculation
                    for index in range(len(food_value)):
                        position_r_food += (food_r[index]*food_value[index])  
                        position_c_food += (food_c[index]*food_value[index])
                    position_r_food = round(position_r_food/(sum(food_value)))
                    position_c_food = round(position_c_food/(sum(food_value)))

                    #add food position as str in global list
                    global_food.append(str(position_r_food)+ " " + str(position_c_food))

        #calculating the nearest food source to reach
        if global_food != []:

            #predefining a list that will contain the distances
            distances = []

            #fill in the list
            for group in global_food:
                distance_food = distance(board["alpha"][team1-1], group)
                distances.append(distance_food)

            #the final food is closest
            final_food = min(distances)
            index_final_food = distances.index(final_food)

            return global_food[index_final_food]  
        else:
            return []     

    #we start by looking around the deers
    result = differents_foods('deers', board, team1)
    
    #if no deer
    if result == []:

        #we continue by looking around the rabbits
        result = differents_foods('rabbits', board, team1)

        #if no rabbits
        if result == []:

            #we continue by looking around the mouse
            result = differents_foods('mice', board, team1)

            #if no mice
            if result == []:

                #we continue by looking around the apples
                result = differents_foods('apples', board, team1)

                #if no apple
                if result == []:

                    #we continue by looking around the berries
                    result = differents_foods('berries', board, team1)

                    #return berries
                    return result
                
                #return apples
                else:
                    return result

            #return mice
            else:
                return result

        #return rabbit
        else:
            return result

    #return deer
    else:
        return result

def several_index(list, element):
    """
    Find several index of an element in a list.

    Parameters
    -------
    list : elements in wich we search (list)
    element : element to find in the list (int)

    return
    -------
    all_index : index of the different appearances of the sought element, empty list if it does not appear (list)

    version
    -------
    Specification : Mohamed Ait Hassou (v.1 12/04/2022)
    Implementation : Mohamed Ait Hassou (v.1 12/04/2022)
    """

    #list that will contain the indexes
    all_index = []

    #loop that adds indexes of the element to a list
    for index ,tile in enumerate(list):
        if tile == element:
            all_index.append(index)
    
    #it returns the list if it is not empty, and none if she is
    if all_index != []:
        return all_index
    else:
        return []

def distance(position_1, position_2):
    """
    Find distance between two elements on board.

    Parameters
    -------
    position_1 : Position of the first element on the board. (str)
    position 2 : Position of the second element on the board. (str)

    return
    -------
    distance : distance between two elements on board. (int)

    version
    -------
    Specification : Virgile Devolder (v.2 25/02/2022)
    Implementation : Virgile Devolder (v.1 27/02/2022)
    """

    #separates in the string the two integers (x,y)
    position_1 = position_1.split(" ")
    position_2 = position_2.split(" ")

    #str to integer
    for index in range(2):
        position_1[index] = int(position_1[index]) 
        position_2[index] = int(position_2[index])
        
    #Tchebychev calculation
    return max(abs(position_1[0] - position_2[0]), abs(position_1[1] - position_2[1]))


#######################
#                     #
#    MAIN FUNCTION    #
#                     #
#######################


def get_AI_orders(board, type1, type2):
    """
    Give AI orders every turn.
    
    Parameters
    -------
    board : informations on team 1, on team 2, on food, on board's size, cases' background color, pixels details of each element, list of werewolves to print, list of food to print, turn to count turns without attack, alpha position. (dict)
    type1 : type of player one (human, AI, remote) (str)
    type2 : type of player two (human, AI, remtote) (str)

    return
    -------
    actions : actions of AI 1 (str)
    actions2 : actions of AI 2 (str)
    (actions1, actions2) : actions of AI one and two (tuple)
        
    version
    -------
    Specification : Virgile Devolder (v.1 17/02/2022)
    Implementation : Virgile Devolder, Alexandre Wenkin (v.4 01/05/2022)
    """
        
    #AI player 1
    if type1 == "AI" and type2 != "AI":
        iteration = 1
        team1, team2 = 1, 2

    #AI player 2
    if type2 == "AI" and type1 != "AI":
        iteration = 1
        team1, team2 = 2, 1

    #AI player 1 and 2
    if type1 == "AI" and type2 == "AI":
        iteration = 2
        team1, team2 = 1, 2

    #empty list that will contains orders
    full_actions = []

    #do 2 iterations if there are two AI
    for number_AI in range(iteration):

        #empty str that will contains orders of one AI
        actions = ""

        board_copy = deepcopy(board)

        #a werewolf can not do 2 actions the same turn
        board["already_action"] = []

        #change the team for the second AI
        if number_AI == 1:
            team1, team2 = 2, 1
        
        #checks what is around the alpha of the team
        around_alpha1 = what_around(board["alpha"][team1-1],board, team1, team2)

        #loop who looks if the alpha is with his 8 werewolves
        formation = 0
        for tile in around_alpha1:
            if tile == 1:
                formation += 1
        
        #loop to count ennemy's humans
        human = 0
        for ennemy in board[team2]:
            if 'human' in board[team2][ennemy][0]:
                human += 1
        
        #loop to count ally's humans
        human2 = 0
        for ally in board[team1]:
            if 'human' in board[team1][ally][0]:
                human2 += 1

        #best food on the map
        best_food = find_best_food(board, team1)

        #position of alpha
        r_alpha, c_alpha = board['alpha'][team1-1].split(" ")

        #if no attack during 126 turns
        if board["turn"] >= 126:
            actions = actions + no_ennemy_attack(board, board_copy, team1, team2)
            actions = actions + grouping(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)
            actions = actions + defense(board, board_copy, team1, team2)

        #if 
        elif board[team1][board["alpha"][team1-1]][1] <= 50:
            actions = actions + go_on_food(board, board_copy, team1, team2)
            actions = actions + defense(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)
            actions = actions + grouping(board, board_copy, team1, team2)

        #if 3 humans or more in adverse team or ennemy's alpha has less than 50 energy
        elif human >= 3 or board[team2][board['alpha'][team2-1]][1]< 50:
            actions = actions + final_attack(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)
            actions = actions + defense(board, board_copy, team1, team2)

        #if 3 humans or more in our team and our omega has enough life to pacify
        elif (human2 >= 3 and board[team1][board["omega"][team1-1]][1] >= 40) or (board[team1][board["alpha"][team1-1]][1] <= 50 and board[team1][board["omega"][team1-1]][1] >= 40):
            actions = actions + pacification(board, board_copy, team1)
            actions = actions + eat_around(board, board_copy, team1)
            actions = actions + defense(board, board_copy, team1, team2)

        #if formation is not good (8 werewolves around the alpha)
        elif formation != 8:
            actions = actions + grouping(board, board_copy, team1, team2)
            actions = actions + defense(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)

            if board["alpha"][team1-1] != best_food and best_food != []:
                actions = actions + go_on_food(board, board_copy, team1, team2)
                actions = actions + defense(board, board_copy, team1, team2)
                actions = actions + eat_around(board, board_copy, team1)

        #if the formation is not on the best food
        elif board["alpha"][team1-1] != best_food and best_food != []:
            actions = actions + go_on_food(board, board_copy, team1, team2)
            actions = actions + defense(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)

        #if the formation is on the best food
        elif board["alpha"][team1-1] == best_food:
            actions = actions + defense(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)

        elif best_food == []:
            actions = actions + final_attack(board, board_copy, team1, team2)
            actions = actions + eat_around(board, board_copy, team1)
            actions = actions + defense(board, board_copy, team1, team2)
        
        #append actions to the list
        full_actions.append(actions.strip())
        
    #if there are two AI, return a tuple with two str
    if type1 =='AI' and type2 == "AI":
        return tuple(full_actions)

    #return a str
    elif type1 == 'AI' and type2 != "AI":
        return str(full_actions[0])
    
    #return a str
    elif type2 == 'AI' and type1 != "AI":
        return str(full_actions[0])
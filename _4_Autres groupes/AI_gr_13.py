import random

def calculate_distance(x1, y1, x2, y2):
        """
        This function calculates the distance between 2 werewolves 
        
        Parameters : 
        ------------
        x1 : first row's position (int)
        y1 : first column's position (int)
        x2 : second row's position (int)
        y2 : second columns' position(int)
        
        Returns :
        ---------
        distance : distance between the two coordonates (int)

        Version :
        ---------
        Specification : Esteban Bernagou (v.1 10/03/2022)
        Implementation : Esteban Bernagou (v.1 10/03/2022)
        """


        distance = max(abs(x2-x1), abs(y2-y1))
        return distance

def get_AI_orders(game_dict, teams):
    """
    This function creates and controls the AI
    Parameters : 
    ------------
    game_dict : dictionnary based on the .ano file (dict)
    teams : name of the teams (team_1 or team_2) (str)

    Returns :
    ---------
    orders : orders of the AI (str) (list)

    Specification :
    ---------------
    Esteban Bernagou (v.1) - 02/05/2022

    Implementation :
    ----------------
    The whole group (v.5) - 01/05/2022
    """
    
    orders = ''

    #We give the teams :
    #------------------#

    if teams == "team_1":
        team = "team_2"
    else:
        team = "team_1"

    for werewolves_a in game_dict['werewolves'][teams] :


        #Implementation of low-level functions :
        #--------------------------------------#

        def get_target(target_dict):
            """
            This function is used to find the nearest_target of the werewolves who attacks/ want to eat

            Parameters :
            ------------
            target_dict : dictionnary within is the target (dict)
            distance_dict : dictionnary whick take in keys the distance between the werewolf who attacks/ want to eat and his target and in values the position of the target (dict)
            distance_list : list of all the distances between the werewolf who attacks/ want to eat and his target (list)
            
            Returns :
            ---------
            target : position of the target (tuple)
            distance_target : distance between the werewolf who attacks/ want to eat and his target (int)
            
            """
            distance_dict = {}
            distance_list = []
            for target in target_dict:

                if target not in game_dict['foods']:
                    if game_dict['werewolves'][team][target][0] == 'normal' or game_dict['werewolves'][team][target][0] == 'omega' or game_dict['werewolves'][team][target][0] == 'alpha':
                        distance = calculate_distance(werewolves_a[0], werewolves_a[1],target[0],target[1])
                        distance_dict[distance] = target
                        distance_list.append(distance)
                else:
                        distance = calculate_distance(werewolves_a[0], werewolves_a[1],target[0],target[1])
                        distance_dict[distance] = target
                        distance_list.append(distance)

            if len(distance_list) > 1:
                min_distance = min(*distance_list)
            else:
                min_distance = distance_list[0]

            target = distance_dict[min_distance]
            distance_target = calculate_distance(werewolves_a[0], werewolves_a[1], target[0], target[1])
            return target, distance_target

        def find_the_ways(target):
            """
            This function finds the better way to join the target

            Parameters:
            -----------
            target : position of the target (tuple)

            Returns:
            --------
            best_ways_list : list of all the best_ways to join the target (list)
            
            """

            #Creates the list of all the possibles ways :
            #-------------------------------------------#
            possible_way_list = []
            for x in range(-1, 2):
                for y in range (-1, 2):
                    new_position = werewolves_a[0] + x, werewolves_a[1] + y 

                    if new_position not in game_dict['werewolves']['team_1'] and new_position not in game_dict['werewolves']['team_2'] and new_position[0] > 0 and new_position[1] > 0:
                        possible_way_list.append(new_position)

            distance = calculate_distance(werewolves_a[0], werewolves_a[1], target[0], target[1])

            best_ways_list = []
            for new_position in possible_way_list:
                new_distance = calculate_distance(new_position[0], new_position[1], target[0], target[1])
                
                if new_distance == distance or new_distance == distance - 1:
                    best_ways_list.append(new_position)
            
            return best_ways_list

        #IA Principal :
        #-------------#

        ispacify = False
        w_energy = game_dict['werewolves'][teams][werewolves_a][1]
        distance_dict = {}
        distance_list = []
        symbol_2 = ':@'

        #Fight part if hp >= 50:
        #----------------------#

        if w_energy > 50 or (w_energy < 50 and len(game_dict['foods']) == 0):
            
            symbol = ':*'
            target_dict = game_dict['werewolves'][team]
            pacify_list = []

            #Werewolves in omega's range :
            #----------------------------#

            for target in target_dict:
                distance = calculate_distance(werewolves_a[0], werewolves_a[1],target[0],target[1])
                distance_dict[distance] = target
                distance_list.append(distance)

                if distance in range(0, 7):
                    pacify_list.append(distance)
            
            #Conditions to pacify :
            #---------------------#

            if w_energy >= 60 and game_dict['werewolves'][teams][werewolves_a][0] == 'omega' and  len(pacify_list) >= 3 :
                symbol = ':pacify'
                ispacify = True
                
                order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol
                orders += order + ' ' 

            if ispacify == False:
                
                target, distance_target = get_target(target_dict)
                
                if distance_target == 1 and target not in game_dict['werewolves'][teams]:

                    #Order to attack :
                    #----------------#

                    order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol + str(target[0]) + '-' + str(target[1])
                    orders += order + ' '

                else: 
                    
                    #Order to move :
                    #--------------#

                    best_ways_list = find_the_ways(target)
                    the_way = True
                    if len(best_ways_list)>0 :
                        if len(best_ways_list) > 1:
                            for ways in best_ways_list:
                                if calculate_distance(ways[0],ways[1], target[0], target[1]) == distance_target - 1:
                                    the_way = ways
                            if the_way != True:
                                order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol_2 + str(the_way[0]) + '-' + str(the_way[1])
                            else:
                                order = ''
                        else:
                            the_way = best_ways_list[0]
                            order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol_2 + str(the_way[0]) + '-' + str(the_way[1])
                    else:
                        order = ''
                    
                    if order != '':
                        orders += order + ' '
                    else:
                        orders += order

        #Feed part if hp < 50:
        #--------------------#

        elif w_energy <= 50 and len(game_dict['foods']) > 0:    

            symbol = ':<'
            target_dict = game_dict['foods']

            target, distance_target = get_target(target_dict)

            if distance_target <= 1:

                #Order to feed :
                #--------------#

                order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol + str(target[0]) + '-' + str(target[1])
                orders += order + ' '

            else: 

                best_ways_list = find_the_ways(target)
                
                #Order to move :
                #--------------#

                if len(best_ways_list)>0:
                    if len(best_ways_list) > 1:
                        the_way = random.choices(best_ways_list)
                        order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol_2 + str(the_way[0][0]) + '-' + str(the_way[0][1])
                    else:
                        the_way = best_ways_list[0]
                        order = str(werewolves_a[0]) + '-' + str(werewolves_a[1]) + symbol_2 + str(the_way[0]) + '-' + str(the_way[1])
                else:
                    order = ''
                
                if order != '':
                    orders += order + ' '
                else:
                    orders += order
    order = orders.strip(' ')
    return orders
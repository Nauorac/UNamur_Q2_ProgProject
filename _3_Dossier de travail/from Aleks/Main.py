import random, blessed 


def start_game(maplink, player2type):

    """ This function starts the game.
        Parameters
        -------------
            maplink : link to the map file: str;
            player2type: 0 if it's a human and 1 if it's a IA: bool;
        Return :
        --------
            
        Notes :
        -------
            This function starts the game
        Version
        -------------
    """
    turn = 0
    game_state = True
    map_creation(maplink)
    creation(ants, carte, turn)
    map_update(game_map,map_size,ant)
   


    while game_state == True:
        
        turn =+ 1
        clod_orders = []
        attack_orders = []
        movement_orders = []

        print(" Phase 1 donner vos ordres :")
        for i in range(2):
            raw_orders = input("Joueur %d donner la liste de vos ordres" %(i+1) )

            if not raw_orders == "next": 
                orders_list = raw_orders.split(" ")
                
                for order in orders_list:
                    if (order.find("lift") > -1 ):
                        clod_orders.append(order)
                    elif (order.find("drop") > -1) :
                        clod_orders.append(order)
                    elif (order.find("*") > -1 ):
                        attack_orders.append(order)
                    elif (order.find("@") > -1):
                        movement_orders.append(order)
                    else : 
                        print(order + "est un ordre non valide.")

        
        print(" Phase 2 : Execution des actions sur les mottes de terre.")
        
        clod_action(clod_orders, ants, carte)
        
        print("Phase 3 : Execution des actions d'attaques.")
        
        attack(attack_orders, ants, carte)

        print(" Phase 4 : Execution des actions de mouvement.")
        
        move(movement_orders, ants, carte)

        if (turn % 5) == 0 :
            print(" Phase 5 : création des nouvelle fourmie.")

            creation(ants, carte, turn)

        game_state = end_game(clod_orders, ants, carte)
    return()

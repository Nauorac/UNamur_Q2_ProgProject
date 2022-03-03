
entities = {(2, 1): [1, "alpha", 60], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, "deers", 100]}

"""
orders_P1 = "  10-10:@10-11   12-10:*12-11 19-20:*20-20  2-1:<2-4  12-72:<27-48 17-20:pacify"
orders_P2 = "7-10:<8-11 22-10:@12-11 19-20:*14-15 45-99:pacify"
"""

orders_P1 = "2-1:<4-4"
orders_P2 = ""

def entity_at(entity_coords):  # VALIDE
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2]]

#fct test feed
def feed(list):
    #is_ww = entity_at(list[0])
    # Comme la ligne ci-dessous fonctionne on peut supprimer la fonction entity_at
    is_ww = entities[list[0]]
    is_food = entities[list[1]]
    if is_food and is_food[0] == 0:
        if is_ww and is_ww[0] == 1:
            if is_ww[2] < 100:
                food_E = is_food[2]
                ww_E = is_ww[2]
                toteaten = 0
                while (food_E > 0) and (ww_E < 100):
                    food_E -= 1
                    ww_E += 1
                    toteaten += 1
                if food_E == 0:
                    print("The "+is_food[1]+" have been completely eaten.")
                    entities.pop(list[1])
                else:
                    is_food[2] = food_E
                is_ww[2] = ww_E
                entities.update({list[1]: is_food})
                entities.update({list[0]: is_ww})
                print("The werewolf at "+str(list[0])+" has eat "+str(toteaten)+" energy from "+str(entities[list[1]][1])+" at "+str(list[1])+".")
            else:
                print("Your werewolf energy is already at max.")
    else:
        print("This is not food.")



#fct test pacify


def pacify(list):
    ...
    print(list)

#fct test bonus
def bonus(list):
    print(list)

#fct attack feed
def attack(list):
    ...
    print(list)

#fct move feed
def move(list):
    ...
    print(list)

def hacher(string):
    ordre = string
    #print(ordre)
    #Split gauche droite
    gd = ordre.split(":")
    #Split origine X et origine Y
    c = gd[0].split("-")
    #Création de la liste avec les coordonnées d'origine X, Y
    origine = (int(c[0]), int(c[1]))
    #Test si l'ordre est pacify
    if gd[1] == "pacify":
        order_type = gd[1]
        hach_order = [origine]
    else:
        #Sinon débute le split des coordonnées de destination
        e = gd[1].split("-")
        z = e[0][1:]
        order_type = e[0][0]
        destination = (int(z), int(e[1]))
        hach_order = [order_type, origine, destination]
    return hach_order


"""
==========================================================
                    ORDERS MANAGER
========================================================
    """
def orders_manager(orders_P1, orders_P2):
    # Convert Player 1 orders in a list
    cleanP1 = orders_P1.split()
    # Convert Player 2 orders in a list
    cleanP2 = orders_P2.split()
    # Initialize lists of differents orders for each players.
    pacify_P1 = []
    pacify_P2 = []
    feeds_orders_P1 = []
    feeds_orders_P2 = []
    attacks_orders_P1 = []
    attacks_orders_P2 = []
    move_orders_P1 = []
    move_orders_P2 = []

    # Populate lists orders for player 1
    i = 0
    while i < len(cleanP1):
        current_order = cleanP1[i]
        listcurord = hacher(current_order)
        #print(listcurord)
        # Il faut rajouter pour chaque ordre un check afin de s'assurer que le ww est bien de la bonne équipe
        # if entity_at(listcurord[1])[0] == 1
        if listcurord[0] == "<":
            feeds_orders_P1.append(listcurord)
        elif listcurord[0] == "*":
            attacks_orders_P1.append(listcurord)
        elif listcurord[0] == "@":
            move_orders_P1.append(listcurord)
        else:
            pacify_P1.append(listcurord)
        i += 1
    # Populate lists orders for player 2
    i = 0
    while i < len(cleanP2):
        current_order = cleanP2[i]
        listcurord = hacher(current_order)
        if listcurord[0] == "<":
            feeds_orders_P2.append(listcurord)
        elif listcurord[0] == "*":
            attacks_orders_P2.append(listcurord)
        elif listcurord[0] == "@":
            move_orders_P2.append(listcurord)
        else:
            pacify_P2.append(listcurord)
        i += 1

    # --------------------
    # --- PACIFY PHASE ---
    # --------------------
    # Check if Player 1 given pacify order and run it.
    if len(pacify_P1) > 0:
        print("Player 1 pacify phase.")
        while len(pacify_P1) > 0:
            pacify(pacify_P1[0])
            pacify_P1.pop(0)
    # Check if Player 2 given pacify order and run it.
    if len(pacify_P2) > 0:
        print("Player 2 pacify phase.")
        while len(pacify_P2) > 0:
            pacify(pacify_P2[0])
            pacify_P2.pop(0)
    # ---------------------
    # --- BONUSES PHASE ---
    # ---------------------
    #bonuses(P1)
    # Il faut créer une liste (ou sous-dictionnaire) avec tout les ww du Player 1
    # Puis while sur cette liste et envoyer à fct bonuses
    #def make_team_P1():
    team1 = {}
    for key, values in entities.items():
        if values[0] == 1:
            #ajouter au dictionnaire team1
            team1.update({key:values})
    if len(team1) > 0:
        print("Player 1 bonus phase.")
        for keys in team1:
            # Je ne parviens pas à acceder et retirer du dico
            coords = [keys]
            bonus(coords)


    #bonuses(P2)
    team2 = {}
    for key, values in entities.items():
        if values[0] == 1:
            #ajouter au dictionnaire team2
            team2.update({key: values})
    if len(team2) > 0:
        print("Player 2 bonus phase.")
        for keys in team2:
            # Je ne parviens pas à acceder et retirer du dico
            coords = [keys]
            bonus(coords)


    # ------------------
    # --- FEED PHASE ---
    # ------------------
    # Check if Player 1 given feeds orders and run them.
    if len(feeds_orders_P1) > 0:
        print("Player 1 feed phase.")
        #print(feeds_orders_P1)
        while len(feeds_orders_P1) > 0:
            feed(feeds_orders_P1[0][1:3])
            feeds_orders_P1.pop(0)
    # Check if Player 2 given feeds orders and run them.
    if len(feeds_orders_P2) > 0:
        print("Player 2 feed phase.")
        while len(feeds_orders_P2) > 0:
            feed(feeds_orders_P2[0][1:3])
            feeds_orders_P2.pop(0)

    # --------------------
    # --- ATTACK PHASE ---
    # --------------------
    # Check if Player 1 given attacks orders and run them.
    if len(attacks_orders_P1) > 0:
        print("Player 1 attack phase.")
        while len(attacks_orders_P1) > 0:
            attack(attacks_orders_P1[0][1:3])
            attacks_orders_P1.pop(0)
    # Check if Player 2 given attacks orders and run them.
    if len(attacks_orders_P2) > 0:
        print("Player 2 attack phase.")
        while len(attacks_orders_P2) > 0:
            attack(attacks_orders_P2[0][1:3])
            attacks_orders_P2.pop(0)

    # ------------------
    # --- MOVE PHASE ---
    # ------------------
    # Check if Player 1 given move orders and run them.
    if len(move_orders_P1) > 0:
        print("Player 1 move phase.")
        while len(move_orders_P1) > 0:
            move(move_orders_P1[0][1:3])
            move_orders_P1.pop(0)
    # Check if Player 2 given move orders and run them.
    if len(move_orders_P2) > 0:
        print("Player 2 move phase.")
        while len(move_orders_P2) > 0:
            move(move_orders_P2[0][1:3])
            move_orders_P2.pop(0)

    #return = (game_turns += 1)

orders_manager(orders_P1, orders_P2)





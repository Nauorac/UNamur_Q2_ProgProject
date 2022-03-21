

size = (20, 20)
entities = {(2, 2): [1, 'alpha', 100, 0], (1, 1): [1, 'omega', 100, 0], (1, 2): [1, 'normal', 100, 0], (2, 1): [1, 'normal', 100, 0], (1, 3): [1, 'normal', 100, 0], (2, 3): [1, 'normal', 100, 0], (3, 3): [1, 'normal', 100, 0], (3, 2): [1, 'normal', 100, 0], (3, 1): [1, 'normal', 100, 0],
            (19, 19): [2, 'alpha', 100, 0], (20, 20): [2, 'omega', 100, 0], (20, 19): [2, 'normal', 100, 0], (19, 20): [2, 'normal', 100, 0], (20, 18): [2, 'normal', 100, 0], (19, 18): [2, 'normal', 100, 0], (18, 18): [2, 'normal', 100, 0], (18, 19): [2, 'normal', 100, 0], (18, 20): [2, 'normal', 100, 0],
            (4, 4): [0, 'berries', 10, 0], (4, 5): [0, 'berries', 10, 0], (5, 4): [0, 'berries', 10, 0], (5, 5): [0, 'berries', 10, 0], (16, 16): [0, 'berries', 10, 0], (16, 17): [0, 'berries', 10, 0], (17, 16): [0, 'berries', 10, 0], (17, 17): [0, 'berries', 10, 0], (1, 4): [0, 'apples', 30, 0], (1, 5): [0, 'apples', 30, 0], (20, 16): [0, 'apples', 30, 0], (20, 17): [0, 'apples', 30, 0], (4, 1): [0, 'mice', 50, 0], (5, 1): [0, 'mice', 50, 0], (16, 20): [0, 'mice', 50, 0], (17, 20): [0, 'mice', 50, 0], (5, 7): [0, 'rabbits', 100, 0], (7, 5): [0, 'deers', 500, 0], (16, 14): [0, 'rabbits', 100, 0], (14, 16): [0, 'deers', 500, 0]}

test = {(9, 11): [1, "normal", 100],
        (9, 13): [1, "alpha", 100],
        (6, 14): [1, "normal", 100],
        (8, 10): [1, "normal", 100],
        (7, 9): [2, "normal", 100],
        (6, 8): [2, "alpha", 100],
        (10, 9): [0, "rabbits", 100]
        }

def in_range(range, ww_coord):  # Spec 100 % and Code 100%
    nbr_entity = 0
    ww_in_range = {}
    key = []
    for key, values in test.items():
        #Test if entity is a werewolf
        if values[0] == 1 or values[0] == 2:
            x = abs(key[0]-ww_coord[0])
            y = abs(key[1]-ww_coord[1])
            if x == 0 and y == 0:
                ...  # current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key: values})
    return ww_in_range

"""
    =================================
                    A.I. ENGINE
    =================================
"""


"""
PHASE 1 - Deploiement - Mise en boule

==> Si alpha à moins de 3 cases d'un mur
==> Identifier le mur le plus proche (et placer l'alpha a 3 cases.)
==> Mettre les autres loups autours en laissant l'espace vide à l'opposé du max d'ennemi
==> Envoyer l'omega a plus de 6 cases.

PHASE 2 - Progression
    Meute
==> Viser l'alpha ennemi
==> Bouger en meute
    Omega
==> S'éloigner de la meute et vise à pacifier le max d'ennemi


Savoir dans quelle direction aller.
1) Analyse environnement
    - Boucler des in_range jusqu'a trouver un ennemi.
"""
def find(i, coords):
    #Trouver un ennemi
    team = test[coords][0]
    dict_entity = in_range(i, coords)
    target = ()
    # Si entités et pas de de cible
    if len(dict_entity) > 0 and len(target) == 0:
        for key in dict_entity:
            if dict_entity[key][0] != team:
                t = (key[0], key[1])
                target = target + t
    # Si pas de cible
    if len(target) == 0 or len(dict_entity) == 0:
        i += 1
        find(i, coords)
    else:
        print(target)
        return target


def find_ennemy_alpha(i, coords, *target):
    #Trouver un ennemi
    team = test[coords][0]
    dict_entity = in_range(i, coords)
    target = ()
    while len(target) == 0:
        # Si pas de cible et pas d'entités
        if len(dict_entity) == 0:
            i += 1
            find(i, coords)
        # Si entités et pas de de cible
        for key in dict_entity:
            # Si team différente et alpha
            if (dict_entity[key][0] != team) and (dict_entity[key][1] == "alpha"):
                t = (key[0], key[1])
                target = target + t
        i += 1
        find(i, coords)
        else:
            print(target)
            return target

def direction(orig, dest):
    #determiner la direction à prendre et les coords pour y aller
    #pathfinding
    xo = orig[0]
    yo = orig[1]
    xd = dest[0]
    yd = dest[1]
    xstep = 0
    ystep = 0

    if xd-xo < 0:
        #Haut
        xstep = -1
    elif xd-xo > 0:
        #Bas
        xstep = +1
    elif xd-xo == 0:
        # Deplacement vertical
        xstep = 0

    if yd-yo < 0:
        #Gauche
        ystep = -1
    elif yd-yo > 0:
        #Droite
        ystep = +1
    elif yd-yo == 0:
        # Deplacement horizontal
        ystep = 0
    #Return les coords de destination pour atteindre la cible
    coords = (xo+xstep, yo+ystep)
    #Etape 2, éviter les obstacles
    if coords in test:
        print("Obstacle")
    return coords




#cible = ()
#cible = cible + find(1, (9, 11))
#cible = find(1, (9, 11))
print("Target : "+str(find(1, (9, 11)))+"")

print("Test Pathfinding")
print(direction((9, 11), (7, 9)))

print("Ennemy alpha at : ")
find_ennemy_alpha(1, (9, 11))

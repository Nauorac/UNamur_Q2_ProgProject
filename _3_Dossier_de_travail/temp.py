entities = {(7, 11): [0, 1, 100], (6, 10): [0, 1, 100],
            (6, 12): [0, 1, 100], (8, 12): [0, 1, 100]}

def change_path(path):  # Spec and Code 100%
    """
    Description of the function
    ---------------------------
    Function that ask with inputs to select the file path.

    Returns:
    --------
    string : Return the path of the file
    """
    with term.cbreak():
        print("Please enter the path of the file : ")
        path = term.inkey()
        return path

def data_import(path, size, entities):  # Spec and Code 100%
    """
	Description
	---------------------------
    Update the size tuple and the entities dictionary with data in a ano file.

    Args:
    -----
    path : filepath of the .ano file  - str
    size : Tuple with 2 elements, raw number and column number - tuple
    entities : Dictionnary that contains all elements on the boardgame - dict

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 11/03/2022)
	Code : Trésor Tchientcheu (v.3.0 - 25/04/2022)
	"""
    file = open(path, "r")
    liste = file.readlines()
    for i in range(len(liste)):
        # Detect if line contains boardgame size
        if ("map" in liste[i]):
            j = i+1
            si = liste[j].split(" ")
            size = [int(si[0]), int(si[1])]
            j = i+1
        elif ("werewolves" in liste[i]):
            j = i+1
            while liste[j] != "foods:\n":
                a = liste[j].split(" ")
                b = a[3].split("\n")
                entities[int(a[1]), int(a[2])] = [int(a[0]), (b[0]), 100, 0]
                j = j+1
        elif ("foods" in liste[i]):
            j = i+1
            while j < len(liste):
                a = liste[j].split(" ")
                b = a[2].split("\n")
                entities[int(a[0]), int(a[1])] = [0, (b[0]), int(a[3])]
                j = j+1
    return path, size, entities

#path, size, entities = data_import(path, size, entities)

def distance(position_x1, position_y1, position_x2, position_y2):
    if abs(position_x2 - position_x1) > abs(position_y2-position_y1):
        return abs(position_x2-position_x1)
    else:
        return abs(position_y2-position_y1)

def target_Ealpha(Px):
    pos_alpha_ennemi = []
    for cle in entities:
        # Check if it's an opposite alpha of the entities in argument
        if(entities[cle][0] != Px and entities[cle][0] != 0 and entities[cle][1] == "alpha"):
            pos_alpha_ennemi.append(cle[0])
            pos_alpha_ennemi.append(cle[1])
    return pos_alpha_ennemi

def direction(ww_pos, pos_alpha_ennemi):

    if pos_alpha_ennemi[0] > ww_pos[0]:
        x = 1
    elif pos_alpha_ennemi[0] < ww_pos[0]:
        x = -1
    elif pos_alpha_ennemi[0] == ww_pos[0]:
        x = 0

    if pos_alpha_ennemi[1] > ww_pos[1]:
        y = 1
    elif pos_alpha_ennemi[1] < ww_pos[1]:
        y = -1
    elif pos_alpha_ennemi[1] == ww_pos[1]:
        y = 0
    ww_pos[0] += x
    ww_pos[1] += y
    return ww_pos

"""
- Faire un dic avec les loups de la team
- Boucle
    -- Check si loup a deja fait son action
        ==> Non
            -- check si place vide
                    -- Si oui bouger vers alpha ennemi
                    -- Si non mettre un flag pour attendre place vide
        ==> Oui suivant sauf si nombre de loups ayant effectués leur actions = 7 (ou9)
"""


def empty_place(ww_pos):
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

print(empty_place((7, 11)))
# Réponse attendue 5 valeurs = [(6, 11), (7, 10), (7, 12), (8, 10), (8, 11)]

import random
from turtle import position
teams={(2, 2): [1, 'normal', 100, False],
    (4, 20): [1, 'alpha', 100 ],(1, 2): [1, 'normal', 10],  
    (4, 19): [1, 'normal', 100 ], (1, 3): [1, 'normal', 100], 
    (2, 3): [1, 'normal', 100], (3, 3): [1, 'normal', 100], (3, 2): [1, 'omega', 100], 
    (3, 1): [1, 'normal', 100, False],
    
    (5,19): [2, 'normal', 100], 
    (2,19): [2, 'omega', 100], (3, 5): [2, 'normal', 100], (5,5): [2, 'normal', 100],
    (5, 2): [2, 'normal', 100], 
    (3, 4): [2, 'normal', 100], (5, 3): [2, 'normal', 100], (18, 20): [2, 'normal', 100],
    (4, 4): [0, 'berries', 10], (1, 2): [0, 'berries', 10], (5, 4): [0, 'berries', 10], (5, 5): [0, 'berries', 10], 
    (16, 16): [0, 'berries', 10], (16, 17): [0, 'berries', 10], (17, 16): [0, 'berries', 10], (17, 17): [0, 'berries', 10], 
    (1, 4): [0, 'apples', 30], (1, 5): [0, 'apples', 30], (20, 16): [0, 'apples', 30], (20, 17): [0, 'apples', 30],
    (4, 1): [0, 'mices', 50], (5, 1): [0, 'mices', 50], (16, 20): [0, 'mices', 50],
    (17, 20): [0, 'mices', 50], (5, 7): [0, 'rabbits', 100], (7, 5): [0, 'deers', 500], (16, 14): [0, 'rabbits', 100], (14, 16): [0, 'deers', 500]
    } 
row=20
col=20

def entity_at(entities,entity_coords): # Spec 100 % and Code 100%
 
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2]]
    return False

def in_range(entities,range, omega_coord):  # Spec 100 % and Code 100%
    nbr_entity = 0
    ww_in_range = {}
    key = []
    #print(omega_coord)
    for key, values in entities.items():
        #Test if entity is a werewolf
        if values[0] != 0:
            #print(omega_coord[0])
            x = abs((key[0]) - (omega_coord[0]))
            y = abs((key[1]) - (omega_coord[1]))
            if x == 0 and y == 0:
                ...  # current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key: values})
    return ww_in_range


def Ai(teams,equipe):
    #recuperer l'ensemble des ennemies et des amis qui son autour de mon alpha
    #recupere la position de mon alpha et alpha ennemi 
    position_alpha=[]
    position_alpha_ennemi=[]
    ami_alpha=[]
    ennemi_alpha=[]
    for cle in teams:
        if teams[cle][0]== equipe and teams[cle][1]== "alpha":  
            position_alpha.append(cle[0])
            position_alpha.append(cle[1])
        elif(teams[cle][0]!= equipe and teams[cle][1]== "alpha"):
            position_alpha_ennemi.append(cle[0])
            position_alpha_ennemi.append(cle[1])
    #recupere les alentour de mon alpha dictionnaire des loup ami est ennemi 
    
    dic_loup=in_range(teams,1,position_alpha)
    for cle in dic_loup:
        if dic_loup[cle][0]==equipe:
            ami_alpha.append([cle[0],cle[1]])
        else:
            ennemi_alpha.append([cle[0],cle[1]])
    
    if ((position_alpha[0],position_alpha[1]) in  teams[(position_alpha[0],position_alpha[1])][2]<100):   #verifier si mon loup alpha est sur une ressource et il a un manque d'enrgie 
        return str(position_alpha[0]) +"-" + str(position_alpha[1])+":<" + str(position_alpha[0]) + "-" + str(position_alpha[1])

    else: # traiter le cas ou le loup est n'est pas sur une ressource ou il assez d'energie 
        
        if (ennemi_alpha==[]):#verifier  si on a pas de loup ennemie a cote de nous 
            if position_alpha_ennemi[0]> position_alpha[0]:
                x= position_alpha[0]+1
            elif position_alpha_ennemi[0]< position_alpha[0]:
                x= position_alpha[0]-1
            elif position_alpha_ennemi[0]== position_alpha[0]:
                x= position_alpha[0]
            elif position_alpha_ennemi[1]> position_alpha[1]:
                y= position_alpha[0]+1
            elif position_alpha_ennemi[1]< position_alpha[1]:
                y= position_alpha[0]-1
            elif position_alpha_ennemi[1]== position_alpha[1]:
                y= position_alpha[0]+1
            return str(position_alpha[0])+"-"+ str(position_alpha[1]) +":@"+ str(x)+"-"+str(y)

        else: #le cas ou on des les loups ennemis qui nous entour

            for i in ennemi_alpha:
                if teams[(i[0],i[1])][1]=="alpha":
                    return str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(i[0])+"-"+ str(i[1])
            z= random.choice(ennemi_alpha)
            return str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(z[0])+"-"+ str(z[1])


def structure(map_path): # Spec and Code 100%
    entities={}
         
    file = open (map_path,"r")
    liste=file.readlines()

    for i in range(len(liste)):
    
        if   ( "werewolves" in liste[i] ) :
            j=i+1
            while liste[j]!="foods:\n":
                a=liste[j].split(" ")
                b=a[3].split("\n")
                entities[int(a[1]),int(a[2])]= [int(a[0]),(b[0]),100]
                j=j+1
        if ( "foods" in liste[i] ) :
            j=i+1
            while j<len(liste):
                a=liste[j].split(" ")
                b=a[2].split("\n")
                entities[int(a[0]),int(a[1])]= [0,(b[0]),int(a[3])]
                j=j+1
    return entities
            

     

struct=structure("./Users/treso/Desktop/map.ano")
print(struct)
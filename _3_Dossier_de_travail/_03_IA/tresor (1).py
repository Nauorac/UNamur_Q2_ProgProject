import random

teams={(2, 2): [1, 'normal', 100],
    (7, 20): [1, 'alpha', 100 ],
    (1, 2): [1, 'normal', 10], 
    (4, 19): [1, 'normal', 100 ], 
    (1, 3): [1, 'normal', 100], 
    (2, 3): [1, 'normal', 100], 
    (3, 3): [1, 'normal', 100], 
    (10, 2): [1, 'omega', 100], 
    (3, 1): [1, 'normal', 100],

    (9, 20): [2, 'alpha', 100 ],
    (9,2): [2, 'omega', 100], 
    (8,2): [2, 'normal', 100],  
    (7, 19): [2, 'normal', 100], 
    (10,3): [2, 'normal', 100],
    (10, 4): [2, 'normal', 100], 
    (8, 5): [2, 'normal', 100], 
    (5, 3): [2, 'normal', 100], 
    (18, 20): [2, 'normal', 100],

    } 
row=20
col=20

def distance(position_x1, position_y1, position_x2, position_y2):
    
    if abs(position_x2- position_x1 )>abs(position_y2-position_y1):
        return abs(position_x2-position_x1)
    else:
        return abs(position_y2-position_y1)

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
            x = abs(key[0] - omega_coord[0])
            y = abs(key[1] - omega_coord[1])
            if x == 0 and y == 0:
                ...  # current = omega
            elif (x <= range) and (y <= range):
                nbr_entity += 1
                ww_in_range.update({key: values})
    return ww_in_range

#print(in_range(teams,1,(4, 20)))

def Ai(teams,equipe):
    #recuperer l'ensemble des ennemies et des amis qui son autour de mon alpha
    #recupere la position de mon alpha et alpha ennemi 
    position_alpha=[]
    position_alpha_ennemi=[]
    ami_alpha=[]
    ennemi_alpha=[]
    ami_omega=[]
    ennemi_omega=[]
    position_omega=[]
    
    ordre_alpha=""
    ordre_omega=""

    for cle in teams:
        
        if teams[cle][0]== equipe and teams[cle][1]== "alpha":  
            
            position_alpha.append(cle[0])
            position_alpha.append(cle[1])
        elif(teams[cle][0]!= equipe and teams[cle][0]!= 0 and teams[cle][1]== "alpha"):
            position_alpha_ennemi.append(cle[0])
            position_alpha_ennemi.append(cle[1])
        elif teams[cle][0]== equipe and teams[cle][1]== "omega":  
            position_omega.append(cle[0])
            position_omega.append(cle[1])
        
    
    #recupere les alentour de mon alpha dictionnaire des loup ami est ennemi 
    #alpha
    dic_loup=in_range(teams,1,position_alpha)
    
    for cle in dic_loup:
        if dic_loup[cle][0]==equipe:
            ami_alpha.append([cle[0],cle[1]])
        else:
            ennemi_alpha.append([cle[0],cle[1]])
    
    if (teams[(position_alpha[0],position_alpha[1])][2]<100): 
        for cle in teams:
            
            if(teams[(cle[0],cle[1])][0]==0 and distance(position_alpha[0],position_alpha[1],cle[0],cle[1])==1 ):  #verifier si mon loup alpha est sur une ressource et il a un manque d'enrgie 
                ordre_alpha= str(position_alpha[0]) +"-" + str(position_alpha[1])+":<" + str(cle[0]) + "-" + str(cle[1])

    else: # traiter le cas ou le loup est n'est pas a cote une ressource ou il assez d'energie 
        x="" 
        y=""
        if (ennemi_alpha==[]):#verifier  si on a pas de loup ennemie a cote de nous
            
            if position_alpha_ennemi[0]> position_alpha[0]:
                x= position_alpha[0]+1
            elif position_alpha_ennemi[0]< position_alpha[0]:
                x= position_alpha[0]-1
            else: 
                x= position_alpha[0]

            if position_alpha_ennemi[1]> position_alpha[1]:
                y= position_alpha[0]+1
            elif position_alpha_ennemi[1]< position_alpha[1]:
                y= position_alpha[0]-1
            else :
                y= position_alpha[1]
              
            ordre_alpha= str(position_alpha[0])+"-"+ str(position_alpha[1]) +":@"+ str(x)+ "-" + str(y)

        else: #le cas ou on des les loups ennemis qui nous entour

            
            for i in ennemi_alpha:
                if teams[(i[0],i[1])][1]=="alpha":
                    ordre_alpha= str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(i[0])+"-"+ str(i[1])
            z= random.choice(ennemi_alpha)
            
            ordre_alpha= str(position_alpha[0]) +"-" + str(position_alpha[1])+ ":*" +str(z[0])+"-"+ str(z[1])
            
    #ordre omega

    if (teams[(position_omega[0],position_omega[1])][2]<40): #le cas ou notre loup omega n'a pas assez d'energie pour pacifier
        dic_loup=in_range(teams,1,position_omega)
        for cle in dic_loup:
            if dic_loup[cle][0]==equipe:
                ami_omega.append([cle[0],cle[1]])
            else:
                ennemi_omega.append([cle[0],cle[1]])
        if ennemi_omega!=[]: # le cas ou notre loup omega a des ennemis qui l'entour 
            if position_alpha_ennemi in ennemi_omega:
                ordre_omega= str(position_omega[0]) +"-" + str(position_omega[1])+":*"+str(position_alpha_ennemi[0])+"-"+ str(position_alpha_ennemi[1])
            else:
                position=random.choice(ennemi_omega)
                ordre_omega= str(position_omega[0]) +"-" + str(position_omega[1])+":*"+str(position[0])+"-"+ str(position[1])
        else:#le cas ou il n'a pas de loup ennemi a cote de notre loup omega 
            proche=[]
            dis=100
            for cle in teams:
                if teams[cle][0]==0 :
                    dist=distance(position_omega[0],position_omega[1],cle[0],cle[1])
                    if distance<dis:
                        proche=cle
            ordre_omega= str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(proche[0])+"-"+ str(proche[1])
    else:
        ennemis_rayon=in_range(teams,6,position_omega)
        if len(ennemis_rayon)>3:
            ordre_omega=str(position_omega[0]) +"-" + str(position_omega[1])+ ":pacify"
        else:
            if ennemi_omega!=[]:
                if [ennemi_alpha[0],ennemi_alpha[1]] in ennemi_omega:
                    ordre_omega= str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(ennemi_alpha[0])+"-"+ str(ennemi_omega[1])
                else:
                    position=random.choice(ennemi_omega)
                    ordre_omega= str(position_alpha[0]) +"-" + str(position_alpha[1])+":*"+str(position[0])+"-"+ str(position[1])
            else:
                if position_alpha_ennemi[0]> position_omega[0]:
                    x= position_omega[0]+1
                elif position_alpha_ennemi[0]< position_omega[0]:
                    x= position_omega[0]-1
                else: 
                    x= position_omega[0]

                if position_alpha_ennemi[1]> position_omega[1]:
                    y= position_omega[0]+1
                elif position_alpha_ennemi[1]< position_omega[1]:
                    y= position_omega[0]-1
                else :
                    y= position_omega[1]
                
                
                ordre_omega = str(position_omega[0]) +"-" + str(position_omega[1])+ ":@" + str(x)+"-"+ str(y)
    
    return  ordre_alpha, ordre_omega
    

print(Ai(teams,1))

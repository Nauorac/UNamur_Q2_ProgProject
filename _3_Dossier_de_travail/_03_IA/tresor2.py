def SAI_orders_generator(Px): # Spec 0 % and Code 0%
    # Recuperer l'ensemble des ennemis et des amis qui son autours de mon alpha
    pos_alpha=[]
    pos_alpha_ennemi=[]
    ami_alpha=[]
    ennemi_alpha=[]
    ami_omega=[]
    ennemi_omega=[]
    pos_omega=[]
    ordre_alpha=""
    ordre_omega=""
    # Recupere la position de mon alpha et alpha ennemi
    for cle in entities:
        # Check if it's alpha of team in argument
        if entities[cle][0]== Px and entities[cle][1]== "alpha":
            pos_alpha.append(cle[0])
            pos_alpha.append(cle[1])
        # Check if it's an opposite alpha of the entities in argument
        elif(entities[cle][0] != Px and entities[cle][0] != 0 and entities[cle][1] == "alpha"):
            pos_alpha_ennemi.append(cle[0])
            pos_alpha_ennemi.append(cle[1])
        # Check if it's omega of the team in argument
        elif entities[cle][0] == Px and entities[cle][1] == "omega":
            pos_omega.append(cle[0])
            pos_omega.append(cle[1])
        elif entities[cle][0] == Px and entities[cle][1] == "normal":
    # ------------
    # Ordres Alpha
    # ------------
    #recuperer les alentours de mon alpha => dictionnaire des loups amis est ennemis
    dic_loup=in_range(1,pos_alpha) #dictionnaire des loups amis et ennemis
    for cle in dic_loup:
        if dic_loup[cle][0] == Px:
            ami_alpha.append([cle[0],cle[1]])
        else:
            ennemi_alpha.append([cle[0],cle[1]])
    if (entities[(pos_alpha[0],pos_alpha[1])][2]<100):
        for cle in entities:
            if(entities[(cle[0], cle[1])][0] == 0 and distance(pos_alpha[0], pos_alpha[1], cle[0], cle[1]) == 1):
    # Verifier si mon alpha est sur une ressource et il a un manque d'energie
                ordre_alpha= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+":<" + str(cle[0]) + "-" + str(cle[1])
    else:
    # Traiter le cas ou le loup est n'est pas a cote une ressource et qu'il a assez d'energie
        x=""
        y=""
        if (ennemi_alpha==[]):
    # Verifier si on a pas de loups ennemis a cote de nous
            if pos_alpha_ennemi[0] > pos_alpha[0]:
                x= pos_alpha[0]+1
            elif pos_alpha_ennemi[0] < pos_alpha[0]:
                x= pos_alpha[0]-1
            else:
                x= pos_alpha[0]
            if pos_alpha_ennemi[1] > pos_alpha[1]:
                y= pos_alpha[0]+1
            elif pos_alpha_ennemi[1] < pos_alpha[1]:
                y= pos_alpha[0]-1
            else :
                y= pos_alpha[1]
            ordre_alpha= str(pos_alpha[0])+"-"+ str(pos_alpha[1]) +":@"+ str(x)+ "-" + str(y)
        else: # Le cas ou on des les loups ennemis qui nous entourent
            for i in ennemi_alpha:
                if entities[(i[0], i[1])][1] == "alpha":
                    ordre_alpha= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+":*"+str(i[0])+"-"+ str(i[1])
            z= random.choice(ennemi_alpha)
            ordre_alpha= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+ ":*" +str(z[0])+"-"+ str(z[1])
    # ------------
    # Ordres Omega
    # ------------
    # Le cas ou notre loup omega n'a pas assez d'energie pour pacifier
    if (entities[(pos_omega[0],pos_omega[1])][2]<40):
        dic_loup = in_range(1, pos_omega)
        for cle in dic_loup:
            if dic_loup[cle][0] == Px:
                ami_omega.append([cle[0],cle[1]])
            else:
                ennemi_omega.append([cle[0],cle[1]])
    # Le cas ou notre loup omega a des ennemis qui l'entourent
        if ennemi_omega!=[]:
            if pos_alpha_ennemi in ennemi_omega:
                ordre_omega= str(pos_omega[0]) +"-" + str(pos_omega[1])+":*"+str(pos_alpha_ennemi[0])+"-"+ str(pos_alpha_ennemi[1])
            else:
                position=random.choice(ennemi_omega)
                ordre_omega= str(pos_omega[0]) +"-" + str(pos_omega[1])+":*"+str(position[0])+"-"+ str(position[1])
        else:
    # Le cas ou il n'a pas de loups ennemis a cote de notre loup omega
            proche=[]
            dis=100
            for cle in entities:
                if entities[cle][0] == 0:
                    dist=distance(pos_omega[0],pos_omega[1],cle[0],cle[1])
                    if distance<dis:
                        proche=cle
            ordre_omega= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+":*"+str(proche[0])+"-"+ str(proche[1])
    else:
        ennemis_rayon=in_range(6,pos_omega)
        if len(ennemis_rayon)>3:
            ordre_omega=str(pos_omega[0]) +"-" + str(pos_omega[1])+ ":pacify"
        else:
            if ennemi_omega!=[]:
                if [ennemi_alpha[0],ennemi_alpha[1]] in ennemi_omega:
                    ordre_omega= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+":*"+str(ennemi_alpha[0])+"-"+ str(ennemi_omega[1])
                else:
                    position=random.choice(ennemi_omega)
                    ordre_omega= str(pos_alpha[0]) +"-" + str(pos_alpha[1])+":*"+str(position[0])+"-"+ str(position[1])
            else:
                if pos_alpha_ennemi[0]> pos_omega[0]:
                    x= pos_omega[0]+1
                elif pos_alpha_ennemi[0]< pos_omega[0]:
                    x= pos_omega[0]-1
                else:
                    x= pos_omega[0]

                if pos_alpha_ennemi[1]> pos_omega[1]:
                    y= pos_omega[0]+1
                elif pos_alpha_ennemi[1]< pos_omega[1]:
                    y= pos_omega[0]-1
                else :
                    y= pos_omega[1]
                ordre_omega = str(pos_omega[0]) +"-" + str(pos_omega[1])+ ":@" + str(x)+"-"+ str(y)
    # --------------
    # Ordres normaux
    # --------------

    return ""+ordre_alpha+" "+ordre_omega+""
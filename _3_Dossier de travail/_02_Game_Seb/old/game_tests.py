



def feed(ww_coords, entity_coords):
    check_food = entity_at(entity_coords)
    check_ww = entity_at(ww_coords)
    # Test if food exist
    if check_food != False:
        # Test si le ww existe, et si son energie est en dessous de 100
        if (check_ww != False) and (check_ww[0] != 0) and (check_ww[2] < 100):
            food_E = check_food[2]
            ww_E = check_ww[2]
            while (food_E > 0) and (ww_E < 100):
                food_E -= 1
                #print(food_E)
                ww_E += 1
            if food_E == 0:
                print("The "+check_food[1]+" have been completely eaten.")
                entities.pop(entity_coords)
            else:
                check_food[2] = food_E
            check_ww[2] = ww_E
            entities.update({entity_coords: check_food})
            entities.update({ww_coords: check_ww})
        else:
            print("There is no food there.")


#feed((2,1), (6,1))

#print(entity_at((2, 1)))
#print(entities[(6,1)])
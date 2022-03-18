import random, blessed 

def load_maps(maplink):
    """Creates a map / Shows the map to the players by using the information that are containted in the cpx file.
    
    Parameters
    ----------
    map_link: *pas sur*

    Notes
    -----

    Returns
    -------
    map: the map (dict)

    """   
    game_map = {
        "coord" : [],
        "type" : []
        }
    cload_info = {
        "coord" : [],
        "weigth" : []
    }
    
    line = open(maplink, "r")
    raw_map_info = (line.readline(2))
    map_row, map_col = raw_map_info.split(" ")
    map_size = (map_row, map_col)


    raw_anthill1_info = (line.readline(4))
    anthill1_row, anthill1_col = raw_anthill1_info(" ")
    anthill1_coord = anthill1_row + "," + anthill1_col


    raw_anthill2_info = (line.readline(5))
    anthill2_row, anthill2_col = raw_anthill2_info(" ")
    anthill2_coord = anthill2_row + "," + anthill2_col


    for i in line:
        current_line = (i+7)
        raw_cload_info = (line.readline(current_line))
        cload_row, cload_col, cload_weight = raw_cload_info.split(" ")
        cload_coord = cload_row + "," + cload_col


        cload_info.get("coord").append(cload_coord)
        cload_info.get("weight").append(cload_weight)

    line.close()



    for i in map_row :
        for j in map_col:
            as_add = False
            game_map.get("coord").append(i + "," + j)

            if (i + "," + j) == anthill1_coord:
                game_map.get("type").append("A1")
                as_add = True
            elif (i + "," + j) == anthill2_coord:
                game_map.get("type").append("A2")
                as_add = True
            
            for x in cload_info.get("coord"):
                if x == (i + "," + j):
                    if game_map.get("weight") == 1:
                        game_map.get("type").append("CL")
                    elif game_map.get("weight") == 2:
                        game_map.get("type").append("CM")
                    elif game_map.get("weight") >= 3:
                        game_map.get("type").append("CH")
                    as_add = True
            if as_add == False:
                game_map.get("type").append("V")
            
    return(game_map, map_size)

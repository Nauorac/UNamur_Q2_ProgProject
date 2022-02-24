def map_update(game_map,map_size,ant):
    term = blessed.Terminal()

    print(term.home + term.clear + term.hide_cursor)

    row_tag = 0
    col_tag = 0
    nbrow = map_size[0]
    nbcol = map_size[1]


    print(term.move_yx(row_tag, col_tag) + term.on_black + '  ┌' + term.normal, end='', flush=True)
    col_tag += 3
    for i in range(nbcol):
        print(term.move_yx(row_tag, col_tag) + term.on_black + '---' + term.normal, end='', flush=True)
        col_tag += 3
    print(term.move_yx(row_tag, col_tag) + term.on_black + '┐  ' + term.normal, end='', flush=True)
    row_tag += 1
    col_tag = 0

    for row in range((nbrow)):
        print(term.move_yx(row_tag, col_tag) + term.on_black + '  |' + term.normal, end='', flush=True)
        col_tag += 3
        for column in range((nbcol)):
            case_index = game_map.get("coord").index("%s,%s"%(row,column))
            case_type = game_map.get("type")[case_index]
            if case_type == "V":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_snow3 + ' . ' + term.normal, end='', flush=True)
                col_tag += 3
            elif case_type == "CL":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_palegreen1 + ' ◇ ' + term.normal, end='', flush=True)
                col_tag += 3
            elif case_type == "CM":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_palegreen3 + ' ◈ ' + term.normal, end='', flush=True)
                col_tag += 3
            elif case_type == "CH":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_palegreen4 + ' ◆ ' + term.normal, end='', flush=True)
                col_tag += 3
            elif case_type == "A1":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_cyan3 + ' ☆ ' + term.normal, end='', flush=True)
                col_tag += 3
            elif case_type == "A2":
                print(term.move_yx(row_tag, col_tag) + term.black + term.on_firebrick3 + ' ☆ ' + term.normal, end='', flush=True)
                col_tag += 3
        print(term.move_yx(row_tag, col_tag) + term.on_black + '|  ' + term.normal, end='', flush=True)
        col_tag = 0
        row_tag += 1
        
    print(term.move_yx(row_tag, col_tag) + term.on_black + '  └' + term.normal, end='', flush=True)
    col_tag += 3
    for i in range(nbcol):
        print(term.move_yx(row_tag, col_tag) + term.on_black + '---' + term.normal, end='', flush=True)
        col_tag += 3
    print(term.move_yx(row_tag, col_tag) + term.on_black + '┘  ' + term.normal, end='', flush=True)

    for i in(ant.get("coord")):
        
        row_tag , col_tag = i.split(",")
        ant_row = row_tag
        ant_col = col_tag
        row_tag = int(row_tag) + 1 
        col_tag = (int(col_tag) * 3) + 4

        ant_index = ant.get("coord").index("%s,%s"%(ant_row,ant_col))
        ant_lvl = ant.get("lvl")[ant_index]
        ant_player = ant.get("player")[ant_index]

        if ant_player == 1:
            if ant_lvl == 1:
                print(term.move_yx(row_tag, col_tag) + term.cyan3 + term.on_snow3 + '❶' + term.normal, end='', flush=True)
            elif ant_lvl == 2:
                print(term.move_yx(row_tag, col_tag) + term.cyan3 + term.on_snow3 + '❷' + term.normal, end='', flush=True)
            elif ant_lvl == 3:
                print(term.move_yx(row_tag, col_tag) + term.cyan3 + term.on_snow3 + '❸' + term.normal, end='', flush=True)

        elif ant_player == 2:
            if ant_lvl == 1:
                print(term.move_yx(row_tag, col_tag) + term.firebrick3 + term.on_snow3 + '❶' + term.normal, end='', flush=True)
            elif ant_lvl == 2:
                print(term.move_yx(row_tag, col_tag) + term.firebrick3 + term.on_snow3  + '❷' + term.normal, end='', flush=True)
            elif ant_lvl == 3:
                print(term.move_yx(row_tag, col_tag) + term.firebrick3 + term.on_snow3 + '❸' + term.normal, end='', flush=True)
    return()
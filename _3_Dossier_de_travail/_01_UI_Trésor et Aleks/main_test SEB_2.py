import blessed


def map_update(map_size, entities):
    term = blessed.Terminal()

    print(term.home + term.clear + term.hide_cursor)

    row_tag = 0
    col_tag = 0
    nbrow = map_size[0]
    nbcol = map_size[1]

    print(term.move_yx(row_tag, col_tag) +
          term.on_black + '  ┌', end='', flush=True)
    col_tag += 3
    for i in range(nbcol):
        print(term.move_yx(row_tag, col_tag) +
              term.on_black + '----', end='', flush=True)
        col_tag += 3
    print(term.move_yx(row_tag, col_tag) +
          term.on_black + '┐  \n', end='', flush=True)
    row_tag += 1
    col_tag = 0
    col_count = 0
    creation = 1
    map_creator = {}
    x = 1
    y = 1
    while creation == 1:
        map_creator[x, y] = [0, " ", 0]
        y += 1
        if y == map_size[1] + 1:
            y = 1
            x += 1
        if x >= map_size[0]+1:
            creation = 0
    x = 1
    y = 1
    for i in entities:
        size1, size2 = i
        z = entities[i]
        map_creator[size1, size2] = z

    for i in map_creator:

        x = map_creator[i]
        z = ' '.join([str(elem) for elem in x])
        wolf_player = z.split(" ")[0]
        wolf_type = z.split(" ")[1]
        if col_count == map_size[1]:
            print(term.on_black + ' |\n', end='')
            col_count = 0
        if col_count == map_size[1]:
            print(term.on_black + '|', end=' ')
        else:
            print(term.on_black + '  |', end=' ')
        if wolf_player == "1":
            if wolf_type == "normal":
                print(term.cyan3 + term.on_snow3 + u"\U0001F43A", end='')
                col_count += 1
            elif wolf_type == "omega":
                print(term.cyan3 + term.on_snow3 + 'Ω', end='')
                col_count += 1
            elif wolf_type == "alpha":
                print(term.cyan3 + term.on_snow3 + 'α', end='')
                col_count += 1
            elif wolf_type == "human":
                print(term.cyan3 + term.on_snow3 + u"\U0001F464", end='')
                col_count += 1
            elif wolf_type == " ":
                print(term.firebrick3 + term.on_snow3 + " ", end='')
                col_count += 1
            else:
                print(term.firebrick3 + term.on_snow3 + " ", end='')
                col_count += 1
        elif wolf_player == "2":
            if wolf_type == "normal":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F43A", end='')
                col_count += 1
            elif wolf_type == "omega":
                print(term.firebrick3 + term.on_snow3 + 'Ω', end='')
                col_count += 1
            elif wolf_type == "alpha":
                print(term.firebrick3 + term.on_snow3 + 'α', end='')
                col_count += 1
            elif wolf_type == "human":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F464", end='')
                col_count += 1
            elif wolf_type == " ":
                print(term.firebrick3 + term.on_snow3 + "  ", end='')
                col_count += 1
            else:
                print(term.firebrick3 + term.on_snow3 + "  ", end='')
                col_count += 1
        elif wolf_player == "0":
            if wolf_type == "berries":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F352", end='')
                col_count += 1
            elif wolf_type == "mice":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F401", end='')
                col_count += 1
            elif wolf_type == "apples":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F34E", end='')
                col_count += 1
            elif wolf_type == "rabbits":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F407", end='')
                col_count += 1
            elif wolf_type == "deer":
                print(term.firebrick3 + term.on_snow3 + u"\U0001F98C", end='')
                col_count += 1
            elif wolf_type == " ":
                print(term.firebrick3 + term.on_snow3 + "0", end='')
                col_count += 1
            else:
                print(term.firebrick3 + term.on_snow3 + "0", end='')
                col_count += 1
    print(term.move_yx(row_tag, col_tag) +
          term.on_black + '\n  └', end='', flush=True)
    for i in range(nbcol):
        print(term.move_yx(row_tag, col_tag) +
              term.on_black + '----', end='', flush=True)
        col_tag += 3
    print(term.move_yx(row_tag, col_tag) +
          term.on_black + '┘  ', end='', flush=True)

    return ()


# start_game("D:files\map.ano", 1, "", "", "", "")
map_size = [6, 6]
entities = {(2, 1): [1, "alpha", 60], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "human", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50],
            (1, 6): [0, "rabbits", 75], (4, 4): [0, "deer", 100]}

map_update(map_size, entities)

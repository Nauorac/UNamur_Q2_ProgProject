m = 6
n = 6

entities = {(2, 1): [1, "alpha", 57], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, "deers", 100]}

def make_board(m, n):
    for count in range(m):
        for rows in range(n):
            coords = (rows, count)
            #print(coords)
            if coords in entities:
                print(entities[coords][1])
                return entities[coords][1]
"""            for key, values in entities.items():
                if key == (rows, count):
                    cell = values[1]
                    print(cell)
                    return cell"""
                    #return [[cell for rows in range(m)] for count in range(n)]
                    #return [['..' for count in range(n)] for rows in range(n)]

def print_board(board):
    # todo: coordinates
    for m in board:
        for n in board:
            print(' | '.join(m))
    print('')

"""def get_board_size():
    # todo: user input
    return 6"""

def test():
    m = 6
    n = 6
    myboard = make_board(m, n)
    #print_board(myboard)
    # put value as string, indexes are 0-based
    #myboard[1][2] = "ww"
    print_board(myboard)


if __name__ == '__main__':
    test()

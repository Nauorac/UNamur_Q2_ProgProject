
n = 7

entities = {(2, 1): [1, " alpha ", 57], (1, 1): [1, " omega ", 100], (2, 2): [1, "normal ", 100],
            (5, 5): [2, " alpha ", 100], (6, 6): [2, " omega ", 100], (6, 5): [2, "normal ", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples ", 30], (5, 3): [0, " mice  ", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, " deers ", 100]}


def make_board(n):
    return [[' ..... ' for count in range(n)] for rows in range(n)]

def print_board(board):
    for row in board:
        print('|'.join(row))
    print('')


def updateboard(myboard):
    r = n
    c = n
    #print (r,c)
    for i in range(r):
        for j in range(c):
            coords = (i, j)
            #print(coords)
            if (i == 0) and (j == 0):
                myboard[i][j] = ""
                ...
            elif (i == 0) and (j < r):
                myboard[i][j] = ""
                ...
            elif (i < r) and (j == 0):
                myboard[i][j] = ""
                ...
            elif (i == r) and (j == c):
                myboard[i][j] = ""
                ...
            elif coords in entities:
                myboard[i][j] = entities[coords][1]
            else:
                myboard[i][j] = ' '+str(coords)+''

    return myboard

def test():
    myboard = make_board(n)
    #print(myboard[0][2])
    #print("****************")
    #print_board(myboard)
    #print("****************")
    updateboard(myboard)
    #myboard[1][2] = "ww"
    print_board(myboard)


if __name__ == '__main__':
    test()

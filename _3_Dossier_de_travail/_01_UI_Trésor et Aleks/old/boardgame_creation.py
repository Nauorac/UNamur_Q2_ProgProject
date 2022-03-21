#-*- coding: utf-8 -*-


entities = {(2, 1): [1, "alpha", 60], (1, 1): [1, "omega", 100], (2, 2): [1, "normal", 100],
            (5, 5): [2, "alpha", 100], (6, 6): [2, "omega", 100], (6, 5): [2, "normal", 100],
            (2, 4): [0, "berries", 10], (6, 1): [0, "apples", 30], (5, 3): [0, "mice", 50], (1, 6): [0, "rabbits", 75], (4, 4): [0, "deers", 100]}

def entity_at(entity_coords):
    # Validée
    for key, values in entities.items():
        if key == entity_coords:
            return [values[0], values[1], values[2], ]
    return False

r = 6
c = 6
boardgame = {}
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
        if (i,j) in entities:
            #print("yes")
            boardgame[(i,j)] = entity_at((i,j))
            #thisdict[(5, 5)] = ["pouet", 10]
            print(boardgame[(i,j)])
        else:
            print("no")
            boardgame = {(i,j): ["empty"]}

print(boardgame)

x = boardgame.items()

print(x)
"""if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")"""

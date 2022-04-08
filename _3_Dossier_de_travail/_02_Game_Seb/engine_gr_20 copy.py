#-*- coding: utf-8 -*-
import blessed
import math
import os
import time
import random
term = blessed.Terminal()

size = (20, 20)
entities = {(2, 2): [1, 'alpha', 86, 0], (1, 1): [1, 'omega', 100, 0], (1, 2): [1, 'normal', 100, 0], (2, 1): [1, 'normal', 100, 0], (1, 3): [1, 
'normal', 100, 0], (2, 3): [1, 'normal', 100, 0], (3, 3): [1, 'normal', 100, 0], (3, 2): [1, 'normal', 100, 0], (3, 1): [1, 'normal', 100, 0], 
            (19, 19): [2, 'alpha', 86, 0], (20, 20): [2, 'omega', 100, 0], (20, 19): [2, 'normal', 100, 0], (19, 20): [2, 'normal', 100, 0], (20, 18): [2, 'normal', 100, 0], (19, 18): [2, 'normal', 100, 0], (18, 18): [2, 'normal', 100, 0], (18, 19): [2, 'normal', 100, 0], (18, 20): [2, 'normal', 100, 0], 
(4, 4): [0, 'berries', 10, 0], (4, 5): [0, 'berries', 10, 0], (5, 4): [0, 'berries', 10, 0], (5, 5): [0, 'berries', 10, 0], (16, 16): [0, 'berries', 10, 0], (16, 17): [0, 'berries', 10, 0], (17, 16): [0, 'berries', 10, 0], (17, 17): [0, 'berries', 10, 0], (1, 4): [0, 'apples', 30, 0], (1, 5): [0, 'apples', 30, 0], (20, 16): [0, 'apples', 30, 0], (20, 17): [0, 'apples', 30, 0], (4, 1): [0, 'mice', 50, 0], (5, 1): [0, 'mice', 50, 0], (16, 20): [0, 'mice', 50, 0], (17, 20): [0, 'mice', 50, 0], (5, 7): [0, 'rabbits', 100, 0], (7, 5): [0, 'deers', 500, 0], (16, 14): [0, 'rabbits', 100, 0], (14, 16): [0, 'deers', 500, 0]}

"""print("Welcome to the game of life !")
alpha_1_life = 100
for key in entities:
    #print(entities[key][0], entities[key][2])
    if (entities[key][0] == 1) and (entities[key][1] == 'alpha'):
        alpha_1_life = entities[key][2]
        print("alpha_1_life = " + str(alpha_1_life))"""

def end_game(winner):
    with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        print(term.center(term.move_y(y_middle-5) +
              term.underline_bold_green((" GAME FINISHED"))))
        if winner == 1 or winner == 2:
            print(term.move_y(y_middle-3) + term.center("PLAYER   " +
                  str(winner)+"  win the game").rstrip())
        else:
            print(term.move_y(y_middle-3) +
                  term.center("Both alphas lives is 0 this turn.").rstrip())
            print(term.move_y(y_middle-2) +
                  term.center("  IT'S  A  DRAW").rstrip())
        print(term.move_y(y_middle+1) + term.center('').rstrip())
        print(term.move_y(y_middle+1) +
              term.center('Press any key to exit !').rstrip())
        term.inkey()
    end_screen()

def check_alphas_life(fin):
    # Get alpha1 and alpha2 life
    alpha_1_life = 100
    alpha_2_life = 100
    for key, values in entities.items():
            if (entities[key][0] == 1) and (entities[key][1] == "alpha"):
                alpha_1_life = entities[key][2]
                print("alpha_1_life = " + str(alpha_1_life))
            if (entities[key][0] == 2) and (entities[key][1] == "alpha"):
                alpha_2_life = entities[key][2]
                print("alpha_2_life = " + str(alpha_2_life))
    # Check max life between alphas and declare winner (end game cases 2 or 3)
    if fin == 1:
        if alpha_1_life > alpha_2_life:
            winner = 1
            return end_game(winner)
        elif alpha_1_life < alpha_2_life:
            winner = 2
            return end_game(winner)
        elif alpha_1_life == alpha_2_life:
            winner = 0
            return end_game(winner)
    # Check if one of the alphas is dead and declare winner (end game cases 1)
    else:
        if alpha_1_life == 0:
            winner = 2
            return end_game(winner)
        elif alpha_2_life == 0:
            winner = 1
            return end_game(winner)
        elif alpha_1_life == 0 and alpha_2_life == 0:
            winner = 0
            return end_game(winner)

check_alphas_life(1)

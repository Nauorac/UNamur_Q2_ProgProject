#
# SELECTION OF ONE OF THE SIX DIFFERENT GAME MODE
#
# Selection player 1
# ------------------
#Local OR Lan
P1_game_mode = int(input('Select game mode for player 1 => 0 (Local) OR 1 (Lan) : '))
# Human or I.A.
P1_type = int(input("Select game type for player 1 => 0 (Human) OR 1 (I.A.) : "))
# ------------------
# Selection player 2
# ------------------
#Local OR Lan
P2_game_mode = int(input("Select game mode for player 2 => 0 (Local) OR 1 (Lan) : "))
# Human or I.A.
P2_type = int(input("Select game type for player 2 => 0 (Human) OR 1 (I.A.) : "))

# ------------------
#        Summary
# ------------------
print("*********************")
print("---  Player  ONE  ---")
if P1_game_mode == 0:
    print("--- LOCAL | ",end=" ")
else:
    print("--- LAN | ", end=" ")
if P1_type == 0:
    print("Human ---")
else:
    print("I.A. ---")
print("*********************")
print("---  Player  TWO  ---")
if P2_game_mode == 0:
    print("--- LOCAL | ", end=" ")
else:
    print("--- LAN | ", end=" ")
if P2_type == 0:
    print("Human ---")
else:
    print("I.A. ---")
print("*********************")

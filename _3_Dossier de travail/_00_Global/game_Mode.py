
print("Enter your name:")
x = input()
# Selection player 1
# ------------------
#Local OR Lan
P1_game_mode = int(input('Select game mode for player 1 => 0 (Local) OR 1 (Lan) : '))
if P1_game_mode == 0:
    print("You've selected Local for player 1.")
else:
    print("You've selected Lan for player 1.")
# Human or I.A.
P1_type = int(input("Select game type for player 1 => 0 (Human) OR 1 (I.A.) : "))
if P1_type == 0:
    print("You've selected Human for player 1.")
else:
    print("You've selected I.A. for player 1.")

# ------------------
# Selection player 2
# ------------------
#Local OR Lan
P2_game_mode = int(input("Select game mode for player 2 => 0 (Local) OR 1 (Lan) : "))
if P1_game_mode == 0:
    print("You've selected Local for player 2.")
else:
    print("You've selected Lan for player 2.")
# Human or I.A.
P2_type = int(input("Select game type for player 2 => 0 (Human) OR 1 (I.A.) : "))
if P2_type == 0:
    print("You've selected Human for player 2.")
else:
    print("You've selected I.A. for player 2.")

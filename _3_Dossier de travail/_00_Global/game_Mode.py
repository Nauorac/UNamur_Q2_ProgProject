#
# SELECTION OF ONE OF THE SIX DIFFERENT GAME MODE
#
# Cases :
# 1) P1 - Local - Human | P2 - Local - Human
# 2) P1 - Local - Human | P2 - Local - IA
# 3) P1 - Local - IA    | P2 - Local - IA
# 4) P1 - Local - Human | P2 - Lan - Human
# 5) P1 - Local - IA    | P2 - Lan - IA
# 6) P1 - Local - IA    | P2 - Lan - Human

# Si on veut arbitrer on peut rajouter 3 autres type de game

# 7) P1 - Lan - Human   | P2 - Lan - Human
# 8) P1 - Lan - IA      | P2 - Lan - IA
# 9) P1- Lan - Human    | P2 - Lan - IA

def game_settings():
    # Selection player 1
    # ------------------
    #Local OR Lan
    P1_game_mode = int(input('Select game mode for player 1 => 0 (Local) OR 1 (Remote) : '))
    # If Remote ask for group number
    if P1_game_mode == 1:
        P1_game_mode = "remote"
        group_1 = int(input("Please enter the group number for player 1 : "))
    else:
        P1_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    P1_type = int(input("Select game type for player 1 => 0 (Human) OR 1 (I.A.) : "))
    if P1_type == 1:
        P1_type = "I.A."
    else:
        P1_type = "Human"
    # ------------------
    # Selection player 2
    # ------------------
    #Local OR Lan
    P2_game_mode = int(
        input("Select game mode for player 2 => 0 (Local) OR 1 (Remote) : "))
    # If Remote ask for group number
    if P2_game_mode == 1:
        P2_game_mode = "remote"
        group_2 = int(input("Please enter the group number for player 2 : "))
    else:
        P2_game_mode = "local"
        group_1 = 20
    # Human or I.A.
    P2_type = int(input("Select game type for player 2 => 0 (Human) OR 1 (I.A.) : "))
    if P2_type == 1:
        P2_type = "I.A."
    else:
        P2_type = "Human"

    # P1 from group number on local/remote and it's a human/IA
    print(f"Player 1 from group : {group_1} on {P1_game_mode} and it's a {P1_type}.")
    # P2 from group number on local/remote and it's a human/IA
    print(f"Player 2 is from group : {group_2} on {P2_game_mode} and it's a {P2_type}.")

    return ["P1", group_1, P1_game_mode, P1_type, "P2", group_2, P2_game_mode, P2_type]


print(game_settings())

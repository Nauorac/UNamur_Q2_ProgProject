
import blessed
term = blessed.Terminal()

# Creation of all "global" variables required for the game
path = "C:/Users/Seb/Documents/GitHub/UNamur_Q2_ProgProject/_3_Dossier_de_travail/vertical.ano"
#https://github.com/Nauorac/UNamur_Q2_ProgProject/blob/526bafbbaa287bad23a7efa7956b62999b42a00b/_0_Ennonce/example.ano
P1_game_mode = "local"
P2_game_mode = "local"
group_1 = 20
group_2 = 1
P1_type = "A.I."
P2_type = "A.I."
orders_P1 = "-"
orders_P2 = "-"
size = []
entities = {}
game_turn = 1
turn_without_damage = 0
path_validated = False
settings_validated = False

#Next two dictionnaries are used to assign UTF-8 "pictures" with keywords
pics = {"alpha": "α", "omega": "Ω", "normal": "🐺", "human": "👤",
        "berries": "🍒", "apples": "🍎", "mice": "🐁", "rabbits": "🐇", "deers": "🦌"}
g_set_pics = {"Human": "👤", "A.I.": "🤖", "local": "💻", "remote": "🖧", }


def game_settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):  # Spec and Code 100%
    """
	Description of the function
	---------------------------
    Function that ask with inputs to select all the game settings.

    Returns:
    --------
	list : Return a list with all the settings defined by players
    ["P1", group_1, P1_game_mode, P1_type, "P2", group_2, P2_game_mode, P2_type]

	Version:
	--------
	Specification : Sébastien Baudoux (v.2.0 - 11/03/2022)
	Code : Sébastien Baudoux (v.3.0 - 11/03/2022)
	"""
    with term.cbreak():
        # Selection player 1
        # ------------------
        #Local OR Remote
        print("Select game mode for player 1 => 0 (Local) OR 1 (Remote) : ")
        temp_P1_game_mode = term.inkey()
        # If Remote, ask for group number
        if temp_P1_game_mode == 1:
            P1_game_mode = "remote"
            print("Please enter the group number for player 1 : ")
            group_1 = term.inkey()
        else:
            P1_game_mode = "local"
            group_1 = 20
        # Human or I.A.
        print("Select game type for player 1 => 0 (Human) OR 1 (A.I.) : ")
        temp_P1_type = term.inkey()
        if temp_P1_type == 1:
            P1_type = "A.I."
        else:
            P1_type = "Human"
        # ------------------
        # Selection player 2
        # ------------------
        #Local OR Remote
        print("Select game mode for player 2 => 0 (Local) OR 1 (Remote) : ")
        temp_P2_game_mode = term.inkey()
        # If Remote, ask for group number
        if temp_P2_game_mode == 1:
            P2_game_mode = "remote"
            print("Please enter the group number for player 2 : ")
            group_2 = term.inkey()
        else:
            P2_game_mode = "local"
            group_1 = 20
        # Human or I.A.
        print("Select game type for player 2 => 0 (Human) OR 1 (A.I.) : ")
        temp_P2_type = term.inkey()
        if temp_P2_type == 1:
            P2_type = "A.I."
        else:
            P2_type = "Human"
        # P1 from group number on local/remote and it's a human/IA
        print(f"Player 1 from group : {group_1} on {P1_game_mode} and it's a {P1_type}.")
        # P2 from group number on local/remote and it's a human/IA
        print(f"Player 2 is from group : {group_2} on {P2_game_mode} and it's a {P2_type}.")
        return [path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type]

def change_path(path):  # Spec and Code 100%
    """
    Description of the function
    ---------------------------
    Function that ask with inputs to select the file path.

    Returns:
    --------
    string : Return the path of the file
    """
    with term.cbreak():
        print("Please enter the path of the file : ")
        path = term.inkey()
        return path

def data_import(path, size, entities):  # Spec and Code 100%
    """
	Description
	---------------------------
    Update the size tuple and the entities dictionary with data in a ano file.

    Args:
    -----
    path : filepath of the .ano file  - str
    size : Tuple with 2 elements, raw number and column number - tuple
    entities : Dictionnary that contains all elements on the boardgame - dict

	Version:
	--------
	Specification : Sébastien Baudoux (v.1.0 - 11/03/2022)
	Code : Sébastien Baudoux (v.2.0 - 10/03/2022)
	"""
    # Open .ano file
    with open(path, "r+") as file:
        # Read the entire file and store it into a list.
        brut = file.readlines()
        for i in brut:
            # Ignore string line
            if (i[0] == "m") or (i[0] == "w") or (i[0] == "f"):
                continue
            # Detect if line contains boardgame size
            if len(i) <= 6:
                si = i.split()
                size = [int(si[0]), int(si[1])]
                continue
            j = i.split()
            # Check if line contain werewolf info or not
            if (j[3] == "alpha") or (j[3] == "omega") or (j[3] == "normal"):
                x = int(j[1])
                y = int(j[2])
                values = [int(j[0]), (j[3]), 100, 0]
                entities.update({(x, y): values})
            else:
                x = int(j[0])
                y = int(j[1])
                # Add "0" as first list value element for food to make the "food team" identified with 0
                values = [0, (j[2]), int((j[3])), 0]
                entities.update({(x, y): values})
    return path, size, entities

path, size, entities = data_import(path, size, entities)

n = size[0]
def simplify_boardgame(n):  # Spec 0 % and Code 100%
    """
	Description of the function
	---------------------------


    Uses:
    -----
    ...
	
    Args:
    -----

    Arg : Description - type
	
    Returns:
    --------

	type : Description
   
	Version:
	--------
	Specification : Author (v.1.0 - dd/mm/yyyy)
	Code : Author (v.1.0 - dd/mm/yyyy)
	"""
    #make_board
    o = n+1
    myboard = [[' ..... ' for count in range(o)] for rows in range(o)]
    #updateboard
    r = n+1
    c = n+1
    #print (r,c)
    for i in range(r):
        for j in range(c):
            coords = (i, j)
            #print(coords)
            if (i == 0) and (j == 0):
                myboard[i][j] = ""
                ...
            elif (i == 0) and (j < c):
                if j < 10:
                    myboard[i][j] = ""
                else:
                    myboard[i][j] = ""
            elif (i < r) and (j == 0):
                if i < 10:
                    myboard[i][j] = ""
                else:
                    myboard[i][j] = ""
                ...
            elif (i == r) and (j == c):
                myboard[i][j] = ""
                ...
            elif coords in entities:
                picture_name = entities[coords][1]
                if (entities[coords][1] == "alpha") or (entities[coords][1] == "omega"):
                    if entities[coords][0] == 2:
                        picture = ""+term.white_on_salmon + \
                            str(pics[picture_name][0])+term.normal+" "
                    else:
                        picture = ""+str(pics[picture_name][0])+" "
                else:
                    if entities[coords][0] == 2:
                        picture = term.white_on_salmon + \
                            pics[picture_name][0]+term.normal
                    else:
                        picture = pics[picture_name][0]
                myboard[i][j] = picture
            else:
                myboard[i][j] = ".."
                #myboard[i][j] = ""+str(coords)+""
    #print board
    for row in myboard:
        print('|'.join(row))
    print('')

def settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type):
    # Display settings menu
      with term.fullscreen(), term.cbreak():
        y_middle = term.height // 2
        x_middle = term.width // 2
        #print(term.move_y(y_middle-17) + term.center("*-*").rstrip())
        print(term.move_y(y_middle-16) + term.center(""+term.bold+"┌-----------------------------------┐"+term.normal+"").rstrip())
        print(term.move_y(y_middle-15) + term.center(""+term.bold+" | 🎮 *  Default game settings  * 🎮 |"+term.normal+"").rstrip())
        print(term.move_y(y_middle-14) + term.center(""+term.bold + "└-----------------------------------┘"+term.normal+"").rstrip())
        print(term.move_y(y_middle-12) + ("    Default map path : ").rstrip())
        print(term.move_y(y_middle-11) + ("" + term.green_on_black+str(path)+term.normal+"").rstrip())
        print(term.move_y(y_middle-8) + ("    Map Preview ").rstrip())
        print(term.move_y(y_middle-9) + ("    Would you like to change it ? Press 'm' to change it.").rstrip())
        print(term.move_y(y_middle-7) + term.center(simplify_boardgame(n)).rstrip())
        #Display P1 settings on right side
        print(term.move_y(y_middle-6)+term.move_x(x_middle+15)+("Player 1").rstrip())
        print(term.move_y(y_middle-5)+term.move_x(x_middle+3)+(" => Game Mode  *-*  Player Type <=").rstrip())
        print(term.move_y(y_middle-3)+term.move_x(x_middle+3)+("   "+P1_game_mode+" - "+g_set_pics[P1_game_mode]+"  *-*     "+P1_type+" "+g_set_pics[P1_type]+" "+term.normal+"").rstrip())
        #Display P2 settings on right side
        print(term.move_y(y_middle-0) +
              term.move_x(x_middle+15)+term.white_on_salmon+("Player 2").rstrip())
        print(term.move_y(y_middle+1)+term.move_x(x_middle+3) +term.white_on_salmon+
              (" => Game Mode  *-*  Player Type <=").rstrip())
        print(term.move_y(y_middle+3)+term.move_x(x_middle+3)+term.white_on_salmon+("   "+P2_game_mode+" - " +
              g_set_pics[P2_game_mode]+"  *-*     "+P2_type+" "+g_set_pics[P2_type]+" "+term.normal+"").rstrip())
        print(term.move_y(y_middle+17) + term.center(("Press 'y'es or 'n'o")).rstrip())
        with term.cbreak():
            val = ''
            blink = 0
            val = term.inkey(timeout=3)
            while val.lower() != 'y' or val.lower() != 'n':
                  val = term.inkey(timeout=0.5)
                  if blink == 1:
                        print(term.center(term.move_y(y_middle+18) + term.underline_bold_green(("Please press 'y' or 'n' "))))
                        blink -= 1
                  else:
                        print(term.move_y(y_middle+17) + term.clear_eos)
                        blink += 1
                  if val.lower() == 'y':
                        print(f"{term.home}{term.clear}")
                        path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type = game_settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
                        settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
                  elif val.lower() == 'm':
                        print(term.move_y(y_middle-10)+(" Please enter new path : ").rstrip())
                        path = term.inkey()
                  elif val.lower() == 'n':
                        return print("GAME")
      settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)


settings(path, P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)

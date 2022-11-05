                                                        #**-/-**__ALPHA__&__OMEGA__**-/-**#
'''
Eben Edwyn
Bernagou Esteban
Bouffioux Corentin
Grandjean Hugo
'''

#Imports :
#--------#

from blessed import Terminal
from math import *
import random
import time
import socket
from AI_gr_13 import get_AI_orders

#Remote-part :
#------------#

def create_server_socket(local_port, verbose):
    """Creates a server socket.
    
    Parameters
    ----------
    local_port: port to listen to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: server socket (socket.socket)
    
    """
    
    socket_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_in.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state

    if verbose:
        print(' binding on local port %d to accept a remote connection' % local_port)
    
    try:
        socket_in.bind(('', local_port))
    except:
        raise IOError('local port %d already in use by your group or the referee' % local_port)
    socket_in.listen(1)
    
    if verbose:
        print('   done -> can now accept a remote connection on local port %d\n' % local_port)
        
    return socket_in

def create_client_socket(remote_IP, remote_port, verbose):
    """Creates a client socket.
    
    Parameters
    ----------
    remote_IP: IP address to send to (int)
    remote_port: port to send to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_out: client socket (socket.socket)
    
    """

    socket_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_out.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state
    
    connected = False
    msg_shown = False
    
    while not connected:
        try:
            if verbose and not msg_shown:
                print(' connecting on %s:%d to send orders' % (remote_IP, remote_port))
                
            socket_out.connect((remote_IP, remote_port))
            connected = True
            
            if verbose:
                print('   done -> can now send orders to %s:%d\n' % (remote_IP, remote_port))
        except:
            if verbose and not msg_shown:
                print('   connection failed -> will try again every 100 msec...')
                
            time.sleep(.1)
            msg_shown = True
            
    return socket_out
       
def wait_for_connection(socket_in, verbose):
    """Waits for a connection on a server socket.
    
    Parameters
    ----------
    socket_in: server socket (socket.socket)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: accepted connection (socket.socket)
    
    """
    
    if verbose:
        print(' waiting for a remote connection to receive orders')
        
    socket_in, remote_address = socket_in.accept()
    
    if verbose:
        print('   done -> can now receive remote orders from %s:%d\n' % remote_address)
        
    return socket_in            

def create_connection(your_group, other_group=0, other_IP='127.0.0.1', verbose=False):
    """Creates a connection with a referee or another group.
    
    Parameters
    ----------
    your_group: id of your group (int)
    other_group: id of the other group, if there is no referee (int, optional)
    other_IP: IP address where the referee or the other group is (str, optional)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    Raises
    ------
    IOError: if your group fails to create a connection
    
    Notes
    -----
    Creating a connection can take a few seconds (it must be initialised on both sides).
    
    If there is a referee, leave other_group=0, otherwise other_IP is the id of the other group.
    
    If the referee or the other group is on the same computer than you, leave other_IP='127.0.0.1',
    otherwise other_IP is the IP address of the computer where the referee or the other group is.
    
    The returned connection can be used directly with other functions in this module.
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')
        
    # check whether there is a referee
    if other_group == 0:
        if verbose:
            print('** group %d connecting to referee on %s **\n' % (your_group, other_IP))
        
        # create one socket (client only)
        socket_out = create_client_socket(other_IP, 42000+your_group, verbose)
        
        connection = {'in':socket_out, 'out':socket_out}
        
        if verbose:
            print('** group %d successfully connected to referee on %s **\n' % (your_group, other_IP))
    else:
        if verbose:
            print('** group %d connecting to group %d on %s **\n' % (your_group, other_group, other_IP))

        # create two sockets (server and client)
        socket_in = create_server_socket(42000+your_group, verbose)
        socket_out = create_client_socket(other_IP, 42000+other_group, verbose)
        
        socket_in = wait_for_connection(socket_in, verbose)
        
        connection = {'in':socket_in, 'out':socket_out}

        if verbose:
            print('** group %d successfully connected to group %d on %s **\n' % (your_group, other_group, other_IP))
        
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return connection
               
def bind_referee(group_1, group_2, verbose=False):
    """Put a referee between two groups.
    
    Parameters
    ----------
    group_1: id of the first group (int)
    group_2: id of the second group (int)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connections: sockets to receive/send orders from both players (dict)
    
    Raises
    ------
    IOError: if the referee fails to create a connection
    
    Notes
    -----
    Putting the referee in place can take a few seconds (it must be connect to both groups).
        
    connections contains two connections (dict of socket.socket) which can be used directly
    with other functions in this module.  connection of first (second) player has key 1 (2).
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')

    # create a server socket (first group)
    if verbose:
        print('** referee connecting to first group %d **\n' % group_1)        

    socket_in_1 = create_server_socket(42000+group_1, verbose)
    socket_in_1 = wait_for_connection(socket_in_1, verbose)

    if verbose:
        print('** referee succcessfully connected to first group %d **\n' % group_1)        
        
    # create a server socket (second group)
    if verbose:
        print('** referee connecting to second group %d **\n' % group_2)        

    socket_in_2 = create_server_socket(42000+group_2, verbose)
    socket_in_2 = wait_for_connection(socket_in_2, verbose)

    if verbose:
        print('** referee succcessfully connected to second group %d **\n' % group_2)        
    
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return {1:{'in':socket_in_1, 'out':socket_in_1},
            2:{'in':socket_in_2, 'out':socket_in_2}}

def close_connection(connection):
    """Closes a connection with a referee or another group.
    
    Parameters
    ----------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    """
    
    # get sockets
    socket_in = connection['in']
    socket_out = connection['out']
    
    # shutdown sockets
    socket_in.shutdown(socket.SHUT_RDWR)    
    socket_out.shutdown(socket.SHUT_RDWR)
    
    # close sockets
    socket_in.close()
    socket_out.close()
       
def notify_remote_orders(connection, orders):
    """Notifies orders to a remote player.
    
    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
    orders: orders to notify (str)
        
    Raises
    ------
    IOError: if remote player cannot be reached
    
    """

    # deal with null orders (empty string)
    if orders == '':
        orders = 'null'
    
    # send orders
    try:
        connection['out'].sendall(orders.encode())
    except:
        raise IOError('remote player cannot be reached')

def get_remote_orders(connection):
    """Returns orders from a remote player.

    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
        
    Returns
    ----------
    player_orders: orders given by remote player (str)

    Raises
    ------
    IOError: if remote player cannot be reached
            
    """
   
    # receive orders    
    try:
        orders = connection['in'].recv(65536).decode()
    except:
        raise IOError('remote player cannot be reached')
        
    # deal with null orders
    if orders == 'null':
        orders = ''
        
    return orders


#Game-part :
#----------#

def create_dic(map_path):
    """
    This function creates the dictionnary based on the .ano file

    Parameters :
    ------------
    map_path : path of the map file

    Returns:
    --------
    game_dict : dictionnary of the ano files' data (dict)

    Version :
    ---------
    Specification : Esteban Bernagou (v.1 - 19/02/2022)
    Implementation : Esteban Bernagou (v.1 - 19/02/2022)
    """
    f = open(map_path, 'r')
    game_dict = {'map': [], 'werewolves': {'team_1': {}, 'team_2': {}}, 'foods': {}}
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.strip(' ')
        if line.endswith(':'):
            line = line.strip(':')
            key = line
        else:
            my_list = line.split(' ')
            if len(my_list) > 2:
                if key == 'werewolves':
                    if my_list[0] == '1':
                        team = 'team_1'
                    else:
                        team = 'team_2'
                    coordonates_w = (int(my_list[1]), int(my_list[2]))
                    game_dict[key][team][coordonates_w] = [my_list[3], 100]
                elif key == 'foods':
                    coordonates_f = (int(my_list[0]), int(my_list[1]))
                    game_dict[key][coordonates_f] = [my_list[2], int(my_list[3])]
            else:
                game_dict[key] = [int(my_list[0]), int(my_list[1])]
    f.close()
    return game_dict

def create_UI(game_dict):
        """
        This function creates the UI based on the dictionnary

        Parameters :
        ------------
        game_dict : dictionnary based on the .ano file (dict)
        term : store the Terminal() class (class)

        Version :
        ---------
        specification : Corentin Bouffioux (v.1 20/02/2022)
        implementation : Corentin Bouffioux (v.4 18/03/2022)
        """
        
        term = Terminal()

        print(term.home + term.clear)

        vline = "│"
        hline = "─"

        llcorner = "└"
        ulcorner = "┌"
        lrcorner = "┘"
        urcorner = "┐"

        ttee = "┬"

        btee = "┴"
        ltee = "├"
        rtee = "┤"

        bigplus = "┼"


        def top_grid(game_dict):

            top_inside_grid = game_dict['map'][0]*(3*hline + ttee)
            top_grid = ulcorner +  top_inside_grid + 3*hline + urcorner

            return top_grid

        def inside_grid(game_dict):

            inside_grid = ltee + (game_dict['map'][0]*((3*hline) + bigplus)) + 3*hline + rtee

            return inside_grid

        def bottom_grid(game_dict):

            bottom_inside_grid = game_dict['map'][0]*(3*hline + btee)
            bottom_grid = llcorner + bottom_inside_grid + 3*hline + lrcorner

            return bottom_grid


        interline = (vline + '   ')*(game_dict['map'][0]+1) + vline

        print(term.move_right(29),top_grid(game_dict))
        
        count = 3
        while count != 2*game_dict['map'][1]+1:

            print(term.move_xy(29,count),inside_grid(game_dict))
            print(term.move_xy(29,count+1),interline)
            count += 2
        
        print(term.move_xy(29,(game_dict['map'][1]*2+1)),inside_grid(game_dict))
        print(term.move_xy(29,(game_dict['map'][1]*2+2)),interline)
        print(term.move_xy(29,(game_dict['map'][1]*2+3)),bottom_grid(game_dict))
        
        # Enumerate grid x (0,1,2,3,...)

        enumeration_grid_x = ' '
        for i in range(game_dict['map'][0]+1):
            if len(str(i)) > 1:
                enumeration_grid_x += ''
                enumeration_grid_x += str(i) + '│ '
            else:
                enumeration_grid_x += ''
                enumeration_grid_x += str(i) + ' │ '

            print(term.move_xy(30,2) + '│' + enumeration_grid_x)

        # Enumerate grid y (0,1,2,3,...)

        for i in range(0,game_dict['map'][1]*2+1,2):
            print(term.move_xy(31,2+i), int(i/2))
        return term
    
def place_item(game_dict, term):
    """
    This function places all items (werewolves and foods) on the grid
    
    Parameters : 
    ------------
    game_dict : dictionnary based on the .ano file (dict)
    term : store the Terminal() class (class)

    Version : 
    ---------
    Specification : Hugo Grandjean (v.3 12/03/2022)
    Implementation : Hugo Grandjean (v.3 15/03/2022)
    """

    for food in game_dict['foods']:
        x,y = calcul_grid(*food)


        f_type = game_dict['foods'][food][0]
        if f_type == 'apples':
            f_print = '🍏 '
            f_max_energy = 30
        elif f_type == 'deers':
            f_print = '🍗 '
            f_max_energy = 500
        elif f_type == 'berries':
            f_print = '🍇 '
            f_max_energy = 10
        elif f_type == 'rabbits':
            f_print = '🐇 '
            f_max_energy = 100
        elif f_type == 'mice':
            f_print = '🐁 '
            f_max_energy = 50

        f_energy = game_dict['foods'][food][1]

        if f_energy <= 0.5*f_max_energy and f_energy > 0.1*f_max_energy:
            print(term.move_xy(x,y) + term.on_yellow(f_print))
        elif f_energy <= 0.1*f_max_energy:
            print(term.move_xy(x,y) + term.on_red(f_print))
        else:
            print(term.move_xy(x, y) + f_print)



    for werewolves_team_1 in game_dict['werewolves']['team_1']:
        x,y = calcul_grid(*werewolves_team_1)
        if 'alpha' in game_dict['werewolves']['team_1'][werewolves_team_1][0]:
            print(term.move_xy(x,y) + term.on_red(' ⍺ '))
        if 'normal' in game_dict['werewolves']['team_1'][werewolves_team_1][0]:
            print(term.move_xy(x,y) + term.on_red('🐺 ')) 
        if 'human' in game_dict['werewolves']['team_1'][werewolves_team_1][0] or 'human omega' in game_dict['werewolves']['team_1'][werewolves_team_1][0]:
            print(term.move_xy(x,y) + term.on_red('🧑 '))    
        elif 'omega' in game_dict['werewolves']['team_1'][werewolves_team_1][0]:
            print(term.move_xy(x,y) + term.on_red(' Ω '))      

    for werewolves_team_2 in game_dict['werewolves']['team_2']:
        x,y = calcul_grid(*werewolves_team_2)
        if 'alpha' in game_dict['werewolves']['team_2'][werewolves_team_2][0]:
            print(term.move_xy(x,y) + term.on_dodgerblue2(' ⍺ '))
        if 'normal' in game_dict['werewolves']['team_2'][werewolves_team_2][0]:
            print(term.move_xy(x,y) + term.on_dodgerblue2('🐺 '))
        if 'human' in game_dict['werewolves']['team_2'][werewolves_team_2][0] or 'human omega' in game_dict['werewolves']['team_2'][werewolves_team_2][0]:
            print(term.move_xy(x,y) + term.on_dodgerblue2('🧑 '))
        elif 'omega' in game_dict['werewolves']['team_2'][werewolves_team_2][0]:
            print(term.move_xy(x,y) + term.on_dodgerblue2(' Ω '))
        
    data_team(game_dict,term)

def data_team(game_dict, term):
        """
        This function prints informations and design about the two teams
        
        Parameters :
        ------------
        game_dict : dictionnary based on the .ano file (dict)
        term : store the Terminal() class (class)

        Version :
        ---------
        Sepcification : Corentin Bouffioux (v.2 24/03/2022)
        Implementation : Corentin Bouffioux (v.5 24/03/2022)
        """
        
        name_werewolves = ('  Alpha    Omega    Normal  ')
    
        # All informations for team 1

        w_list_team1 = []
        energy_team_1 = []
        
        for positions in game_dict['werewolves']['team_1']:
            werewolves1 = game_dict['werewolves']['team_1'][positions][0]
            w_list_team1.append(werewolves1) 
            energy_team_1.append(game_dict['werewolves']['team_1'][positions][1])
            
            if game_dict['werewolves']['team_1'][positions][0] == 'normal' and game_dict['werewolves']['team_1'][positions][1] == 0:
                game_dict['werewolves']['team_1'][positions][0] = 'human'
            if game_dict['werewolves']['team_1'][positions][0] == 'omega' and game_dict['werewolves']['team_1'][positions][1] == 0:
                game_dict['werewolves']['team_1'][positions][0] = 'human omega'
            if game_dict['werewolves']['team_1'][positions][0] == 'human omega' and game_dict['werewolves']['team_1'][positions][1] != 0:
                game_dict['werewolves']['team_1'][positions][0] = 'omega'

                

        count_alpha_team1 = 0
        count_omega_team1 = 0
        count_normal_team1 = 0
        count_human_team1 = 0

        for elem in w_list_team1:
            if elem == 'alpha':
                count_alpha_team1 += 1 
            if elem == 'omega':
                count_omega_team1 += 1
            if elem == 'normal':
                count_normal_team1 += 1 
            if elem == 'human' or elem == 'human omega':
                count_human_team1 += 1
        
        color = term.on_red
        
        for i in range(game_dict['map'][1]*2):
            print(term.move_xy(0,i+4) + color(29*' '))

        print(term.move_xy(56,0) + term.white + term.bold('**-/-**__ALPHA__&__OMEGA__**-/-**'))
        print(term.move_xy(0,1) + color + term.bold('          Player 1           '))
        print(term.move_xy(0,2) + color + (29*'-'))
        print(term.move_xy(0,3) + color, name_werewolves)
        print(term.move_xy(0,4) + color('    %d/1 ','     %d/1 ','     %d/%d    ')%(count_alpha_team1,count_omega_team1,count_normal_team1,len(w_list_team1)-2))
        print(term.move_xy(0,5) + color(29*' '))
        print(term.move_xy(0,6) + color('          Human : %d          ')%(count_human_team1))
        print(term.move_xy(0,7) + color + (29*'-'))


            # data werewolves for team 1

        for position_team1 in game_dict['werewolves']['team_1']:

            data_werewolve_team1 = str((game_dict['werewolves']['team_1'][position_team1], position_team1)).replace('[','').replace(']','').replace('\'','').strip('(')[:-1]    

            print(term.move_down(1) + term.move_right(4) + color(data_werewolve_team1))




        # All informations for team 2

        
        w_list_team2 = []
        energy_team_2 = []

        for positions in game_dict['werewolves']['team_2']:
            werewolves2 = game_dict['werewolves']['team_2'][positions][0]
            w_list_team2.append(werewolves2) 
            energy_team_2.append(game_dict['werewolves']['team_2'][positions][1])

            if game_dict['werewolves']['team_2'][positions][0] == 'normal' and game_dict['werewolves']['team_2'][positions][1] == 0:
                game_dict['werewolves']['team_2'][positions][0] = 'human'
            if game_dict['werewolves']['team_2'][positions][0] == 'omega' and game_dict['werewolves']['team_2'][positions][1] == 0:
                game_dict['werewolves']['team_2'][positions][0] = 'human omega'
            if game_dict['werewolves']['team_2'][positions][0] == 'human omega' and game_dict['werewolves']['team_2'][positions][1] != 0:
                game_dict['werewolves']['team_2'][positions][0] = 'omega'


        count_alpha_team2 = 0
        count_omega_team2 = 0
        count_normal_team2 = 0
        count_human_team2 = 0

        for elem in w_list_team2:
            if elem == 'alpha':
                count_alpha_team2 += 1 
            if elem == 'omega':
                count_omega_team2 += 1
            if elem == 'normal':
                count_normal_team2 += 1 
            if elem == 'human' or elem == 'human omega':
                count_human_team2 += 1
        

        canevas = game_dict['map'][0]*4+36
        color = term.on_dodgerblue2

        for i in range(game_dict['map'][1]*2):
            print(term.move_xy((canevas),i+4) + color(30*' '))
        
        print(term.move_xy(canevas,1) + color + term.bold('          Player 2            '))
        print(term.move_xy(canevas,2) + color + (30*'-')) 
        print(term.move_xy(canevas,3) + color, name_werewolves + ' ')
        print(term.move_xy(canevas,4) + color('    %d/1 ','     %d/1 ','     %d/%d     ')%(count_alpha_team2,count_omega_team2,count_normal_team2,len(w_list_team2)-2))
        print(term.move_xy(canevas,5) + color(30*' '))
        print(term.move_xy(canevas,6) + color('          Human : %d          ')%(count_human_team2))
        print(term.move_xy(canevas,7) + color + (30*'-')) 

        for position_team2 in game_dict['werewolves']['team_2']:

            data_werewolve_team2 = str((game_dict['werewolves']['team_2'][position_team2], position_team2)).replace('[','').replace(']','').replace('\'','').strip('(')[:-1]

            print(term.move_down(1) + term.move_right(game_dict['map'][1]*4 + 39) + color(data_werewolve_team2))

def calcul_grid(x,y):
        """
        This function calculates the offset between the grid and the real coordinates with blessed
        
        Parameters : 
        ------------
        x : calculate rows (int)
        y : calculate columns (int)
        
        Returns :
        ---------
        x : calculate rows (int)
        y : calculate columns (int)

        Version :
        ---------
        Specification : Edwyn Eben (v.1 10/03/2022)
        Implementation : Edwyn Eben (v.1 10/03/2022)
        """

        x = x*4 + 31

        y = y*2 + 2
        return x,y

def calculate_distance(x1, y1, x2, y2):
        """
        This function calculates the distance between 2 werewolves 
        
        Parameters : 
        ------------
        x1 : first row's position (int)
        y1 : first column's position (int)
        x2 : second row's position (int)
        y2 : second columns' position(int)
        
        Returns :
        ---------
        distance : distance between the two coordonates (int)

        Version :
        ---------
        Specification : Esteban Bernagou (v.1 10/03/2022)
        Implementation : Esteban Bernagou (v.1 10/03/2022)
        """


        distance = max(abs(x2-x1), abs(y2-y1))
        return distance

def up_round(n):
        """
        This function round a number is the decimal_part of the number is over 0.5

        Parameters:
        -----------
        n : number to round (int)

        Returns:
        --------
        n_rounded : number rounded (int)

        Notes :
        -------
        .if n == 0.5 , n_rounded = 2
        .if n == 1.5, n_rounded = 2

        Versions :
        ----------
        Specification : Esteban Bernagou - (v.1) 26/03/2022
        Implementation : Esteban Bernagou - (v.1) 26/03/2022
        
        """

        decimal_part = n % 1

        if n < 1 and decimal_part >= 0.5:
                n_rounded = 2
        elif n > 1 and decimal_part >= 0.5:
                n_rounded = (n-decimal_part) + 1
        else :
                n_rounded = n-decimal_part

        return int(n_rounded)

def pacify(game_dict, pacify_list, teams, term):
        """
        This function uses the power of the omega werewolves

        Parameters :
        —---------
        game_dict : dictionnary based on the .ano file (dict)
        pacify_list : list of the pacify's orders (list)
        teams : name of the teams (team_1 or team_2) (str)
        term : store the Terminal() class (class)

        Returns :
        ---------
        pacify_wolf_list : list of the werewolves who were pacified (list)

        Version :
        ---------
        Specification : Hugo Grandjean (v.2) - 27/03/2022
        Implementation : Hugo Grandjean (v.3) - 15/03/2022)
        """
        pacify_order = pacify_list[0]
        pacify_order = pacify_order.strip(':pacify')
        coord_list = pacify_order.split('-')
        pacify_wolf_list = [] 

        if teams == 'team_1':
            team = 'team_2'
        else:
            team = 'team_1'
        if game_dict['werewolves'][teams][(int(coord_list[0]), int(coord_list[1]))][0] == 'omega':
            game_dict['werewolves'][teams][(int(coord_list[0]), int(coord_list[1]))][1] -= 40
            for ennemi in game_dict["werewolves"][team]:
                distance_pacify = calculate_distance(int(coord_list[0]), int(coord_list[1]), ennemi[0], ennemi[1])
                if distance_pacify >= -6 and distance_pacify <= 6:
                    pacify_wolf_list.append(ennemi)
        place_item(game_dict, term)
        return pacify_wolf_list

def feed(game_dict, feed_list, term, teams):
    """
    This function restores the energy of the werewolves 

    Parameters :
    ------------
    game_dict : dictionnary based on the .ano file (dict)
    feed_list : list of the feed's orders (list)
    term : store the Terminal() class (class)
    teams : name of the teams (team_1 or team_2) (str)   

    Version :
    ---------
    Specification : Edwyn Eben - (v.2) 27/02/2022
    Implementation : Edwyn Eben - (v.3) 20/03/2022

    """

    verif_list =  []

    for feed_orders in feed_list:
        feed_order = feed_orders.split(':<')
        werewolves_coord_list = feed_order[0].split('-')
        food_coord_list = feed_order[1].split('-')
        coord_w = (int(werewolves_coord_list[0]), int(werewolves_coord_list[1]))
        coord_f = (int(food_coord_list[0]), int(food_coord_list[1]))   
        x, y = calcul_grid(*coord_f)
        distance = calculate_distance(*coord_w, *coord_f)
        if coord_f in game_dict['foods']:  
            f_type = game_dict['foods'][coord_f][0]
            if distance <= 1: 
                if coord_w not in verif_list:       
                        if coord_w in game_dict['werewolves'][teams]:
                            w_energy = game_dict['werewolves'][teams][coord_w][1]
                            energy_to_restore = 100 - w_energy
                            if energy_to_restore > 0:
                                f_energy = game_dict['foods'][coord_f][1]

                                if energy_to_restore >= f_energy:                                    
                                    w_new_energy = w_energy+ f_energy  
                                    del(game_dict['foods'][coord_f])

                                    print(term.home + term.move_xy(x, y) +term.on_black('ㅤ '))

                                elif energy_to_restore < f_energy:
                                    f_new_energy = f_energy - energy_to_restore
                                    w_new_energy = 100

                                    game_dict['foods'][coord_f] = [f_type, f_new_energy]
                
                                if w_energy == 0 :
                                    if game_dict['werewolves'][teams][coord_w][0] == 'human omega':
                                        game_dict['werewolves'][teams][coord_w] = ['omega', w_new_energy]
                                    else:
                                        game_dict['werewolves'][teams][coord_w] = ['normal', w_new_energy]
                                else:
                                    game_dict['werewolves'][teams][coord_w][1] = w_new_energy
                                
                                verif_list.append(coord_w)
                        
    place_item(game_dict, term)

def fight(game_dict, attack_list, bonus_dict, pacify_wolf_list, term, teams):
        """
        This function makes fight the werewolves

        Parameters :
        ------------
        game_dict : dictionnary based on the .ano file (dict)
        attack_list : list of attack's orders (list)
        bonus_dict : dictionnary containing the datas of the werewolves who reiceived a bonus (dict)
        pacify_wolf_list : list of the werewolves who were pacified (list)
        term : store the Terminal() class (class)
        teams : name of the teams (team_1 or team_2) (str)


        Version :
        ---------
        Specification : Edwyn Eben - (v.2) 14/03/2022
        Implementation : Edwyn Eben - (v.4) 16/03/2022

        """

        verif_list =  []

        for fight_orders in attack_list:
            fight_order = fight_orders.split(':*')
            werewolves_coord_list = fight_order[0].split('-') 
            werewolves_coord_list_2 = fight_order[1].split('-')
            coord_w_a = (int(werewolves_coord_list[0]), int(werewolves_coord_list[1]))
            coord_w_d = (int(werewolves_coord_list_2[0]), int(werewolves_coord_list_2[1]))

            if coord_w_d in game_dict['werewolves']['team_1']:
                team_defensive = 'team_1'
            else:
                team_defensive = 'team_2'   

            distance = calculate_distance(coord_w_a[0], coord_w_a[1], coord_w_d[0], coord_w_d[1])
            if distance == 1:
                if coord_w_a in game_dict['werewolves'][teams] and coord_w_d in game_dict['werewolves'][team_defensive]:
                    if coord_w_a not in verif_list :
                        if game_dict['werewolves'][teams][coord_w_a][0] != 'human' and game_dict['werewolves'][teams][coord_w_a][0] != 'human omega':
                            if coord_w_a not in pacify_wolf_list:
                                w_energy_a = game_dict['werewolves'][teams][coord_w_a][1]
                                bonus = 0
                                for positions in bonus_dict:
                                    if positions == coord_w_a:
                                        bonus = bonus_dict[positions]
                                fight_energy = 0.1 * (w_energy_a + bonus)
                      
                                w_energy_d = game_dict['werewolves'][team_defensive][coord_w_d][1]
        
                                        
                                energyd= w_energy_d-fight_energy
                                new_energy_d= up_round(energyd)

                                if new_energy_d < 0:
                                    new_energy_d = 0

                                game_dict['werewolves'][team_defensive][coord_w_d][1] = new_energy_d
                                    
                                verif_list.append(coord_w_a) 
        
        place_item(game_dict,term)  

def move(game_dict, move_list, term, teams):
        """This function moves the werewolves

        Parameters :
        ------------
        game_dict : dictionnary based on the .ano file (dict)
        move_list : list of the move's orders (list)
        term : stores the Terminal() class (class)
        teams : name of the teams (team_1 or team_2) (str)
        
        Versions :
        ----------
        Specifications : Corentin Bouffioux - (v.4) 27/03/2022
        Implementation : Esteban Bernagou - (v.3) 24/03/2022
        
        """
        
        width = game_dict['map'][0]
        height = game_dict['map'][1]

        verif_list = []

        for move_orders in move_list:  
            move_order = move_orders.split(':@')
            depart_coord_list = move_order[0].split('-')  
            arrived_coord_list = move_order[1].split('-')  
            x, y = calcul_grid(int(depart_coord_list[0]), int(depart_coord_list[1]))
            x2, y2 = calcul_grid(int(arrived_coord_list[0]), int(arrived_coord_list[1]))
            coord_1 = (int(depart_coord_list[0]), int(depart_coord_list[1]))  
            coord_2 = (int(arrived_coord_list[0]), int(arrived_coord_list[1])) 
            position_list = []
            for positions in game_dict['werewolves'][teams]:
                position_list.append(positions)
            if int(arrived_coord_list[0]) <= int(depart_coord_list[0]) + 1 and int(arrived_coord_list[1]) <= int(depart_coord_list[1]) + 1:
                if coord_1 in position_list:
                    if coord_2[0] > 0 and coord_2[1] > 0 and coord_2[0] < width and coord_2[1] < height: # Verify that the werewolve don't exit the Board
                        if coord_2 not in game_dict['werewolves']['team_2'] and coord_2 not in game_dict['werewolves']['team_1']:
                            if coord_1 != coord_2:
                                if coord_1 not in verif_list:  # Verify that a werewolve don't move 2 times
                                    if coord_1 in game_dict['werewolves']['team_1']:
                                        last_data = game_dict['werewolves']['team_1'][coord_1]
                                        del(game_dict['werewolves']['team_1'][coord_1])
                                        game_dict['werewolves']['team_1'][coord_2] = last_data
                                        color = term.red
                                        color_back = term.on_red
                                    elif coord_1 in game_dict['werewolves']['team_2']:
                                        last_data = game_dict['werewolves']['team_2'][coord_1]
                                        game_dict['werewolves']['team_2'][coord_1]
                                        del(game_dict['werewolves']['team_2'][coord_1])
                                        game_dict['werewolves']['team_2'][coord_2] = last_data
                                        color = term.dodgerblue2
                                        color_back = term.on_dodgerblue2
                                    #Move on U.I
                                    print(term.move_xy(x, y) +term.on_black('ㅤ '))
                                    if last_data[0] == 'normal':
                                        print(term.move_xy(x2, y2) + color_back('🐺 '))
                                    elif last_data[0] == 'alpha':
                                        print(term.move_xy(x2, y2) + color(' α '))
                                    else:
                                        print(term.move_xy(x2, y2) +color(' Ω '))
                                    verif_list.append(coord_2)
        place_item(game_dict, term)

def win(game_dict):
    """This function determinates if the game is over or not

    Parameters:
    -----------
    game_dict : dictionnary of the ano files' data (dict)

    Return :
    --------

    True : if the game isn't finished (bool)
    'Team_1' : if the team 1 has won (str)
    'Team_2' : if the Team 2 has won (str)

    Version :
    ---------
    Implementation : Edwyn Eben - (v.1) 25/03/2022
    Specification : Edwyn Eben - (v.1) 25/03/2022
    """
    for werewolves in game_dict["werewolves"]["team_1"]:    
        if game_dict["werewolves"]["team_1"][werewolves][0]=="alpha":
            alpha_energy_1=game_dict["werewolves"]["team_1"][werewolves][1]
    for werewolves in game_dict["werewolves"]["team_2"]:    
        if game_dict["werewolves"]["team_2"][werewolves][0]=="alpha":
            alpha_energy_2=game_dict["werewolves"]["team_2"][werewolves][1]          
    if alpha_energy_1 != 0 and alpha_energy_2!=0:
        return True
    else:
        if alpha_energy_2 == 0:
            return "Team 1"
        else:
            return "Team 2"

def border(game_dict):
        if game_dict['map'][0] >= 20 and game_dict['map'][0] <= 40 and game_dict['map'][1] >= 20 and game_dict['map'][1] <= 40:
            return True
        else:
            return False

def bonus(game_dict, teams):
    """
    This function gives the bonus of each werewolves between each other

    Parameters :
    —-----------
    game_dict : dictionnary based on the .ano file (dict)
    term : store the Terminal() class (class)

    Return :	
    —-------
    bonus_dict : dictionnary containing the datas of the werewolves who reiceived a bonus (dict)

    Version :
    ---------
    Specification : Corentin Bouffioux (v.2 02/03/2022)
    Implementation : Esteban Bernagou, Edwyn Eben (v.1 23/03/2022)

    """
    bonus_dict = {}
    normal_list = []
    alpha_list = []
    alpha_coord_list = []
    normal_bonus = 10
    alpha_bonus = 0

    for positions in game_dict['werewolves'][teams]:
        x = positions[0]
        y = positions[1]

        #On récupère les coordonnées de l'alpha
        if game_dict['werewolves'][teams][positions][0] == 'alpha':
            alpha_coord_list.append(positions)
           
        #On crée l'alpha
        if alpha_coord_list != []:
            if positions != alpha_coord_list[0]:
                alpha_distance = calculate_distance(x, y, alpha_coord_list[0][0], alpha_coord_list[0][1])
                if alpha_distance in range(0, 5):
                    alpha_list.append(positions)

        for teamates in game_dict['werewolves'][teams]:
            if game_dict['werewolves'][teams][teamates][0] != 'alpha' and teamates != positions:
                normal_distance = calculate_distance(x, y, teamates[0], teamates[1])
                if normal_distance in range(0, 3) and positions not in normal_list:
                    normal_list.append(teamates)
        
        if positions in alpha_list:
            alpha_bonus = 30

        total_bonus = normal_bonus * len(normal_list) + alpha_bonus
        bonus_dict[positions] = total_bonus

    return bonus_dict
            
def deal_orders(orders):
    """This function separates orders in some low-levels list to deals with differents kind of orders

    Parameters :
    ------------
    
    orders : list of every orders (list)

    Returns :
    ---------
    pacify_list : list of the pacify's orders (list)
    feed_list : list of the feed's orders (list)
    attack_list : list of attack's orders (list)
    move_list : list of the move's orders (list)
    """

    pacify_list = []
    feed_list = []
    attack_list = []
    move_list = []

    orders = orders.split( )
    for order in orders:

        if ':*' not in order and ':@' not in order and ':<' not in order and ':pacify' not in order:
            orders.remove(order)
        elif ':pacify' in order and order not in pacify_list:
            pacify_list.append(order)
        elif ':<' in order and order not in feed_list:
            feed_list.append(order)
        elif ':*' in order and order not in attack_list:
            attack_list.append(order)
        elif ':@' in order and order not in move_list:
            move_list.append(order)
            for orders_move in move_list:
                second_move_list = []
                len_verify_list = []
                order_move = orders_move.split(':@')
                second_move_list.append(order_move[1])
                for second_orders in range(len(second_move_list)):
                    len_verify_list.append(second_orders)
                if len(len_verify_list) > 1:
                    move_list.remove(orders_move)

    
    return pacify_list, feed_list, attack_list, move_list

def count_energy(game_dict):
    energy_list_1 = []
    energy_list_2 = []

    for positions in game_dict['werewolves']['team_1']:
        energy_list_1.append(game_dict['werewolves']['team_1'][positions][1])
    for positions in game_dict['werewolves']['team_2']:
        energy_list_2.append(game_dict['werewolves']['team_2'][positions][1])

    total_1 = energy_list_1[0]
    total_2 = energy_list_2[0]

    for x in range(len(energy_list_1)):
        if x > 0:
            total_1 += energy_list_1[x]
    
    for x in range(len(energy_list_2)):
        if x > 0:
            total_2 += energy_list_2[x]

    if total_1 > total_2:
        return "Team 1"
    
    elif total_2 > total_1:
        return "Team 2"

    else:
        return "Draw"

def play_game(map_path, group_1, type_1, group_2, type_2):
    """Play a game.
    
    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    
    If there is an external referee, set group id to 0 for remote player.
    
    Versions:
    ---------
    Implementation : Hugo Grandjean (v.1) - 15/03/2022
    Specification : Esteban Bernagou (v.1) - 27/03/2022
    """

    pacify_wolf_list = []

    #Dictionnary creation :
    #---------------------#

    game_dict = create_dic(map_path)

    #Data_verification :
    #------------------#
    
    verif = border(game_dict)
    
    if verif == True:

        #Game :
        #-----#

        if type_1 == 'remote':
            connection = create_connection(group_2, group_1)
        elif type_2 == 'remote':
            connection = create_connection(group_1, group_2, verbose = True, other_IP = '138.48.160.134')
        

        count_round = 0
        count_pacify = 0
        count_attack = 0

        term = create_UI(game_dict)
        place_item(game_dict, term)

        #Loop to continue the game :
        #--------------------------#
        while win(game_dict) == True and count_attack < 200:
            
            place_item(game_dict, term)
            count = 0
            count_round += 1
            count_attack += 1

            while count !=2:

                if count % 2 == 0:
                    teams = 'team_1'
                    color_back = term.on_red

                else:
                    teams = 'team_2'
                    color_back = term.on_dodgerblue2

                if len(str(count_round)) == 2:
                    framework_back = 11 * ' '
                elif len(str(count_round)) == 3:
                    framework_back = 10 * ' '
                else:
                    framework_back = 12 * ' '

                framework = 12 * ' '
                framework_instruction = 6 * ' '
                instruction = 'AI is playing'

                print(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 4) + term.bold + color_back('      Turn : ' + teams + '      '))
                print(term.move_xy(int(25 + (game_dict['map'][0] * 3) / 2 + 4), game_dict['map'][1] * 2 + 5) + term.bold + color_back(framework + str(count_round) + framework_back))

                if (teams == 'team_1' and type_1 == 'AI') or (teams == 'team_2' and type_2 == 'AI'):
                    print(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 6) + term.bold + color_back(framework_instruction + instruction + framework_instruction))
                else:
                    print(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 6) + term.bold + color_back('    Give your order :    '))


                if count % 2 == 0:

                    # get orders of player 1 and notify them to player 1, if necessary
                    if type_1 == 'remote':
                        orders = get_remote_orders(connection)

                    # get orders of the human player
                    elif type_1 == 'human':
                        order = input(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 7))
                        orders = order.split(' ')
                        print(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 7) + '                                                                                                    ')

                    # get orders of the AI
                    else:
                        teams = 'team_1'
                        orders = get_AI_orders(game_dict, teams)
                        if type_2 == 'remote':
                            notify_remote_orders(connection, orders)

                else:
                    # get orders of player 2 and notify them to player 1, if necessary
                    if type_2 == 'remote':
                        orders = get_remote_orders(connection)

                    # get orders of the human player
                    elif type_2 == 'human':
                        order = input(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 7))
                        orders = order.split(' ')
                        print(term.move_xy(int(29 + (game_dict['map'][0] * 3) / 2), game_dict['map'][1] * 2 + 7) + '                                                                                                     ')

                    # get orders of the AI
                    else:
                        teams = 'team_2'
                        orders = get_AI_orders(game_dict, teams)
                        if type_1 == 'remote':
                            notify_remote_orders(connection, orders)

                pacify_list, feed_list, attack_list, move_list = deal_orders(orders)


                if count_pacify == 2:
                    pacify_wolf_list = []

                bonus_dict = bonus(game_dict, teams)
                
                #Apply the orders in the right order
                if pacify_list !=[]:
                    pacify_wolf_list = pacify(game_dict, pacify_list, teams, term)
                    count_pacify = 0
                if feed_list != []:
                    feed(game_dict, feed_list, term, teams)
                if attack_list != []:
                    fight(game_dict, attack_list, bonus_dict, pacify_wolf_list, term, teams)
                    pacify_wolf_list = []
                    count_attack = 0
                if move_list != []:
                    move(game_dict, move_list, term, teams)

                count_pacify += 1
                count += 1
                   
        #If any werewolves has received damages during the last 200 rounds the game is over and then we count the total energy of each team
        new_coord = calcul_grid(0, (game_dict['map'][1] + 14))
        if count_attack >= 200:
            if count_energy(game_dict) == "Team 1":
                print(term.move_xy(new_coord[0], new_coord[1])+term.bold + term.red("\n ______  ____    ______                  _      __      __  _____   __  __      __     \n/\__  _\/\  _`\ /\  _  \  /'\_/`\      /' \    /\ \  __/\ \/\  __`\/\ \/\ \    /\ \    \n\/_/\ \/\ \ \L\_\ \ \L\ \/\      \    /\_, \   \ \ \/\ \ \ \ \ \/\ \ \ `\\  \   \ \ \   \n   \ \ \ \ \  _\L\ \  __ \ \ \__\ \   \/_/\ \   \ \ \ \ \ \ \ \ \ \ \ \ , ` \   \ \ \  \n    \ \ \ \ \ \L\ \ \ \/\ \ \ \_/\ \     \ \ \   \ \ \_/ \_\ \ \ \_\ \ \ \`\ \   \ \_\ \n     \ \_\ \ \____/\ \_\ \_\ \_ \\ \_\     \ \_\   \ `\___x___/\ \_____\ \_\ \_\   \/\_\ \n      \/_/  \/___/  \/_/\/_/\/_/ \/_/      \/_/    '\/__//__/  \/_____/\/_/\/_/    \/_/ "))
            elif count_energy(game_dict) == "Team 2":
                print(term.move_xy(new_coord[0], new_coord[1])+term.bold + term.dodgerblue2("\n ______  ____    ______                   ___       __      __  _____   __  __      __     \n/\__  _\/\  _`\ /\  _  \  /'\_/`\       /'___`\    /\ \  __/\ \/\  __`\/\ \/\ \    /\ \    \n\/_/\ \/\ \ \L\_\ \ \L\ \/\      \     /\_\ /\ \   \ \ \/\ \ \ \ \ \/\ \ \ ` \\ \   \ \ \   \n   \ \ \ \ \  _\L\ \  __ \ \ \__\ \    \/_/// /__   \ \ \ \ \ \ \ \ \ \ \ \ , ` \   \ \ \  \n    \ \ \ \ \ \L\ \ \ \/\ \ \ \_/\ \      // /_\ \   \ \ \_/ \_\ \ \ \_\ \ \ \`\ \   \ \_\ \n     \ \_\ \ \____/\ \_\ \_\ \_ \\ \_\    /\______/    \ `\___x___/\ \_____\ \_\ \_\   \/\_\ \n      \/_/  \/___/  \/_/\/_/\/_/ \/_/    \/_____/      '\/__//__/  \/_____/\/_/\/_/    \/_/"))
            else:
                print(term.move_xy(new_coord[0], new_coord[1])+term.bold + term.green("\n ____    ____    ______  __      __      __     \n/\  _`\ /\  _`\ /\  _  \/\ \  __/\ \    /\ \    \n\ \ \/\ \ \ \L\ \ \ \L\ \ \ \/\ \ \ \   \ \ \   \n \ \ \ \ \ \ ,  /\ \  __ \ \ \ \ \ \ \   \ \ \  \n  \ \ \_\ \ \   \\ \\ \ \/\ \ \ \_/ \_\ \   \ \_\ \n   \ \____/\ \_\ \_\ \_\ \_\ `\___x___/    \/\_\ \n    \/___/  \/_/\/ /\/_/\/_/'\/__//__/      \/_/"))

        else:
            if win(game_dict) == "Team 1":
                print(term.move_xy(new_coord[0], new_coord[1])+term.bold + term.red("\n ______  ____    ______                  _      __      __  _____   __  __      __     \n/\__  _\/\  _`\ /\  _  \  /'\_/`\      /' \    /\ \  __/\ \/\  __`\/\ \/\ \    /\ \    \n\/_/\ \/\ \ \L\_\ \ \L\ \/\      \    /\_, \   \ \ \/\ \ \ \ \ \/\ \ \ `\\  \   \ \ \   \n   \ \ \ \ \  _\L\ \  __ \ \ \__\ \   \/_/\ \   \ \ \ \ \ \ \ \ \ \ \ \ , ` \   \ \ \  \n    \ \ \ \ \ \L\ \ \ \/\ \ \ \_/\ \     \ \ \   \ \ \_/ \_\ \ \ \_\ \ \ \`\ \   \ \_\ \n     \ \_\ \ \____/\ \_\ \_\ \_ \\ \_\     \ \_\   \ `\___x___/\ \_____\ \_\ \_\   \/\_\ \n      \/_/  \/___/  \/_/\/_/\/_/ \/_/      \/_/    '\/__//__/  \/_____/\/_/\/_/    \/_/ "))
            elif win(game_dict) == "Team 2":
                print(term.move_xy(new_coord[0], new_coord[1])+term.bold + term.dodgerblue2("\n ______  ____    ______                   ___       __      __  _____   __  __      __     \n/\__  _\/\  _`\ /\  _  \  /'\_/`\       /'___`\    /\ \  __/\ \/\  __`\/\ \/\ \    /\ \    \n\/_/\ \/\ \ \L\_\ \ \L\ \/\      \     /\_\ /\ \   \ \ \/\ \ \ \ \ \/\ \ \ ` \\ \   \ \ \   \n   \ \ \ \ \  _\L\ \  __ \ \ \__\ \    \/_/// /__   \ \ \ \ \ \ \ \ \ \ \ \ , ` \   \ \ \  \n    \ \ \ \ \ \L\ \ \ \/\ \ \ \_/\ \      // /_\ \   \ \ \_/ \_\ \ \ \_\ \ \ \`\ \   \ \_\ \n     \ \_\ \ \____/\ \_\ \_\ \_ \\ \_\    /\______/    \ `\___x___/\ \_____\ \_\ \_\   \/\_\ \n      \/_/  \/___/  \/_/\/_/\/_/ \/_/    \/_____/      '\/__//__/  \/_____/\/_/\/_/    \/_/"))

        # close connection, if necessary
        if type_1 == 'remote' or type_2 == 'remote':
            close_connection(connection)

    else:
        print("Change the size of your map : min size = (20, 20) and max_size = (40, 60)")
            
play_game('Code/myfiles.ano', 13, "AI", 27, "AI")
#
# Work on remote functions
#
# PX_game_mode
# PX_type
#
# Our group is 20

"""
def play_game(map_path, group_1, type_1, group_2, type_2):
Parameters
----------
map_path: path of map file(str)
group_1: group of player 1 (int)
type_1: type of player 1 (str)
group_2: group of player 2 (int)
type_2: type of player 2 (str)
"""

# create connection, if necessary
if type_1 == 'remote':
    connection = create_connection(group_2, group_1)
elif type_2 == 'remote':
    connection = create_connection(group_1, group_2)

...

# get orders of player 1 and notify them to player 2, if necessary
if type_1 == 'remote':
    orders = get_remote_orders(connection)
else:
    orders = get_AI_orders(..., 1)
    if type_2 == 'remote':
        notify_remote_orders(connection, orders)

# get orders of player 2 and notify them to player 1, if necessary
if type_2 == 'remote':
    orders = get_remote_orders(connection)
else:
    orders = get_AI_orders(..., 2)
    if type_1 == 'remote':
        notify_remote_orders(connection, orders)

...
...
...

# close connection, if necessary
if type_1 == 'remote' or type_2 == 'remote':
    close_connection(connection)
        
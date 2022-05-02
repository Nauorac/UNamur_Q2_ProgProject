
import random

# 2 coordonnées de test
target = [3, 4]
ww_coords = [1, 1]
# Une liste de case vides selon le schéma suivant:
"""
T = Target
W = Wolf
X = Wall

	1 	2 	3	4
1 | T | _ | _ | _ |
2 | _ | X | X | _ |
3 | _ | _ | _ | W |
4 | _ | _ | _ | _ |
"""
current_empty_spaces = [(2, 4), (2, 5), (3, 3), (3, 5), (4, 3), (4, 4), (4, 5), (2, 1), (1, 2)]

# -------------------------------------------------
going_to = {"N": [-1, 0], "NE": [-1, +1], "E": [0, +1], "SE": [+1, +1], "S": [+1, 0], "SW": [+1, -1], "W": [0, -1], "NW": [-1, -1]}

alt_dir = {"N": ["NW", "NE"], "S": ["SW", "SE"], "E": ["NE", "SE"], "W": ["NW", "SW"], "NE": ["N", "E"], "SE": ["S", "E"], "NW": ["N", "W"], "SW": ["S", "W"]}
# -------------------------------------------------

def target_direction(ww_coords, target):
	"""_summary_

	Args:
		ww_coords (_type_): _description_
		target (_type_): _description_

	Returns:
		_type_: _description_
	"""
	xf = target[0] - ww_coords[0]  # x final
	yf = target[1] - ww_coords[1]  # y final
	if xf > 0:
		if yf > 0:
			return "SE"
		elif yf < 0:
			return "SW"
		else:
			return "S"
	elif xf < 0:
		if yf > 0:
			return "NE"
		elif yf < 0:
			return "NW"
		else:
			return "N"
	else:
		if yf > 0:
			return "E"
		elif yf < 0:
			return "W"
	#Direction cible = direction de Y (N, S, nothing) + direction de X (W, E, nothing)
	dirf = ""+Priory+""+Priorx+""
	print("Direction cible : "+dirf)
	return dirf

temp_target_dir = target_direction(ww_coords, target)

print("********************") # -------------------------------------------------

def test_move(ww_coords, temp_target_dir):
	xtemp = ww_coords[0] + going_to[temp_target_dir][0]
	ytemp = ww_coords[1] + going_to[temp_target_dir][1]
	while (xtemp, ytemp) not in current_empty_spaces:
		#print("Current target case = ("+str(xtemp)+","+str(ytemp)+")")
		#print("----")
		new_direction = random.choice(alt_dir[temp_target_dir])
		print("New direction = "+new_direction)
		xtemp = ww_coords[0] + going_to[new_direction][0]
		ytemp = ww_coords[1] + going_to[new_direction][1]
		print("New target case = ("+str(xtemp)+","+str(ytemp)+")")
	#print("----")
	print("Final direction = "+new_direction)
	#Return final coordinates
	return (xtemp, ytemp)

print("TEST 1")
test_move(ww_coords, temp_target_dir)

#print("TEST 2")
#Add wall in (2, 4)
#current_empty_spaces.remove((2, 4))

print("TEST 3")
#Add wall in (1, 2)
current_empty_spaces.remove((1, 2))

test_move(ww_coords, temp_target_dir)


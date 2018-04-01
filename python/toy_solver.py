import math
import pulp
import re

def generateGrid(n, m, popArray):
	if (n * m != len(popArray)):
		return "ERROR: invalid input arguments"



# Returns true if two blocks x,y are adjacent
# on an n x m grid,
# false otherwise.
# The adjacent_dist value is set to default at 1
# so that only blocks directly touching each other are
# considered proximal. However, it can be changed to other
# positive integers to simulate the larger area of effect
# of bigger candidate parcels.
def is_adjacent(x, y, n, m, adjacent_dist = 1):
	block_one_row = math.ceil(x/m)
	block_one_col = x % m
	if block_one_col == 0:
		block_one_col = m
	block_two_row = math.ceil(y/m)
	block_two_col = y % m
	if block_two_col == 0:
		block_two_col = m
	return (math.fabs(block_one_row - block_two_row) <= adjacent_dist and math.fabs(block_one_col - block_two_col) <= adjacent_dist)

#
# Calculates the number of people that would benefit
# from construction of a park
#
#

def calculate_beneficiaries(candidate_parcels, n, m):
	set_j = []
	candidates = []
	lots = range(1, n*m+1)

	for i in candidate_parcels:
		candidates.append(i)
		for j in [x for x in lots if x not in candidate_parcels]:
			if is_adjacent(i,j,n,m):
				candidates.append(j)
		set_j.append(candidates[:])
		candidates.clear()


	for s in set_j:
		print(*s)


# Method to generate the set J, that is
# the set of parcels that would benefit
# from the construction of a new park.
# we store these sets as a list of lists,
# with the first item in each sublist indicating
# i, the candidate parcel which when constructed
# would benefit the next parcels in the sublist
#
# we use the highly iniefficient naive algorithm 
# of brute force checking for proximality
#
# INPUT
# candidate_parcels - the list of candidate parcels
# n , m - the dimensions of the grid 
def generate_set_j_no_string(candidate_parcels, n, m, pop_dict):
	lots = range(1, n*m+1)
	set_j = []
	pop_sum = {}

	for i in candidate_parcels:
		for j in [x for x in lots if x not in candidate_parcels]:
			if is_adjacent(i,j,n,m):
				if i in pop_sum:
					pop_sum[i] = pop_sum[i] + pop_dict[j]
				else:
					pop_sum[i] = pop_dict[j]
				if j not in set_j:
					set_j.append(j)
	#print(set_j)
	return sorted(set_j), pop_sum

def generate_set_j(candidate_parcels, n, m):
	lots = range(1, n*m+1)
	set_j = []

	for i in candidate_parcels:
		for j in [x for x in lots if x not in candidate_parcels]:
			if is_adjacent(i,j,n,m):
				if ('z' + str(j)) not in set_j:
					set_j.append('z' + str(j))
	#print(set_j)
	return set_j

#
# Method to generate the sets W_j, for j in J
#
def generate_sets_w(candidate_parcels, n, m, benefitting_sets):
	
	list_of_w_sets = {}
	w_j = []

	for j in benefitting_sets:
		#w_j.append('w'+ str(j))
		for i in candidate_parcels:
			if is_adjacent(i,j,n,m):
				if i not in w_j:
					w_j.append(i)
		list_of_w_sets[j] = w_j[:]
		w_j.clear()

	return list_of_w_sets
	#for s in list_of_w_sets:
	#	print(*s)

#
# If num is a list of numbers
# then append the letter to each item in the list
#
# Else append letter to a given number
#
def append_letter(letter, num):
	if type(num) is list:
		appended = []
		for n in num:
			appended.append(letter + str(n))
		return appended
	elif type(num) is dict:
		appended = {}
		for key, val in num.items():
			appended[letter + str(key)] = val	
		return appended
	return letter + str(num)


def solveLP(obj_function, obj_string, 
	candidate_parcels, vars_z, vars_y, max_parks, sets_w, extra_constraint = None):

	# Initialize park location problem
	park_location_model = pulp.LpProblem("Park Location Model: {0}".format(obj_string), pulp.LpMaximize)
	# Add objective function
	park_location_model += obj_function , obj_string

	# Add constraint on maximum number of parks built
	park_location_model += pulp.lpSum([vars_y[y] for y in candidate_parcels]) <= max_parks, "Can only build {0} park(s)".format(max_parks)


	# attempt to add some constraints
	for key, val in vars_z.items():
		num = extract_num(key)
		y_constraints = sets_w[num]


		lp_sum = pulp.lpSum([vars_y[y] for y in y_constraints])

 		# these are the conditions of the form
		# z_j <= sum (y_i) for i in W_j
		# followed by the label
		condition_one = lp_sum >= val
		label_one = "If lot {0} is serviced at least one park is built".format(num)

		# these are the conditions of the form 
		# |W_j| * z_j >= sum(y_i) for i in W_j
		# followed by the label
		condition_two = len(y_constraints) * val >= lp_sum
		label_two = "If a park serving lot {0} is picked then lot {1} must be serviced".format(num,num)

		# adding both conditions to the model
		park_location_model += condition_one, label_one
		park_location_model += condition_two, label_two

	# Add extra constrain which will be the deterioration for an objective
	if extra_constraint is not None: 
		park_location_model += extra_constraint , "Objective function deterioration"

	# The problem data is written to an .lp file
	park_location_model.writeLP("Model-{0}.lp".format(obj_string))

	# The problem is solved using PuLP's choice of Solver
	park_location_model.solve()

	# The status of the solution is printed to the screen
	print ("Status:", pulp.LpStatus[park_location_model.status])

	# Each of the variables is printed with its resolved optimum value
	for v in park_location_model.variables():
		print (v.name, "=", v.varValue)

	# The optimised objective function value is printed to the screen
	print ("{0} = ".format(obj_string), pulp.value(park_location_model.objective))

	return park_location_model	

def place_parks(candidate_parcels, n, m, max_parks, population, lower = 10, 
	upper = 15, step = 5):

	set_j, pop_sum = generate_set_j_no_string(candidate_parcels, n, m, population)
	sets_w = generate_sets_w(candidate_parcels, n, m, set_j)
	set_j = append_letter('z', set_j)
	
	# forms dictionary of number and variable pairs
	set_i_dict = {}
	for i in candidate_parcels:
		set_i_dict[i] = append_letter('y', i) 

	# form the variables in the objective function
	vars_z = {}
	vars_y = {}
	for z in set_j:
		vars_z[z] = pulp.LpVariable(z, lowBound = 0, upBound = 1, cat = 'Integer')
	for key, val in set_i_dict.items():
		vars_y[key] = pulp.LpVariable(val, lowBound = 0, upBound = 1, cat = 'Integer')

	# putting together the first objective function which
    # maximizes geographical service area of candidate parcels
	block_objective = ''
	for key, val in vars_z.items():
		block_objective += val

	# population objective function
	pop_objective = pulp.lpSum(vars_y[y] * pop_sum[y] for y in candidate_parcels)


	# Setting up LP and solving it for servie area objective
	print("Solving in isolation for service area objective function\n-------------------")
	LP1 = solveLP(block_objective, 
		"Maximum number of blocks serviced", candidate_parcels, 
		vars_z, vars_y, max_parks, sets_w)

	LP1_obj_value = pulp.value(LP1.objective)

	# Setting up new LP and solving it for population objective
	print("Solving in isolation for population objective function\n-------------------")
	LP2 = solveLP(pop_objective, 
		"Maximum number of beneficiaries", candidate_parcels, 
		vars_z, vars_y, max_parks, sets_w)

	

	for i in range(lower, upper, step):
		# maximum acceptable deterioration amount
		det_amount = i / 100
		deterioration = LP1.objective >= (1 - det_amount) * LP1_obj_value
		# SOLVING BOTH THINGIES! SO EXCITING
		print("Solving both objective functions\n-------------------")
		print("Acceptable deterioration value: {0}%".format(i))
		LP3 = solveLP(pop_objective, 
			"Maximizing beneficiaries considering blocks serviced", candidate_parcels,
			vars_z, vars_y, max_parks, sets_w, deterioration)



# Returns first match of an integer in a string
def extract_num(letters):
	num = (re.search('\d+', letters))
	return (int(num[0]))

#print(generate_sets_w([1,3,12,15,19,21],5,5))
lower = int(input("Enter the lower acceptable deterioration amount (to allow for only 10 percent deterioration, enter 10):"))
upper = int(input("Enter the upper acceptable deterioration amount (to allow for only 90 percent deterioration, enter 90):"))
step = int(input("Enter the step value (to jump by 5 percent enter 5):"))

#candidates = [3,12,15,16,24,38,45,47,49,55,59,66,72,78,98,104,107,108,110,117,122,134,146]
#pop_dict = {1:50, 2:55, 4:45, 5:60, 6:85, 7:65, 8:120, 9:105, 10:95, 11:85, 13:65, 14:45, 17:50, 18:45, 19:60, 20:110, 21:120, 22:95, 23:110, 25:100, 26:65, 27:75, 28:40, 29:45, 30:30, 31:80, 32:75, 33:55, 34:70, 35:105, 36:130, 37:115, 39:105, 40:115, 41:80, 42:50, 43:65, 44:50, 46:165, 48:65, 50:65, 51:80, 52:95, 53:110, 54:105, 56:70, 57:55, 58:45, 60:25, 61:225, 62:200, 63:70, 64:75, 65:100, 67:100, 68:105, 69:120, 70:105, 71:55, 73:20, 74:25, 75:15, 76:250, 77:120, 79:85, 80:105, 81:100, 82:110, 83:70, 84:80, 85:70, 86:65, 87:50, 88:15, 89:5, 90:10, 91:200, 92:100, 93:180, 94:155, 95:125, 96:105, 97:80, 99:95, 100:75, 101:40, 102:45, 103:35, 105:15, 106:250, 109:145, 111:235, 112:100, 113:80, 114:135, 115:95, 116:70, 118:50, 119:45, 120:20, 121:300, 123:265, 124:205, 125:235, 126:505, 127:500, 128:245, 129:175, 130:80, 131:85, 132:65, 133:60, 135:25, 136:305, 137:255, 138:275, 139:215, 140:225, 141:400, 142:405, 143:410, 144:500, 145:305, 147:75, 148:50, 149:40, 150:30}
candidates = [1,3,12,15,19,21]
pop_dict = {1:0, 2:200, 3:0, 4:200, 5:30, 6:50, 7:100, 8:150, 9:160, 10:20, 11:45, 12:0, 13:150, 14:140, 15:0, 16:40, 17:50, 18:130, 19:0, 20:90, 21:0, 22:60, 23:95, 24:80, 25:55}
place_parks(candidates,5,5,1, pop_dict, lower, upper, step)
#place_parks(candidates, 10, 15, 5, pop_dict, lower, upper, step)

print('hello')				
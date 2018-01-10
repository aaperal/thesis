import math
import pulp
import re

def generateGrid(n, m, popArray):
	if (n * m != len(popArray)):
		return "ERROR: invalid input arguments"



# returns true if
# two blocks x,y are adjacent
# on an n x m grid
# false otherwise 
def is_adjacent(x, y, n, m):
	block_one_row = math.ceil(x/m)
	block_one_col = x % m
	if block_one_col == 0:
		block_one_col = m
	block_two_row = math.ceil(y/m)
	block_two_col = y % m
	if block_two_col == 0:
		block_two_col = m
	return (math.fabs(block_one_row - block_two_row) <= 1 and math.fabs(block_one_col - block_two_col) <= 1)

# method to generate the set J, that is
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
def get_beneficiaries(candidate_parcels, n, m):
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

def generate_set_j_no_string(candidate_parcels, n, m):
	lots = range(1, n*m+1)
	set_j = []

	for i in candidate_parcels:
		for j in [x for x in lots if x not in candidate_parcels]:
			if is_adjacent(i,j,n,m):
				if j not in set_j:
					set_j.append(j)
	#print(set_j)
	return sorted(set_j)

def generate_set_j(candidate_parcels, n, m):
	lots = range(1, n*m+1)
	set_j = []

	for i in candidate_parcels:
		for j in [x for x in lots if x not in candidate_parcels]:
			if is_adjacent(i,j,n,m):
				if j not in set_j:
					set_j.append('z' + str(j))
	#print(set_j)
	return set_j

def generate_sets_w(candidate_parcels, n, m):
	benefitting_sets = generate_set_j_no_string(candidate_parcels, n, m)
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
#get_beneficiaries([1,3,12,15,19,21],5,5)

#
# appends letter to a given number
#
def append_letter(letter, num):
	return letter + str(num)

def placeParks(candidate_parcels, n, m):
	set_j = generate_set_j(candidate_parcels, n, m)
	sets_w = generate_sets_w(candidate_parcels, n, m)
	#set_i = append_letter(candidate_parcels, 'y')

	# forms dictionary of number and variable pairs
	set_i_dict = {}
	for i in candidate_parcels:
		set_i_dict[i] = append_letter('y', i) 

	# initialize park location problem
	park_location_problem = pulp.LpProblem("Park Location Problem", pulp.LpMaximize)

	# form the variables in the objective function
	vars_z = {}
	vars_y = {}
	for z in set_j:
		vars_z[z] = pulp.LpVariable(z, lowBound = 0, upBound = 1, cat = 'Integer')
	for key, val in set_i_dict.items():
		vars_y[key] = pulp.LpVariable(val, lowBound = 0, upBound = 1, cat = 'Integer')

	# putting together the first objective function
	temp_function = ''
	for key, val in vars_z.items():
		temp_function += val

	park_location_problem += temp_function , "the maximum number of blocks serviced"

	# attempt to add some constraints

	for key, val in vars_z.items():
		num = extract_num(key)
		y_constraints = sets_w[num]
		label = "Ensures if lot %d is serviced at least one park is built" % num
		condition = pulp.lpSum([vars_y[y] for y in y_constraints]) >= val
		park_location_problem += condition, label
	park_location_problem.writeLP("ParkLocationModel.lp")

# returns first match of an integer in letters string
def extract_num(letters):
	num = (re.search('\d+', letters))
	return (int(num[0]))

#print(generate_sets_w([1,3,12,15,19,21],5,5))
placeParks([1,3,12,15,19,21],5,5)
print('hello')				
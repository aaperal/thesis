import math
import pulp

def generateGrid(n, m, popArray):
	if (n * m != len(popArray)):
		return "ERROR: invalid input arguments"



# returns true if
# two blocks x,y are adjacent
# on an n x m grid
# false otherwise 
def isAdjacent(x, y, n, m):
	row_x = math.ceil(x/m)
	col_x = x % m
	if col_x == 0:
		col_x = m
	row_y = math.ceil(y/m)
	col_y = y % m
	if col_y == 0:
		col_y = m
	return (math.fabs(row_x - row_y) <= 1 and math.fabs(col_x - col_y) <= 1)

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
# candidateParcels - the list of candidate parcels
# n , m - the dimensions of the grid 
def generateBeneficiaries(candidateParcels, n, m):
	set_j = []
	candidates = []
	lots = range(1, n*m+1)

	for i in candidateParcels:
		candidates.append(i)
		for j in [x for x in lots if x not in candidateParcels]:
			if isAdjacent(i,j,n,m):
				candidates.append(j)
		set_j.append(candidates[:])
		candidates.clear()


	for s in set_j:
		print(*s)

def generateSetJNoString(candidateParcels, n, m):
	lots = range(1, n*m+1)
	set_j = []

	for i in candidateParcels:
		for j in [x for x in lots if x not in candidateParcels]:
			if isAdjacent(i,j,n,m):
				if j not in set_j:
					set_j.append(j)
	#print(set_j)
	return sorted(set_j)

def generateSetJ(candidateParcels, n, m):
	lots = range(1, n*m+1)
	set_j = []

	for i in candidateParcels:
		for j in [x for x in lots if x not in candidateParcels]:
			if isAdjacent(i,j,n,m):
				if j not in set_j:
					set_j.append('z' + str(j))
	#print(set_j)
	return set_j

def generateSetsW(candidateParcels, n, m):
	benefitting_sets = generateSetJNoString(candidateParcels, n, m)
	listofws = []
	w_j = []

	for j in benefitting_sets:
		w_j.append('w_'+ str(j))
		for i in candidateParcels:
			if isAdjacent(i,j,n,m):
				if i not in w_j:
					w_j.append(i)
		listofws.append(w_j[:])
		w_j.clear()

	for s in listofws:
		print(*s)
#generateBeneficiaries([1,3,12,15,19,21],5,5)
myJs = generateSetJ([1,3,12,15,19,21],5,5)
#myWs = generateSetsW([1,3,12,15,19,21],5,5)

#park_location_problem = pulp.LpProblem("Park Location Problem", pulp.LpMaximize)
#vars = {}
#for z in my 

print('hello')				
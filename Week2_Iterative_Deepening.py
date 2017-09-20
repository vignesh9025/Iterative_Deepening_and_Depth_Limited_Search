# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- IMPLEMENTATION OF 8 PUZZLE PROBLEM --------------------------------------------------------------------------
# ------------------------------- AUTHOR: VIGNESH M. PAGADALA ---------------------------------------------------------------------------------
# ------------------------------- FILE: Week2_8_Puzzle.py.py ----------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- DEPTH-LIMITED SEARCH ----------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTION WHICH TAKES IN A STATE AND PRINTF IT OUT

def printState_8p(state):
    ctr = 0
    for i in range(3):
        for j in range(3):
            if state[ctr] == 0:
                print(' ', end = ' ')
            else:
                print(state[ctr], end=' ')
            ctr += 1
        print()
        
# FUNCTION WHIH PRINTS OUT THE SOLUTION PATH

def printPath_8p(startState, goalState, path):
    l = len(path)
    print("The path from %s to %s is %d nodes long." % (startState, goalState, l))
    print()
    print(type(path))
    print()
    for p in path:
        printState_8p(p)
        print()
       

# LET US FIRSTLY DEFINE A FUNCTION WHICH TAKES IN X INDEX AND Y INDEX VALUES, AND RETURNS THE SIMPLE-LIST INDEX

def matrix_to_list(x, y):
	counter = 0
	for i in range(3):
		for j in range(3):
			if i == x and j == y:
				return counter
			counter += 1
	return 'Index does not exist!'

# FUNCTION WHICH TAKES IN A SIMPLE-LIST INDEX AND RETURNS X, Y VALUES

def list_to_matrix(x):
	counter = 0
	for i in range(3):
		for j in range(3):
			if counter == x:
				return i, j
			counter += 1
	return 'Index does not exist!'

# FUNCTION TO FIND THE BLANK IN A GIVEN STATE

def findBlank_8p(state):
	ctr = 0
	for i in state:
		if i == 0:
			return list_to_matrix(ctr)
		ctr += 1
	return 'Blank not found!'

# FUNCTION TO SWAP TWO POSITIONS IN A 2D MATRIX

def swap(state, x1, y1, x2, y2):
	temp = state[matrix_to_list(x1, y1)]
	state[matrix_to_list(x1, y1)] = state[matrix_to_list(x2, y2)]
	state[matrix_to_list(x2, y2)] = temp

# NOW LET'S CREATE THE ACTIONSF FUNCTION WHICH CAN GENERATE ALL POSSIBLE VALID ACTIONS

def actionsF(state):

	# FIRSTLY, WE DETERMINE WHERE THE BLANK IS LOCATED
	blank = findBlank_8p(state)

	# LET'S INITIALIZE THE VALID ACTIONS LIST
	validActions = []

	# NOW WE USE A SET OF CONDITIONALS AND KEEP APPENDING TO validActions
	
	# FOR GOING LEFT, CONDITION IS (Y != 0)
	if blank[1] != 0:
		validActions.append('left')
	# FOR GOING RIGHT, CONDITION IS (Y != 2)
	if blank[1] != 2:
		validActions.append('right')
	# FOR GOING UP, CONDITION IS (X != 0)
	if blank[0] != 0:
		validActions.append('up')
	# FOR GOING DOWN, CONDITION IS (X != 2)
	if blank[0] != 2:
		validActions.append('down')

	return validActions

import copy

# TAKEACTIONS FUNCTION

def takeActionF(state, action):

	# DETERMINE BLANK LOCATION
	blank = findBlank_8p(state)
	state2 = copy.copy(state)
	# MOVING LEFT
	if action == 'left':
		swap(state2, blank[0], blank[1], blank[0], blank[1] - 1)

	# MOVING RIGHT
	if action == 'right':
		swap(state2, blank[0], blank[1], blank[0], blank[1] + 1)

	# MOVING UP
	if action == 'up':
		swap(state2, blank[0], blank[1], blank[0] - 1, blank[1])

	# MOVING DOWN
	if action == 'down':
		swap(state2, blank[0], blank[1], blank[0] + 1, blank[1])

	return state2

def depthLimitedSearch(state, goalState, actionsF, takeActionF, depthLimit):
	if state == goalState:
		return []
	if depthLimit == 0:
		return 'cutoff'
	cutoffOccurred = False
	for action in actionsF(state):
		childState = takeActionF(state, action)
		result = depthLimitedSearch(childState, goalState, actionsF, takeActionF, depthLimit - 1)
		if result == 'cutoff':
			cutoffOccurred = True
		elif result != 'failure':
			result.insert(0, childState)
			return result
	if cutoffOccurred:
		return 'cutoff'
	else:
		return 'failure'

def iterativeDeepeningSearch(startState, goalState, actionsF, takeActionF, maxDepth):
	for depth in range(maxDepth):
		result = depthLimitedSearch(startState, goalState, actionsF, takeActionF, depth)
		if result == 'failure':
			return 'failure'
		if result != 'cutoff':
			result.insert(0, startState)
			return result
	return 'cutoff'


if __name__ == '__main__':
	
	state = [1, 0, 3, 4, 2, 6, 7, 5, 8]
	goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

	#print(depthLimitedSearch(state, goalState, actionsF, takeActionF, 2))
	#path = iterativeDeepeningSearch(state, goalState, actionsF, takeActionF, 10)
	#print(findBlank_8p(state))
	printState_8p(state)



#def depthLimitedSearch(startState, goalState, actionsF, takeActionF, depthLimit):



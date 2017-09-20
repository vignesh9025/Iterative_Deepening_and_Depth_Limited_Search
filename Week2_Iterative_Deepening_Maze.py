# 8 X 8 MAZE
# THE MAZE WILL HAVE 3 TYPES:
# 	1. EMPTY - ' '
# 	2. WALL - 'W'
#	3. GOAL - 'G'
#	4. ROBOT - 'R'

# FUNCTION WHICH TAKES IN A STATE AND PRINTS IT OUT

def printState_maze(state):
	if state == 'cutoff' or state == 'failure':
		return 'Goal cannot be reached'
	print()
	print()
	ctr = 0
	for i in range(10):
		print('-', end = ' ')
	print()
	for i in range(8):
		for j in range(8):
			if j == 0:
				print('|', end = ' ')
			print(state[ctr], end=' ')
			ctr += 1
			if j == 7:
				print('|', end = ' ')
		print()
	for i in range(10):
		print('-', end = ' ')
        
# FUNCTION WHICH PRINTS OUT THE SOLUTION PATH
 
def printPath_maze(startState, goalState, path):
    l = len(path)
    print('The path from ')
    printState_maze(startState)
    print('\n\nto')
    printState_maze(goalState)
    print('\n\nis %d nodes long.' % l)
    #print("The path from %s to %s is %d nodes long." % (startState, goalState, l))
    print()
    print()
    for p in path:
        printState_maze(p)
        print()

# LET US FIRSTLY DEFINE A FUNCTION WHICH TAKES IN X INDEX AND Y INDEX VALUES, AND RETURNS THE SIMPLE-LIST INDEX       

def matrix_to_list(x, y):
	counter = 0
	for i in range(8):
		for j in range(8):
			if i == x and j == y:
				return counter
			counter += 1
	return 'Index does not exist!'

# FUNCTION WHICH TAKES IN A SIMPLE-LIST INDEX AND RETURNS X, Y VALUES

def list_to_matrix(x):
	counter = 0
	for i in range(8):
		for j in range(8):
			if counter == x:
				return i, j
			counter += 1
	return 'Index does not exist!'

# FUNCTION TO FIND ROBOT POSITION

def findRobot_maze(state):
	ctr = 0
	for i in state:
		if i == 'R':
			return(list_to_matrix(ctr))
		ctr += 1
	return "The robot could not be located."		

# FUNCTION TO SWAP TWO POSITIONS IN A 2D MATRIX

def swap(state, x1, y1, x2, y2):
	temp = state[matrix_to_list(x1, y1)]
	state[matrix_to_list(x1, y1)] = state[matrix_to_list(x2, y2)]
	state[matrix_to_list(x2, y2)] = temp

# THE ACTIONSF_MAZE FUNCTION TAKES IN A GIVEN STATE AND RETURNS ALL THE POSSIBLE MOVES WHICH CAN BE DONE BY THE ROBOT FROM THIS STATE

def actionsF_maze(state):

	#FIND WHERE THE ROBOT IS LOCATED
	robot = findRobot_maze(state)

	#LET'S INITIALIZE THE VALID ACTIONS LIST
	validActions = []

	# LEFT
	if robot[1] != 0 and state[matrix_to_list(robot[0], robot[1] - 1)] != 'W':
		validActions.append('left')

	# RIGHT
	if robot[1] != 7 and state[matrix_to_list(robot[0], robot[1] + 1)] != 'W':
		validActions.append('right')
	# UP
	if robot[0] != 0 and state[matrix_to_list(robot[0] - 1, robot[1])] != 'W':
		validActions.append('up')
	# DOWN
	if robot[0] != 7 and state[matrix_to_list(robot[0] + 1, robot[1])] != 'W':
		validActions.append('down')

	return validActions

import copy

def takeActionF_maze(state, action):

	# DETERMINE ROBOT LOCATION
	robot = findRobot_maze(state)
	state2 = copy.copy(state)
	# MOVING LEFT
	if action == 'left':
		swap(state2, robot[0], robot[1], robot[0], robot[1] - 1)

	# MOVING RIGHT
	if action == 'right':
		swap(state2, robot[0], robot[1], robot[0], robot[1] + 1)

	# MOVING UP
	if action == 'up':
		swap(state2, robot[0], robot[1], robot[0] - 1, robot[1])

	# MOVING DOWN
	if action == 'down':
		swap(state2, robot[0], robot[1], robot[0] + 1, robot[1])

	return state2

def depthLimitedSearch(state, goalState, actionsF, takeActionF, depthLimit):
	if state == goalState:
		return []
	#printState_maze(state)
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
		print("WE'RE AT DEPTH: ", depth)
		result = depthLimitedSearch(startState, goalState, actionsF, takeActionF, depth)
		if result == 'failure':
			return 'failure'
		if result != 'cutoff':
			result.insert(0, startState)
			return result
	return 'cutoff'

if __name__ == '__main__':
	
	state = ['R','W',' ',' ',' ',' ','W',' ',
			 ' ','W','W','W','W',' ','W',' ',
			 ' ',' ',' ',' ','W',' ','W',' ',
			 'W','W',' ','W','W',' ','W',' ',
			 'W',' ',' ',' ',' ',' ',' ',' ',
			 'W',' ',' ','W','W','W',' ',' ',
			 'W',' ','W','W',' ','W','W',' ',
			 ' ',' ',' ',' ',' ',' ',' ',' ']

	goalState = [' ','W',' ',' ',' ',' ','W',' ',
				 ' ','W','W','W','W',' ','W',' ',
				 ' ',' ',' ',' ','W',' ','W',' ',
				 'W','W',' ','W','W',' ','W',' ',
				 'W',' ',' ',' ',' ',' ',' ',' ',
				 'W',' ',' ','W','W','W',' ',' ',
				 'W',' ','W','W',' ','W','W',' ',
				 ' ',' ',' ',' ',' ',' ',' ','R']

	#printState_maze(state)
	#print(state[matrix_to_list(0,1)])
	#print(findRobot(state))
	#swap(state, 0,0,2,0)
	#printState_maze(takeActionF_maze(state, 'down'))

	#print(depthLimitedSearch(state, goalState, actionsF_maze, takeActionF_maze, 13))
	l = iterativeDeepeningSearch(state, goalState, actionsF_maze, takeActionF_maze, 20)
	#l = depthLimitedSearch(state, goalState, actionsF_maze, takeActionF_maze, 10)
	print(l)
	#printPath_maze(state, goalState, l)
	
	





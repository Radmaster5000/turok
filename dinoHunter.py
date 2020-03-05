import random

score = 0
moves = 0
dinosaur = '0'
player = 'R'
empty = '-'
validMove = False


world = {1:{1:empty, 2:empty, 3:empty, 4:empty, 5:empty},
		 2:{1:empty, 2:empty, 3:empty, 4:empty, 5:empty}, 
		 3:{1:empty, 2:empty, 3:empty, 4:empty, 5:empty},
		 4:{1:empty, 2:empty, 3:empty, 4:empty, 5:empty},
		 5:{1:empty, 2:empty, 3:empty, 4:empty, 5:empty}}



#replacing three random tiles with dinosaurs
#THERE IS CURRENTLY A RISK OF THE PLAYER BEING REPLACED.
for j in range(3):
	world[random.randint(1,4)][random.randint(1,4)] = dinosaur
#	print(world['R'])

#replacing the middle tile with the player
world[3][3] = player

# print the game board in a user friendly way including score at the top
def printWorld(world, score):
	print('##############################')
	print('score: ' + str(score) + '            moves: ' + str(moves))
	print('player location: ')
	print('##############################')
	for i in range(1,6):
		for j in range(1,6):
			print(world[j][i], end = '')
		print()


# moving the player around the grid. Boundaries need to be added. 
def movePlayer(world, direction):
	for i in range(1,6):
		for j in range(1,6):			
			if (world[i][j] == player and direction == 'left'):
				world[i-1][j] = player;
				world[i][j] = empty;
				return world
			elif (world[i][j] == player and direction == 'right'):
				world[i+1][j] = player;
				world[i][j] = empty;
				return world
			elif (world[i][j] == player and direction == 'up'):
				world[i][j-1] = player;
				world[i][j] = empty;
				return world
			elif (world[i][j] == player and direction == 'down'):
				world[i][j+1] = player;
				world[i][j] = empty;
				return world

# function to count the number of dinosaurs on the grid and work out the player's score from that
def checkDinoKill(world):
	dinos = 3
	dinoCount = 0
	for i in range(1,6):
		for j in range(1,6):
			if (world[i][j] == dinosaur):
				dinoCount += 1;
	return dinos - dinoCount

def checkValidMove(direction):
	if (direction == 'up' or direction == 'down' or direction == 'left' or direction == 'right'):
		#for i in range(1,6):
		#	for j in range(1,6):			
		#		if (world[i][j] == player and direction == 'left' and ((i-1)>=1)):
		#			return True
		#		elif (world[i][j] == player and direction == 'right' and ((i+1)<=6)):
		#			return True
		#		elif (world[i][j] == player and direction == 'up' and ((j-1)>=1)):
		#			return True
		#		elif (world[i][j] == player and direction == 'down' and ((j+1)<=6)):
		#
		return True
	else:
		return False

while (True):
	
	validMove = False
	score = checkDinoKill(world)
	printWorld(world, score)
	if (score == 3):
		print('congratulations! you won!');
		print('you made ' + str(moves) + ' moves.');
		break
	#loop to check that the user had given a valid input
	while True:
		direction = input()

		validMove = checkValidMove(direction)
		if validMove == False:
			print('sorry, not a valid move')
			continue
		else:
			break

	#if input is okay, increase move count and update world
	moves += 1
	world = movePlayer(world, direction)
	


	
import random

#function that creates an empty world based on the value passed in as an argument
def build_world (n):
	world = []
	for i in range(0, n):
		#create n number of rows
		world.append({})
		for j in range(0, n):	
			#every space is initialised as EMPTY
			world[i].update({j:'empty'})
	#returns a nested list (n x n) of empty values		
	return world

#this function is currently working at identifying the column but needs to identify the row as well
def getKeysByValue(dictOfElements, valueToFind, n):
	listOfKeys = list()
	for i in range(0, n):
		listOfItems = dictOfElements[i].items()
		for item in listOfItems:     #each item is a (key, value) tuple
			if item[1] == valueToFind:
				listOfKeys.append(i)
				listOfKeys.append(item[0])
	return listOfKeys

#this function prints the world as a grid
def printWorld(madeWorld, moves):
	print('#################################')
	print('score:                  moves: ' + str(moves))
	print('player location: ')
	print('#################################')
	for line in range(0, n):
		print(madeWorld[line])
	print()

#function to choose where to put a dinosaur
def dinoPlacer():
	dinoLocation = list()

	dinoLocation.append(int(input('Choose a row >>>')))
	dinoLocation.append(int(input('Choose a column >>>')))

	return dinoLocation

#Returns a boolean depending on whether the proposed move is out of bounds
def checkValidMove(playerLocation, direction, sizeOfWorld):
	if (direction == 'up'):
		if ((playerLocation[0] - 1) < 0):
			return False
		else:
			return True
	elif (direction == 'right'):
		if ((playerLocation[1] + 1) >= sizeOfWorld):
			return False
		else:
			return True
	elif (direction == 'down'):
		if ((playerLocation[0] + 1) >= sizeOfWorld):
			return False
		else:
			return True
	elif (direction == 'left'):
		if ((playerLocation[1] - 1) < 0):
			return False
		else:
			return True

#returns the player's new position as well as their old position
def movePlayer(playerLocation, direction, sizeOfWorld):
	oldPlayerLocation = playerLocation[:]
	
	validMove = checkValidMove(playerLocation, direction, sizeOfWorld)
	print(validMove)
	if (validMove == True):
		if (direction == 'up'):
			playerLocation[0] -= 1
		elif (direction == 'right'):
			playerLocation[1] += 1
		elif (direction == 'down'):
			playerLocation[0] += 1
		elif (direction == 'left'):
			playerLocation[1] -= 1

		return playerLocation, oldPlayerLocation
	else:
		direction = input("""Sorry, that's an invalid move!
			Try again >>> """)
		playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n)
		return playerLocation, oldPlayerLocation

n = int(input("please enter a number: "))
moves = 0
#create a (roughly) middle value to use when placing the player
mid = n/2
mid = int(mid)
#create the world (based on the size n) and save it in the madeWorld variable
madeWorld = build_world(n)

#place player in a random position in the world
madeWorld[random.randint(0,(n-1))][random.randint(0,(n-1))] = 'player'

#get player's location and save it to the playerLocation variable
playerLocation = getKeysByValue(madeWorld, 'player', n)

#asks the player for a location and places the dinosaur there
dinoXY = dinoPlacer()
madeWorld[dinoXY[0]][dinoXY[1]] = 'dinosaur'

printWorld(madeWorld, moves)

while (moves < 5):
	direction = input('Choose a direction >>> ')

	playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n)

	madeWorld[playerLocation[0]][playerLocation[1]] = 'player'
	madeWorld[oldPlayerLocation[0]][oldPlayerLocation[1]] = 'empty'

	moves += 1

	printWorld(madeWorld, moves)
#print('newPlayerLocation: ' + str(playerLocation))
#print('oldPlayerLocation: ' + str(oldPlayerLocation))

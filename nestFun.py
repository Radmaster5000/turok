

n = int(input("please enter a number: "))

#create a (roughly) middle value to use when placing the player
mid = n/2
mid = int(mid)

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
def printWorld(madeWorld):
	print()
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


#create the world (based on the size n) and save it in the madeWorld variable
madeWorld = build_world(n)

#place player in the middle of the world (best as possible)
madeWorld[0][0] = 'player'

printWorld(madeWorld)

playerLocation = getKeysByValue(madeWorld, 'player', n)
print("Keys with value equal to player")
print(playerLocation)
print(madeWorld[playerLocation[0]][playerLocation[1]])

dinoXY = dinoPlacer()
madeWorld[dinoXY[0]][dinoXY[1]] = 'dinosaur'

printWorld(madeWorld)

direction = input('Choose a direction >>> ')

isItValid = checkValidMove(playerLocation, direction, n)
print(isItValid)


import random
import time
from worldID import worldID
from worldDesc import worldDesc
from classTest import *


empty = '-'
player = 'P'
n = 5
moves = 0
possibleDirections = ['up', 'down', 'left', 'right']

# created this so I can have different types of dinosaurs
class Dinosaur:
	def __init__(self, name, hp, speed, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.appearance = appearance

# first screen that loads up for the player
def intro(key):
	
	# repeats until player presses 1, 2, or 3
	while (key != 1 or key != 2 or key != 3):

		print("""

		##  # #  # #### # # # # #  # ### ### ###
		# # # ## # #  # # # # # ## #  #  #   # #
		# # # # ## #  # ### # # # ##  #  ##  ##
		# # # #  # #  # # # # # #  #  #  #   # #
		##  # #  # #### # # ### #  #  #  ### # #

			Welcome to DinoHunter!
		  You're here to hunt dinosaurs!
		  Go find them and capture them.
			   Don't get eaten!

		****************************************

			SELECT AN OPTION:
			1 - Start game
			2 - How to play
			3 - Quit

		****************************************
		   """)

		try:
			key = int(input('>>> '))
			if (key == 1):
				return selectDifficulty()
			elif (key == 2):
				rules()
			elif (key == 3):
				quit()
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')
			
def selectDifficulty():
	print(""" 
	*****************************************
			SELECT DIFFICULTY
	*****************************************

		1. Easy (1 T-rex)
		2. Medium (1 T-rex, 1 Raptor)
		3. Hard (1 T-rex, 2 Raptors)
	""")
	choice = input("Please select difficulty: ")
	if (choice == '1' or choice == '2' or choice == '3'):
		return choice
	else:
		print("Sorry, try again...")
		time.sleep(0.5)
		selectDifficulty()

# selection 2 from the introduction screen
def rules():
	print("""
	*****************************************
			RULES AND STUFF
	*****************************************

	You are the player and you look like this: """ + player)
	print("	There are also dinosaurs. They look like this: " + tRex.appearance + " and " + raptor.appearance)
	print("""	The aim of the game is to catch the dinosaurs by landing 
	on the same space. Use ONLY the following commands:
		'up' to move up
		'down' to move down
		'left' to move left
		'right' to move right
	Pretty self explanatory really, isn't it? """)
	choice = input("	When you're ready, type 'back' to continue...")
	if (choice == 'back'):
		return
	else:
		print("That's not the word 'back', is it?...")
		time.sleep(1)
		rules()


#function that creates an empty world based on the value passed in as an argument
# (n is currently hard coded at the begining)
def build_world (n):
	world = []
	for i in range(0, n):
		#create n number of rows
		world.append({})
		for j in range(0, n):	
			#every space is initialised as EMPTY
			world[i].update({j:empty})
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
def printWorld(moves, score):
	#creates a tuple version of the player's location so it can be used in the worldID dictionary
	playerLocationDictKey = tuple(playerLocation)


	print('\n\n\n\n\n\n')
	print()
	print('#################################')
	print()
	print('score: ' + str(score) + '                 moves: ' + str(moves))
	print()
	print('#################################')
	print(worldDesc[worldID[playerLocationDictKey]])
	print()

	for row in range(0, n):
		for column in range(0, n):
			print(madeWorld[row][column], end = '')
		print()
	print()
	# use this next line as a dictionary lookup to print the description of the playerLocation
	#print(playerLocation)
	#print()	

#function to choose where to put a dinosaur
def dinoPlacer():
	dinoLocation = list()

	dinoLocation.append(random.randint(0, (n-1)))
	dinoLocation.append(random.randint(0, (n-1)))

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
def movePlayer(playerLocation, direction, sizeOfWorld, isItADinosaur):
	oldPlayerLocation = playerLocation[:]
	
	validMove = checkValidMove(playerLocation, direction, sizeOfWorld)
	
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
		if (isItADinosaur == False):
			direction = input("""Sorry, that's not a valid move!
				Try again >>> """)
			playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n, False)
			return playerLocation, oldPlayerLocation
		else:
			print("Dinosaur tried to leave the island. It tries a different direction...")
			playerLocation, oldPlayerLocation = movePlayer(playerLocation, possibleDirections[random.randint(0,3)], n, True)
			return playerLocation, oldPlayerLocation

#function that starts the game loop
def playGame(moves, playerLocation, score):
	
	#creates a random spawn point for the dinosaur, retrying if it clashes
	#with the player's location.
	for dino in listOfDinosaurs:
		dino.dinoXY = dinoPlacer()
		while (dino.dinoXY == playerLocation):
			dino.dinoXY = dinoPlacer()

		madeWorld[dino.dinoXY[0]][dino.dinoXY[1]] = dino.appearance

	printWorld(moves, score)

	win = False

	while (score != targetScore):
		direction = input('Choose a direction >>> ')

		playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n, False)
		# when a player lands on the same space as a dinosaur
		if(playerLocation == dino.dinoXY):
			listOfDinosaurs.pop(listOfDinosaurs.index(dino))
			score += 1
			if (score == targetScore):
				win = True

		madeWorld[playerLocation[0]][playerLocation[1]] = player
		madeWorld[oldPlayerLocation[0]][oldPlayerLocation[1]] = empty

		moves += 1

		printWorld(moves, score)

		if (win == True):
			print("Congrats! You won in " + str(moves) + " moves.")
			quit()

		time.sleep(1)

		for dino in listOfDinosaurs:
			dino.dinoXY, dino.oldDinoXY = movePlayer(dino.dinoXY, possibleDirections[random.randint(0,3)], n, True)

			if (dino.dinoXY == playerLocation):
				print('you dead!')
				quit()

			madeWorld[dino.dinoXY[0]][dino.dinoXY[1]] = dino.appearance
			madeWorld[dino.oldDinoXY[0]][dino.oldDinoXY[1]] = empty

			printWorld(moves, score)

			time.sleep(1)
######################################################################
#                                                                    #
# All this shit below needs to go in the game loop function but last #
#             time I moved it all, everything broke                  #
#                                                                    #
######################################################################

difficulty = intro(0)

if (difficulty == '1'):
	listOfDinosaurs = [dino_1]
elif (difficulty == '2'):
	listOfDinosaurs = [dino_1, dino_2]
elif (difficulty == '3'):
	listOfDinosaurs = [dino_1, dino_2, dino_3]

targetScore = len(listOfDinosaurs)
#create the world (based on the size n) and save it in the madeWorld variable
madeWorld = build_world(n)

#place player in a random position in the world
madeWorld[random.randint(0,(n-1))][random.randint(0,(n-1))] = player

#get player's location and save it to the playerLocation variable
playerLocation = getKeysByValue(madeWorld, player, n)



score = 0

playGame(moves, playerLocation, score)



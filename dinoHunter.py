import random
import time
from worldID import worldID
from worldDesc import worldDesc
from classTest import *
from wordLimiter import wordLimiter
from fight import *


empty = '-'
n = 5
moves = 0
possibleDirections = ['up', 'down', 'left', 'right']
oppositeDirections = { 'right' : 'left', 'left' : 'right', 'up' : 'down', 'down' : 'up' }

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
				return selectPlayer()
			elif (key == 2):
				rules()
			elif (key == 3):
				quit()
			else:
				print('ooops! Try again!')
		except ValueError:
			print('Type a number, stupid!')

def selectPlayer():
	# choice 3 is hidden as it's the test player.
	print(""" 
	*****************************************
			SELECT PLAYER
	*****************************************

		1. Tank (Strong, Slow)
		2. Tracker (Weak, Fast)
		
	Strength:
		Strong = 2hp
		Weak   = 1hp

	Speed:
		Slow   = 1 move per turn
		Fast   = 2 moves per turn

	""")
	choice = input("Please select player: ")
	if (choice == '1' or choice == '2' or choice == '3'):
		return choice
	else:
		print("Sorry, try again...")
		time.sleep(0.5)
		selectPlayer()			
			
def selectDifficulty():
	# choice 4 is a hidden choice for test difficulty
	print(""" 
	*****************************************
			SELECT DIFFICULTY
	*****************************************

		1. Easy (1 T-rex)
		2. Medium (1 T-rex, 1 Raptor)
		3. Hard (1 T-rex, 2 Raptors)
	""")
	choice = input("Please select difficulty: ")
	if (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
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
	print("	There are also dinosaurs. They look like this: " + dino_1.appearance + " and " + dino_2.appearance)
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
	print()
	print('----------------------------')
	print('| UP | DOWN | LEFT | RIGHT |')
	print('----------------------------')
	print()
	#Prints the description of the space but limits the number of words on a line to keep it a neater size in the terminal
	wordLimiter(worldDesc[worldID[playerLocationDictKey]], 6)
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
def checkValidMove(playerLocation, direction, sizeOfWorld, isItADinosaur):
	# first line checks the direction chosen
	if (direction == 'up'):
		# next line checks the chosen space is within the world's boundaries
		if ((playerLocation[0] - 1) < 0):
			# if it's not, deny the move
			return False
		# if it's a valid space in the world, check if the moving character is a dinosaur
		# if they are, check that the chosen space isn't already occupied by a dinosaur
		# if it is, log it, and deny the move
		elif ((isItADinosaur == True) and (madeWorld[playerLocation[0] - 1][playerLocation[1]] == dino_1.appearance or madeWorld[playerLocation[0] - 1][playerLocation[1]] == dino_2.appearance)):
			print('Already a dinosaur there')
			return False
		# if everything's okay to this point, it's a valid move
		else:
			return True
	elif (direction == 'right'):
		if ((playerLocation[1] + 1) >= sizeOfWorld):
			return False
		elif ((isItADinosaur == True) and (madeWorld[playerLocation[0]][playerLocation[1] + 1] == dino_1.appearance or madeWorld[playerLocation[0]][playerLocation[1] + 1] == dino_2.appearance)):
			print('Already a dinosaur there')
			return False
		else:
			return True
	elif (direction == 'down'):
		if ((playerLocation[0] + 1) >= sizeOfWorld):
			return False
		elif ((isItADinosaur == True) and (madeWorld[playerLocation[0] + 1][playerLocation[1]] == dino_1.appearance or madeWorld[playerLocation[0] + 1][playerLocation[1]] == dino_2.appearance)):
			print('Already a dinosaur there')
			return False
		else:
			return True
	elif (direction == 'left'):
		if ((playerLocation[1] - 1) < 0):
			return False
		elif ((isItADinosaur == True) and (madeWorld[playerLocation[0]][playerLocation[1] - 1] == dino_1.appearance or madeWorld[playerLocation[0]][playerLocation[1] - 1] == dino_2.appearance)):
			print('Already a dinosaur there')
			return False
		else:
			return True

#returns the player's new position as well as their old position
def movePlayer(playerLocation, direction, sizeOfWorld, isItADinosaur):
	oldPlayerLocation = playerLocation[:]
	
	validMove = checkValidMove(playerLocation, direction, sizeOfWorld, isItADinosaur)
	
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
		#If it's a player, ask for a valid move until they cooperate
		if (isItADinosaur == False):
			direction = input("""Sorry, that's not a valid move!
				Try again >>> """)
			playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n, False)
			return playerLocation, oldPlayerLocation
		#If it's a dinosaur, keep trying to move them to a valid space
		else:
			#The below print statement was to check if this was working or not
			#print("Dinosaur tried to leave the island. It tries a different direction...")
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
		
		for goes in range(player.speed):

			direction = input('Choose a direction >>> ')

			playerLocation, oldPlayerLocation = movePlayer(playerLocation, direction, n, False)
			# when a player lands on the same space as a dinosaur
			for dino in listOfDinosaurs:
				if(playerLocation == dino.dinoXY):
					#below print statement printed the index of the dinosaur being removed from the array when caught
					#print(listOfDinosaurs.index(dino))
					print("player hp = " + str(player.hp))
					print("player weapon = " + str(player.weapon))
					print("Dinosaur hp = " + str(dino.hp))
					print("Dinosaur bite = " + str(dino.bite))	
					playerHP, dinoHP, playerRun = fightMechanic(player.hp, player.weapon, dino.hp, dino.bite)
					
					if (playerRun == True):
						#print(oppositeDirections[direction])
						playerLocation, oldPlayerLocation = movePlayer(playerLocation, oppositeDirections[direction], n, False)
						# undo last player move
						break
					else:
						if (dinoHP <=0):
							print("You survived your encounter with the dinosaur.")
							print("The dinosaur didn't.")

							time.sleep(3)

							listOfDinosaurs.pop(listOfDinosaurs.index(dino))
							score += 1
							if (score == targetScore):
								win = True
						else:
							print("The dinosaur ate you!")
							quit()

			madeWorld[playerLocation[0]][playerLocation[1]] = player.appearance
			madeWorld[oldPlayerLocation[0]][oldPlayerLocation[1]] = empty

			moves += 1

			printWorld(moves, score)

			#Winning condition
			if (win == True):
				print("Congrats! You won in " + str(moves) + " moves.")
				quit()

		time.sleep(1)

		#Each of the dinosaurs gets to move
		for dino in listOfDinosaurs:
			
			for numberOfMoves in range(dino.speed):

				dino.dinoXY, dino.oldDinoXY = movePlayer(dino.dinoXY, possibleDirections[random.randint(0,3)], n, True)
				if (dino.dinoXY == playerLocation):
					print("player hp = " + str(player.hp))
					print("player weapon = " + str(player.weapon))
					print("Dinosaur hp = " + str(dino.hp))
					print("Dinosaur bite = " + str(dino.bite))
					playerHP, dinoHP, playerRun = fightMechanic(player.hp, player.weapon, dino.hp, dino.bite)
					
					if (playerRun == True):
						# put player in last dinosaur position
						break
					else:
						if (dinoHP <=0):
							print("You survived your encounter with the dinosaur.")
							print("The dinosaur didn't.")

							time.sleep(3)

							listOfDinosaurs.pop(listOfDinosaurs.index(dino))
							score += 1
							if (score == targetScore):
								win = True
						else:
							print("The dinosaur ate you!")
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


playerSelect = intro(0)
if (playerSelect == '1'):
	player = player_1
elif (playerSelect == '2'):
	player = player_2
elif (playerSelect == '3'):
	player = player_test

difficulty = selectDifficulty()

if (difficulty == '1'):
	listOfDinosaurs = [dino_1]
elif (difficulty == '2'):
	listOfDinosaurs = [dino_1, dino_2]
elif (difficulty == '3'):
	listOfDinosaurs = [dino_1, dino_2, dino_3]
elif (difficulty == '4'):
	listOfDinosaurs = [dino_test]

targetScore = len(listOfDinosaurs)
#create the world (based on the size n) and save it in the madeWorld variable
madeWorld = build_world(n)

#place player in a random position in the world
madeWorld[random.randint(0,(n-1))][random.randint(0,(n-1))] = player.appearance

#get player's location and save it to the playerLocation variable
playerLocation = getKeysByValue(madeWorld, player.appearance, n)



score = 0

playGame(moves, playerLocation, score)



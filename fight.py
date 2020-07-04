import random

################################
# These variables will come from the player and dinosaur classes when it's working properly
################################

#playerHP = 60
#playerWeapon = 4
#playerHidden = False

#dinoHP = 10
#dinoBite = 5

#def roll():
#	return random.randint(1,6)

def fightMechanic(playerHP, playerWeapon, dinoHP, dinoBite):

	def playerAttack(playerWeapon, playerHidden, dinoHP):
		print()
		print()
		print()
		print()
		print('----------------------------')
		print('|  FIGHT  |  HIDE  |  RUN  |')
		print('----------------------------')

		print()
		print()
		
		turn = input('> ')



		while (turn != 'fight' and turn != 'hide' and turn != 'run'):
			turn = input('> ')

		roll = random.randint(1,6)
		#print(roll)

		# Series of if statements based on player's input
		
		# If they choose to fight, they need to roll a 1, 2, or 3
		# If they succeed they inflict the amount of damage their weapon carries
		if (turn == 'fight'): 
	
			if (roll <= 3):
				print("You choose to fight and successfully attack the dinosaur.")
				dinoHP -= playerWeapon
				return dinoHP, playerHidden, False
			else:
				print("You choose to fight the dinosaur but miss with your attack.")
				return dinoHP, playerHidden, False
		
		# If they choose to hide, they need to roll a 4, 5, or 6
		# If they succeed they are hidden when it's the dinosaur's turn
		elif (turn == 'hide'):
			if (roll >= 4):
				print("Fearing for your life, you decide to hide and duck behind a tree.")
				playerHidden = True
				return dinoHP, playerHidden, False
			else:
				print("Fearing for your life, you try to hide but are unable to escape the dinosaur's sight.")
				return dinoHP, playerHidden, False
	
		# If they choose to run, this will end the entire fighting mini-game
		# Possibly cause the player to take damage as a penalty?
	
		elif (turn == 'run'):
			print("You turn on your heels and run.")
			
			return dinoHP, playerHidden, True
	
	def dinoAttack(playerHP, playerHidden, dinoBite):
		if (playerHidden == True):
			print("The dinosaur approaches your hiding place.")
			roll = random.randint(1,6)
			#print(roll)
	
			if (roll <= 3):
				playerHidden = False
				print("You've been found! You're bitten as you scramble from your hiding place.")
				playerHP -= dinoBite
				return playerHP, playerHidden
			else:
				print("It stops near you, but then continues it's search. You remain hidden.")
				return playerHP, playerHidden
		else:
			roll = random.randint(1,6)
			print("The dinosaur lunges at you with it's mouth wide open.")
	
			if (roll <= 3):
				print("You've been bitten!")
				playerHP -= dinoBite
				return playerHP, playerHidden
			else:
				print("Its teeth snap loudly in front of your face. It misses.")
				return playerHP, playerHidden
	
			#SEarch for player
	playerHidden = False
	playerRun = False
	
	# Main code block will be a while statement
	# While both player and dinosaur have more than 0 HP and the player hasn't run away, the turns will loop
	
	while ((dinoHP > 0) and (playerHP > 0)):
	
		#print("dino = " + str(dinoHP) + " player = " + str(playerHP) + " Player hidden = " + str(playerHidden))
	
	
		dinoHP, playerHidden, playerRun = playerAttack(playerWeapon, playerHidden, dinoHP)
		
		if (playerRun == True):
			break

		if (dinoHP <= 0):
			break
	
		#print("dino = " + str(dinoHP) + " player = " + str(playerHP) + " Player hidden = " + str(playerHidden))
	
		playerHP, playerHidden = dinoAttack(playerHP, playerHidden, dinoBite)
	
		if (playerHP <= 0):
			break
	
		print("dino = " + str(dinoHP) + " player = " + str(playerHP))
	
	return playerHP, dinoHP, playerRun




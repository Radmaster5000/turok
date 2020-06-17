import random

################################
# These variables will come from the player and dinosaur classes when it's working properly
################################

playerHP = 6
playerWeapon = 2
playerHidden = False

dinoHP = 10
dinoAttack = 5

#def roll():
#	return random.randint(1,6)


def playerAttack(playerWeapon, playerHidden, dinoHP):
	turn = input('> ')

	roll = random.randint(1,6)
	print(roll)

	# Series of if statements based on player's input
	
	# If they choose to fight, they need to roll a 1, 2, or 3
	# If they succeed they inflict the amount of damage their weapon carries
	if (turn == 'fight'): 

		if (roll <= 3):
			dinoHP -= playerWeapon
			return dinoHP, playerHidden
		else:
			return dinoHP, playerHidden
	
	# If they choose to hide, they need to roll a 4, 5, or 6
	# If they succeed they are hidden when it's the dinosaur's turn
	elif (turn == 'hide'):
		if (roll >= 4):
			playerHidden = True
			return dinoHP, playerHidden
		else:
			return dinoHP, playerHidden

	# If they choose to run, this will end the entire fighting mini-game
	# Possibly cause the player to take damage as a penalty?

	elif (turn == 'run'):
		return dinoHP, playerHidden

def dinoAttack(playerHP, playerHidden, dinoAttack):
	if (playerHidden == True):
		#SEarch for player


# Main code block will be a while statement
# While both player and dinosaur have more than 0 HP and the player hasn't run away, the turns will loop



print(dinoHP, playerHidden)


dinoHP, playerHidden = playerAttack(playerWeapon, playerHidden, dinoHP)

print(dinoHP, playerHidden)
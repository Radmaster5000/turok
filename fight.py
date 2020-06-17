import random

playerHP = 6
playerWeapon = 2
playerHidden = False

dinoHP = 10
dinoAttack = 5

#def roll():
#	return random.randint(1,6)

def playerAttack(playerWeapon, dinoHP):
	turn = input('> ')

	roll = random.randint(1,6)
	print(roll)

	if (turn == 'fight'): 
		if (roll <= 3):
			dinoHP -= playerWeapon
			return dinoHP, playerHidden
		else:
			return dinoHP, playerHidden
	
	elif (turn == 'hide'):
		if (roll <= 4):
			playerHidden = True
			return dinoHP, playerHidden

	elif (turn == 'run'):
		return





print(dinoHP, playerHidden)

dinoHP, playerHidden = playerAttack(playerWeapon, dinoHP)

print(dinoHP, playerHidden)
class Dinosaur:
	def __init__(self, name, hp, speed, bite, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.bite = bite
		self.appearance = appearance

dino_1 = Dinosaur('Trex', 30, 1, 5, 'T')
dino_2 = Dinosaur('Raptor', 10, 2, 3, 'R')
dino_3 = Dinosaur('Raptor', 10, 2, 3, 'R')

class Player:
	def __init__(self, name, hp, speed, weapon, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.weapon = weapon
		self.appearance = appearance

player_1 = Player('Tank', 15, 1, 2, '1')
player_2 = Player('Tracker', 50, 2, 10, '2')



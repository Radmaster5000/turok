class Dinosaur:
	def __init__(self, name, hp, speed, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.appearance = appearance

dino_1 = Dinosaur('Trex', 10, 1, 'T')
dino_2 = Dinosaur('Raptor', 5, 2, 'R')
dino_3 = Dinosaur('Raptor', 5, 2, 'R')

class Player:
	def __init__(self, name, hp, speed, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.appearance = appearance

player_1 = Player('Tank', 5, 1, '1')
player_2 = Player('Tracker', 2, 2, '2')



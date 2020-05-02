class Dinosaur:
	def __init__(self, name, hp, speed, appearance):
		self.name = name
		self.hp = hp
		self.speed = speed
		self.appearance = appearance

tRex = Dinosaur('Trex', 10, 5, 'T')
raptor = Dinosaur('Raptor', 5, 10, 'R')

dino_1 = tRex
dino_2 = raptor
dino_3 = raptor


print('dino_2 hp = ' + str(dino_2.hp))
print('dino_3 hp = ' + str(dino_3.hp))
print('dino_2 hp after attack = ' + str(dino_2.hp-5))
print('dino_3 hp = ' + str(dino_3.hp))


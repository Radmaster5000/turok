

n = input("please enter a number: ")

#create a (roughly) middle value to use when placing the player
mid = int(n)/2
mid = int(mid)

def build_world (n):
	world = []


	for i in range(0, int(n)):
		#create n number of rows
		world.append({})
		for j in range(0, int(n)):	
			world[i].update({j:'empty'})


	return world

#this function is currently working at identifying the column but needs to identify the row as well
def getKeysByValue(dictOfElements, valueToFind, n):
	listOfKeys = list()
	for i in range(0, int(n)):
		listOfItems = dictOfElements[i].items()
		print(listOfItems)
		for item in listOfItems:     #each item is a (key, value) tuple
			if item[1] == valueToFind:
				listOfKeys.append(item[0])
				print("*****")
				print(i)
				print(listOfItems)
				print("*****")
	return listOfKeys



#create the world and save it in the madeWorld variable
madeWorld = build_world(n)

#print each row on a new line
for line in range(0, int(n)):
	print(madeWorld[line])

#place player in the middle of the world (best as possible)
madeWorld[mid][0] = 'player'
print()
print()

for line in range(0, int(n)):
	print(madeWorld[line])

print()
print()

listOfKeys = getKeysByValue(madeWorld, 'player', n)
print("Keys with value equal to player")
for key in listOfKeys:
	print(key)
#print new layout with player in the middle of the world
#for line in range(0, int(n)):
#	print(madeWorld[line])
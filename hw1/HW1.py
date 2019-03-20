def Setup():
	x, minx, maxn = 0, -1, -1 
	numOfZombies = int(input('Enter the number of Zombies: ' ))
	lengthOfBridge = int(input('Enter length of the bridge: '))
	posOfZombies = [None] * int(numOfZombies)
	positionOfZombies = input('Place the initial position of each individual zombie:')
	for i in positionOfZombies.split(' '):
		posOfZombies[x] = i
		x+=1
	#TODO: catch exception
	for p in posOfZombies:
		if p == None:
			print("Something is amiss! ")
			break
		elif int(p) <= 0 or int(p) > lengthOfBridge:
			print("Wrong position was inputted...The val should be in the range of (1, lengthOfBridge)")
			return 1 

	for z in range(numOfZombies):
		# print('max:' ,maxn)
		# print('min:' , minx)
		maxn = max(maxn, max(lengthOfBridge-int(posOfZombies[z])+1, int(posOfZombies[z])))
		minx = max(minx, min(lengthOfBridge-int(posOfZombies[z]), int(posOfZombies[z])))
	print('The earliest time taken is : ', minx)
	print('The latest time taken is : ', maxn)

# def Setup():
# 	pickDirection = random.randint(1, 100)
# 	if pickDirection >= 50:
# 		pickDirection = 
# 		timeTaken = lengthOfBridge 
# 	else:

# class Initialisation(self):
# 	def __init__( self, \
# 					numOfZombies,\
# 					lengthOfBridge, \
# 					positionOfZombies)
# 	self.numOfZombies =
# 	self.lengthOfBridge = 
# 	self.positionOfZombies = 
# 	both of the zombies meet at the same step from different steps, it will take one sec and another sec to bounce off
#	eg.  #####################   1s   ######################   1s   #####################
#		 #   # 1 #   # 2 #   #  --->  #   #   # 12 #   #   #  --->  #   # 1 #   # 2 #   #
#		 #####################	      ######################	    #####################
# 	if both of the zombies are adjacent to each other, it will only take one sec and change direction instantly.


if __name__ == '__main__':
	Setup()

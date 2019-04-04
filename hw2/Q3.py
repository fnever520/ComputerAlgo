def main():
	numApp = [None] *21
	numDis = [None] *21

	numApp[1] = numApp[2] = 0
	numApp[3] = 1

	numDis[0], numDis[1], numDis[2], numDis[3] = 1 ,2 , 4, 7

	for day in range(3,20):
		numApp[day+1] = 2*numApp[day] + numDis[day-3]
		numDis[day+1] = 2**(day+1) - numApp[day+1]

	perc = 1 - numApp[20]/2**20
	print("Probability : {}".format(perc))

if __name__ == '__main__':
	main()
import time
from bitarray import bitarray

def main():
	start = time.clock()
	result = 0 
	n = 99999
	x = int(input("Please enter a number: "))
	if ( (x%2 and x%5)!= 0):
		for c in range(0,n):
			y = 1*10**c
			result += y
			if (result%x == 0):
				break
		output = bitarray(str(result))
		print("Output : ", output.count(1))
		print("Time taken is {} sec".format(time.clock()-start))

'''
	array = [None] * n
	array[0] = 0b1
	array[1] = 0b11
	x = int(input("Please enter a number: "))
	if ( x%2 != 0 ):
		for c in range(2,n):
			array[c] = array[c-1] << 1 | 0b1
			result = array[c]
			result = 
			if (result%x == 0):
				break
		output = bin(result)
		print(result)
		print("the decimal is ", output.count('1'))
		print("time taken is ", time.time()-start)

'''
if __name__ == '__main__':
	main()
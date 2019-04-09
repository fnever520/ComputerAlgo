import numpy as np
import time
import math
from numpy.linalg import matrix_power

def matrixMul(a, power):
	if (power<=1):
		return a
	else:
		return np.matmul(matrixMul(a,power-1), a)

def Q4():
	num = input("Please enter the number of power for [4+13**1/2]: ")

	X = np.array([[4,13],[1,4]])
	Y = np.array([1,0])
	# Z = np.matmul(matrix_power(X,int(num)),Y)
	Z = np.matmul(matrixMul(X,int(num)),Y)
	val = math.pow(13,1/2)
	print(val)
	result = Z[0] + Z[1]*(val)
	result %= 100000
	return result

startTime = time.time()
# print("%-14s:%d" % (Q4()))
print("%-14s:%d" % ("Result",Q4()))
print("%-14s:%.4f seconds" % ("Elapsed time",time.time() - startTime))






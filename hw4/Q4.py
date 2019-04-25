import numpy as np
import time

# X = [[1,3,3],[4,5,6],[7,8,9]]

# for x in range(3):
#     for y in range(3):
#         print(X[x][y])

def matrixMul(a, power):
    if (power==0):
        return 1
    elif (power == 2):
        return (np.dot(a,a)) % 32767
    elif (power%2 == 0):
        power /= 2
        return matrixMul(matrixMul(a,power), 2)
    else:
        power //= 2
        return np.dot(a,(matrixMul(matrixMul(a, power),2)))

resultant_matrix = 0

n = int(input("n="))
k = int(input("k="))
'''
input as
1 2 3 \return
4 5 6 \return
7 8 9
'''
array = [[int(j) for j in input("X%d | "%i).split(" ")] for i in range(n)]

# array = []
# for i in range(n):
#     row_list= []
#     for j in range(n):
#         row_list.append(int(input("X:")))
#     array.append(row_list)
print("Input array: ", array)

startTime = time.time()
for p in range(1,k+1):
    resultant_matrix += matrixMul(array, p)

print("\nR:\n", resultant_matrix)
print("Elapsed time: %.4f seconds" %(time.time()-startTime))
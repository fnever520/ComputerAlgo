import numpy as np
import time
from itertools import starmap
from operator import mul

def matrixMul(a, power):
    if (power==0):
        return 1
    elif (power == 2):
        return (np.dot(a,a))%100000
    elif not (power%2):
        power /= 2
        ccc = matrixMul(matrixMul(a,power), 2)
        print("ccc", ccc)
        return ccc
    else:
        power //= 2
        cc= np.dot(a,(matrixMul(matrixMul(a, power),2)))
        print(cc)
        return cc

def solver(m1, m2):
    res = [[0 for x in range(2)] for y in range(2)]
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):

                res[i][j] += (m2[i][k] * m2[k][j]) % 100000
    print("halo",res)
    return res

def identityMatrix():
    return np.array([1,1])

# def matrixMul(a, power):
#     result = identityMatrix()
#     while (power != 0):
#         if (power%2 != 0):
#             result = solver(result, a)
       
#         power//=2
#         a = solver(a,a)
#     print(a)
#     return result



'''
def matrixMul(a, power):
        temp = a
        for loop in range(power-1): 
            # _, temp = np.divmod(temp, 100000)
            print(temp)
            print("a",*a)
            s= [[sum(starmap(mul, zip(row, col))) for col in zip(a)] for row in temp]
            print("sss",s)
            temp = s
            return s
'''
def Q4():
    num = input("Please enter the number of power for [4+13**1/2]: ")

    X = np.array([[4,13],[1,4]])
    Y = np.array([[4],[1]])

    Z = np.dot(matrixMul(X,int(num)-1),Y)
    print(Z)
    result = (2*Z[0][0] - 1) %100000

    return result

startTime = time.time()
print("%-14s:%d" % ("Result",Q4()))
print("%-14s:%.4f seconds" % ("Elapsed time",time.time() - startTime))






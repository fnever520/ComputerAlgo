import time
import numpy as np

def zeroMatrix(nPick):
    matrix = []
    ## creating a list of array in a loop
    zeros_array = [0 for x in range(nPick*nPick)]
    rows, cols = nPick, nPick
    for i in range(rows):
        rowList = []
        for j in range(cols):
            rowList.append(zeros_array[nPick*i + j])
        matrix.append(rowList)
    return matrix

def marbleMatrix(nPick):
    matrix = zeroMatrix(nPick)

    for i in range(nPick):
        for j in range(nPick):
            if i == 0:
                matrix[i][j] = 1
            elif (i-1) == j:
                matrix[i][j] = 1
    return (matrix) 

def solver(matrixA, matrixB):
    global numPick
    resultantMatrix = [[0 for x in range(numPick)] for y in range(numPick)]

    for i in range(len(matrixB)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                resultantMatrix[i][j] += (matrixA[i][k] * matrixB[k][j]) % 65535
    print(resultantMatrix)
    return resultantMatrix

def identityMatrix():
    global numPick
    return np.identity(numPick)

def matrixMul(a, power):
    if (power==0):
        return 1
    elif (power == 2):
        return (np.dot(a,a))%65535
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

# def matrixMul(a, power):
#     if (power<=1):
#         return a
#     else:
#         b = np.matmul(matrixMul(a,power-1), a)
#         return b

def numMarble(marble, numPick):
    # print(marbleMatrix(numPick)[0][0])
    # rows, cols = numPick, numPick
    # temp_m = []
    # for x in range(rows):
    #     rowList = []
    #     for y in range(cols):
    #         temp = marbleMatrix(numPick)[x][y] * marbleMatrix(numPick)[y][x]
    #         temp += temp
    #         rowList.append(temp[numPick*x + y])
            
    #         print("..",rowList)
    #     temp_m.append(rowList)
    # return temp_m

    # return numMarble(marble-1,numPick)
    return matrixMul(marbleMatrix(numPick), marble)

startTime = time.time()

marble = int(input("Please enter number of marbles: "))
numPick = int(input("Enter the number of pick per time: "))


print("The number of ways are ",numMarble(marble,numPick)[0][0])
print("Elapsed time : %.4f seconds" %(time.time()- startTime))


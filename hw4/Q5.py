import numpy as np
import time

#create an adjacent matrix for the respective graph
graph1 = [[0,1,1,0,0], \
          [0,0,1,0,0], \
          [0,0,0,1,0], \
          [1,0,0,0,1], \
          [1,1,0,0,0]]

graph2 = [[0,1,1,0],\
          [0,0,1,0],\
          [0,0,0,1],\
          [1,0,0,0]]

graph = graph2
k = 0

def numOutputPath(graphLength_k):
    sum = 0 
    for x in range(len(graphLength_k)):
        for y in range(len(graphLength_k)):
            sum += graphLength_k[x][y]
    return sum

def matrixMul(a, power):
    if (power==0):
        return 1
    elif (power == 2):
        return (np.dot(a,a))
    elif (power%2 == 0):
        power /= 2
        return matrixMul(matrixMul(a,power), 2)
    else:
        power //= 2
        return np.dot(a,(matrixMul(matrixMul(a, power),2)))

startTime = time.time()

if (k == 0):
    graph = np.array(graph)
    graphLength_k = graph.tolist()
else:
    resultant_matrix = matrixMul(graph,k)
    graphLength_k = resultant_matrix.tolist()
    # print(graphLength_k)

print("Output: ", numOutputPath(graphLength_k))
print("Elapsed time: %.4f seconds" %(time.time()-startTime))
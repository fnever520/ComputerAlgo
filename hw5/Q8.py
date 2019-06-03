import sys

'''
Input1:
3
0 981 600 
981 0 170 
600 170 0
1
0 1

Input2:
10
0 4 1 4 0 0 0 0 0 0
4 0 5 0 9 9 0 7 0 0
1 5 0 3 0 0 0 9 0 0
4 0 3 0 0 0 0 10 0 18
0 9 0 0 0 2 4 0 6 0
0 9 0 0 2 0 28 0 0
0 0 0 0 4 2 0 9 3 9
0 7 9 10 0 8 9 0 0 8
0 0 0 0 6 0 3 0 0 9
0 0 0 18 0 0 9 8 9 0
2
0 1
0 2

'''
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] \
                      for row in range(vertices)]

    def printMST(self, parent, p, gOutput):
        result = [[0 for y in range(self.V)] \
                for x in range(self.V)]

        for i in range(1, self.V):
            result[parent[i]][i] = int(self.graph[i][parent[i]])
            result[i][parent[i]] = int(self.graph[i][parent[i]])

        for i in range(p):
            result[int(gOutput[i][0])][int(gOutput[i][1])] = int(gOutput[i][2])
            result[int(gOutput[i][1])][int(gOutput[i][0])] = int(gOutput[i][2])

        weight = 0
        for x in range(3):
            for y in range(3):
                weight += result[x][y]
        weight/=2

        for i in range(p):
            weight -=int(gOutput[i][2])
        
        print("Output: \n", weight)
        print(result)
        return result

    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self,p,gOutput):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if int(self.graph[u][v]) > 0 and mstSet[v] == False and key[v] > int(self.graph[u][v]):
                    key[v] = int(self.graph[u][v])
                    parent[v] = u

        self.printMST(parent,p,gOutput)

if __name__ == '__main__':

    minWeight = sys.maxsize
    
    numInput = int(input())
    g = Graph(numInput)
    graph = [[None for i in range(numInput)] for j in range(numInput)]
    for i in range(numInput):
        graph[i] = (input().split())
    # print(graph)

    for i in range(numInput):
        for j in range(numInput):
            if int(graph[i][j])< minWeight and int(graph[i][j])>0:
                minWeight = int(graph[i][j])
                print('min', minWeight)

    # print(minWeight)
    numConstLine = int(input())
    ConsGraph = [[None for col in range(2)] for row in range(numConstLine)]

    inputConsGraph = input().split()
    for i in range(numConstLine):
        ConsGraph[i] = inputConsGraph

    for i in range(numConstLine):
        ConsGraph[i].append(graph[int(ConsGraph[i][0])][int(ConsGraph[i][1])])
        graph[int(ConsGraph[i][0])][int(ConsGraph[i][1])] = minWeight
        graph[int(ConsGraph[i][1])][int(ConsGraph[i][0])] = minWeight
        
    print(graph)
    g.graph = graph
    g.primMST(numConstLine,ConsGraph)

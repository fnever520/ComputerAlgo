import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        #print("Vertex tDistance from Source")
        # need to return with at least 100l
        print("output: ",dist[self.V-1]+1000*100)

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
                print("v%d %d" %(min_index,min))
        return min_index

        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):

                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    #relaxation
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

    # Driver program

# dist = int(input())
# numStation = int(input())
g = Graph(9)
fuel = []    
fuel.append([100,1200])
fuel.append([150,1400])
fuel.append([200,1300])
fuel.append([250,1000])
fuel.append([300,1100])
fuel.append([350,1400])
fuel.append([400,1300])
fuel.append([450,1000])
fuel.append([500,1399])


g.graph = [[0, 50*1200, 100*1200, 150*1200, 200*1200, 0,        0,        0,        0.      ], \
           [0, 0,       50*1400,  100*1400, 150*1400, 200*1400, 0,        0,        0.      ], \
           [0, 0,       0,        50*1300,  100*1300, 150*1300, 200*1300, 0,        0.      ], \
           [0, 0,       0,        0,        50*1000,  100*1000, 150*1000, 200*1000, 0.      ], \
           [0, 0,       0,        0,        0,        50*1100,  100*1100, 150*1100, 200*1100], \
           [0, 0,       0,        0,        0,        0,        50*1400,  100*1400, 150*1400], \
           [0, 0,       0,        0,        0,        0,        0,        50*1300,  100*1300], \
           [0, 0,       0,        0,        0,        0,        0,        0,        50*1000 ], \
           [0, 0,       0,        0,        0,        0,        0,        0,        0.      ]]
# print(g.graph)
g.dijkstra(0)

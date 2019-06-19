# Python program for implementation of Ford Fulkerson algorithm 

from collections import defaultdict 
INF = 99999   
#This class represents a directed graph using adjacency matrix representation 
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 
   
    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 

        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 

            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
  

graph = [[260,   60,   140,   350,   500,   0,   0,   0,   0,   0,0 ,0], \
         [INF, 0,   0,   0, 0, 0,   INF,   0,   0,   0,0 ,0], \
         [INF, 0, 0,   0,   0,   0,   INF,   INF,   INF,   0,0 , 0], \
         [INF, 0,   0,   0,   0,   0,   0, 0,   INF,   INF, 0 , 0], \
         [INF, 0,   0,   0,   0,   0, 0,   0,   0,   INF, 0 , 0], \
         [INF,   0,   0, 0,   0, 0,   0, 0,   0,   INF,INF , 0], \
         [0,   INF,   INF,   0, 0,   0, 0,   0,   0,   0, 0 ,250], \
         [0,   0,   INF,   0, 0,   0, 0,   0,   0,   0,0 , 100], \
         [0,   0,   INF,   INF, 0,   0, 0,   0,   0,   0,0 , 150], \
         [0,   0,   0,   INF, INF,   INF, 0,   0,   0,   0,0 , 300], \
         [0,   0,   0,   0, 0,   INF, 0,   0,   0,   0,0 , 100], \
         [0,   0,   0,   0,   0, 0,   250, 100,   150,   300, 100 ,0]] \
  
g = Graph(graph) 
source = 0
sink = 11

winningMatch = g.FordFulkerson(source, sink)
print("Maxflow : %d" %(winningMatch))

# currentWins = 0 
# for i in range(len(graph)):
#     for j in range(len(graph)):
#         if i==0:
#             currentWins += graph[0][j]

# print("Minimum wins : %d"%(currentWins - winningMatch))

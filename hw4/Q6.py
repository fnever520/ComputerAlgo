from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
          
   
    # function to add an edge to graph 
    def addEdge(self,menIndex,womenIndex, intimacy): 
        womenIndex = womenIndex+numMen
        self.graph.append([menIndex,womenIndex,-intimacy]) 
        #print(self.graph)
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        #Todo
        for node in range(self.V + numMen): 
            parent.append(node) 
            rank.append(0) 


        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            menIndex, womenIndex, intimacy =  self.graph[i] 

            i += 1

            x = self.find(parent, menIndex) 
            y = self.find(parent ,womenIndex)
            
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([menIndex,womenIndex,intimacy]) 
                self.union(parent, rank, x, y)  

            # prevent it goes out of range
            if (self.V == i ):
                return result          

def output(result):
    #todo
    print("Following are the edges in the constructed MST")
    w = 0
    for menIndex,womenIndex,intimacy  in result: 
        print ("(%d -- %d) == %d" % (menIndex,womenIndex,intimacy)) 
        w += intimacy
    print("\nThe minimum cost to hire : $%d" %(10000*(numMen+numWomen) + w) )


numMen = 5
numWomen = 5

# first input

g1 = Graph(8) 
g1.addEdge(0, 0, 6590) 
g1.addEdge(0, 1, 3073) 
g1.addEdge(1, 3, 4573) 
g1.addEdge(1, 3, 2149) 
g1.addEdge(2,2,789) 
g1.addEdge(3,3,975) 
g1.addEdge(4,2,204) 
g1.addEdge(4,3,631) 
# result = g1.KruskalMST() 

# second input
g2 = Graph(10)
g2.addEdge(0,4,4372)
g2.addEdge(2,0,16)
g2.addEdge(2,0,146)
g2.addEdge(2,4,326)
g2.addEdge(2,4,2133)
g2.addEdge(2,4,9220)
g2.addEdge(3,1,8364)
g2.addEdge(3,2,6336)
g2.addEdge(3,4,8833)
g2.addEdge(4,1,2339)
result = g2.KruskalMST()

output(result)
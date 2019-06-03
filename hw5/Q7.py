import heapq as hq
from collections import defaultdict

'''
input:
9 
14 
1 2 4
1 8 8
2 3 8 
2 8 11 
3 4 7 
3 6 4 
3 9 2 
4 5 9 
4 6 14 
5 6 10 
6 7 2 
7 8 1  
7 9 6
8 9 7
'''

# class DisjointSet:
#     def __init__(self, init_arr):
#         self._disjoint_set = []
#         if init_arr:
#             for item in list(set(init_arr)):
#                 self._disjoint_set.append([item])

#     def _find_index(self, elem):
#         for item in self._disjoint_set:
#             if elem in item:
#                 return self._disjoint_set.index(item)
#         return None

#     def find(self, elem):
#         for item in self._disjoint_set:
#             if elem in item:
#                 return self._disjoint_set[self._disjoint_set.index(item)]

#     def union(self, elem1, elem2):
#         index_elem1 = self._find_index(elem1)
#         index_elem2 = self._find_index(elem2)
#         if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
#             self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
#             del self._disjoint_set[index_elem1]
#         return self._disjoint_set

#     def get(self):
#         return self._disjoint_set


def prim(edges):

    li = defaultdict(list)
    for v1,v2,weight in tree:
        li[v1].append((weight, v1,v2))
        li[v2].append((weight, v2,v1))

    mst = []
    used = set([1])
    cache = li[1][:]
    # print(cache)
    hq.heapify(cache)

    while (cache):
        weight, v1, v2 = hq.heappop(cache)
        if v2 not in used:
            used.add(v2)
            mst.append((v1,v2,weight))
            for e in li[v2]:
                if e[2] not in used:
                    hq.heappush(cache, e)
    return mst


if __name__ == '__main__':
    numVertices = int(input())
    numEdges = int(input())
    tree = [None]*numEdges
   
    for i in range(numEdges):
        tree[i] = input().split()
        tree[i][0] = int(tree[i][0])
        tree[i][1] = int(tree[i][1])
        tree[i][2] = -int(tree[i][2])

    print(tree)
    mst = prim(tree)
    sumWeight = 0 
    for i in range(numVertices-1):
        sumWeight += -mst[i][2]

    print("Output: ", sumWeight)


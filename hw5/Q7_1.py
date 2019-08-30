from heapq import *

class DisjointSet:
    def __init__(self, init_arr):
        self._disjoint_set = []
        if init_arr:
            for item in list(set(init_arr)):
                self._disjoint_set.append([item])

    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None

    def find(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set[self._disjoint_set.index(item)]

    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]
        return self._disjoint_set

    def get(self):
        return self._disjoint_set

# using the maxheapify/heapsort method

def swap(a,i, j):
    ab = a[int(i)]
    a[int(i)] = a[int(j)]
    a[int(j)] = ab

def is_heap():
    n = 0
    m = 0 
    while True:
        for i in [0,1]:
            m += 1
            if m >= len(a):
                return True
            if a[m] > a[n]:
                return False
        n += 1

def sift_down(a, n, max):
    while True:
        biggest= n
        c1 = int(2*n +1)
        c2 = int(c1 +1)
        for c in (c1, c2):
            if c < max and a[c] >a[int(biggest)]:
                biggest = c
        if biggest ==n :
            return
        swap(a, n, biggest)
        n = biggest

def heapify(a):
    i = len(a)/2 -1 
    max = len(a)
    while i>=0:
        sift_down(a, i, max)
        i -=1

def heapsort(a):
    heapify(a)
    j = len(a)-1
    while j > 0:
        swap(a,0,j)
        sift_down(a,0,j)
        j -=1


a = [4,8,8,11,7,4,2,9,14,10,2,1,6,7]
heapsort(a)
print(a)

node_num = int(input())
edge_num = int(input())
a=[""]*edge_num

for i in range(len(a)):
    a[i] = input()
    a[i] = a[i].split()
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
    a[i][2] = int(a[i][2])
    print(a)

w = [""]*edge_num
ow=[""]*edge_num
for i in range(len(w)):
    w[i] = a[i][2]
heapsort(w)

for i in range(len(w)):
    ow[i] = a[i][2]

print("w", w)
print("ow", ow)

if __name__=='__main__':
    Output = 0 
    li =[""]*node_num
    print(li)
    symbol=[0]*edge_num
    print(symbol)

    for i in range(node_num):
        li[i] = i+1
    test_set_node = DisjointSet(li)
    print("test_set_node", test_set_node)

    print('w: ', w)
    print('ow: ', ow)

    for j in range(edge_num):
        print('max_w', w[edge_num-j-1])
        if ow[i] == w[edge_num-j-1]:
            index = i
            print("a[index][0]: ", a[index][0])
            print("a[index][1]: ", a[index][1])
            if test_set_node.find(a[index][0] != test_set_node.find(a[index][1]) and symbol[i]==0):
                symbol[i]=1
                print("ow[i]", ow[i])
                print(symbol)
                Output += ow[i]

                print("test_set_node", test_set_node.union(a[i][0],a[i][1]))
                print(test_set_node.get())
                break
        else:
            continue
    print("Output", Output)

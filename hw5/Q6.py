class DisjointSetForest:
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
        return None

    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if (index_elem1 != index_elem2) and (index_elem1 is not None) and (index_elem2 is not None):
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]

        return self._disjoint_set

    def get(self):
        return self._disjoint_set

if __name__ == '__main__':

    numInput = int(input())
    user_input = [None]*numInput
    for i in range(numInput):
        user_input[i] = input().split()
        # print(user_input[i])

    for i in range(numInput):
        if user_input[i][0] =="!":
            tree_a = user_input[i][1]
            tree_b = user_input[i][2]
            cache = i
            break

    group = [tree_a, tree_b]
    # print(group)
    disjSet = DisjointSetForest(group)
    disjSet.get()

    for i in range(numInput):
        if (user_input[i][0] == "?"):
            if i < cache:
                print("Not Yet")
            elif disjSet.find(user_input[i][1]) in [disjSet.find(user_input[i][2])]:
                # print(disjSet.find(user_input[i][1]))
                # print(disjSet.find(user_input[i][2]))
                print("Same")
            elif (disjSet.find(user_input[i][1]) == disjSet.find(tree_a)) and (disjSet.find(user_input[i][2]) == disjSet.find(tree_b)):
                print("Different")
            elif (disjSet.find(user_input[i][2]) == disjSet.find(tree_a)) and (disjSet.find(user_input[i][1]) == disjSet.find(tree_b)):
                print("Different")
            else:
                print("Not Yet")

        elif user_input[i][0] == "!":
            if not (user_input[i][1] in [tree_a, tree_b]):
                group.append(user_input[i][1])

            elif not (user_input[i][2] in [tree_a, tree_b]):
                group.append(user_input[i][2])

            disjSet = DisjointSetForest(group)
            disjSet.get()

            if disjSet.find(tree_a) == disjSet.find(user_input[i][1]):
                disjSet.union(tree_b, user_input[i][2])

            elif disjSet.find(tree_a) == disjSet.find(user_input[i][2]):
                disjSet.union(tree_b, user_input[i][1])

            elif disjSet.find(tree_b) == disjSet.find(user_input[i][1]):
                disjSet.union(tree_a, user_input[i][2])

            elif disjSet.find(tree_b) == disjSet.find(user_input[i][2]):
                disjSet.union(tree_a, user_input[i][1])
    

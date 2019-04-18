checkerboard = [[2, 5, 1, 6, 1, 4, 1], \
                [6, 1, 1, 2, 2, 9, 3], \
                [7, 2, 3, 2, 1, 3, 1], \
                [1, 1, 3, 1, 7, 1, 2], \
                [4, 1, 2, 3, 4, 1, 2], \
                [3, 3, 1, 2, 3, 4, 1], \
                [1, 5, 2, 9, 4, 7, 5]]

checkerMap = []
start = [0,0]
checkerMap.append(start)
maxIndexCheckerboard = len(checkerboard) - 1

for num in range(len(checkerboard)):
    for x in range(len(checkerMap)):
        pair = checkerMap[x]

        i = pair[0]
        j = pair[1]

        if ((checkerboard[i][j]+i)< len(checkerboard)):
            checkerMap.append([checkerboard[i][j]+i,j])

        if ((checkerboard[i][j]+j) < len(checkerboard)):
            checkerMap.append([i,checkerboard[i][j]+j])
        # print(checkerMap)

lastIndex = checkerMap.pop()
if (lastIndex == [maxIndexCheckerboard for i in range(2)]):
    result = "true"
else:
    result = "false"

print("Result: ", result)

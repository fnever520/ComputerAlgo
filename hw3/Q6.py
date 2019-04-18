checkerboard = [[2, 5, 1, 6, 1], \
                [6, 1, 1, 2, 2], \
                [7, 2, 3, 2, 1], \
                [1, 1, 3, 1, 7], \
                [4, 1, 2, 3, 4]] 
       
checkerMap = [[None for i in range(len(checkerboard))] for j in range(len(checkerboard))]

for i in range(len(checkerboard)):
    for j in range(len(checkerboard)):
        if ((i == 0) and (j == 0)):
            checkerMap[i][j] = checkerboard[i][j]
        elif (i == 0 ):
            checkerMap[i][j] = checkerboard[i][j] + checkerMap[i][j-1]
        elif (j == 0):
            checkerMap[i][j] = checkerboard[i][j] + checkerMap[i-1][j]
        else:
            prevTop = checkerMap[i-1][j]
            prevLeft = checkerMap[i][j-1]
            prevDiagonal = checkerMap[i-1][j-1]

            if (prevTop == prevLeft):
                print("fail")
                print(i)
                print(j)
            down = prevTop + checkerboard[i][j]
            right = prevLeft + checkerboard[i][j]
            diagonal = prevDiagonal + checkerboard[i][j]
            checkerMap[i][j] = max(max(down, right), diagonal)

print(checkerMap)

array = []
x = len(checkerboard) -1
y = len(checkerboard) -1

while ((x != 0) or (y != 0)):
    array.append([x,y])

    up = 0
    left = 0
    diagonal = 0 

    if (x != 0):
        up = checkerMap[x-1][y]
    if (y != 0):
        left = checkerMap[x][y-1]
    if ((x != 0) and (y != 0)):
        diagonal = checkerMap[x-1][y-1]

    maximum = max(max(up, left), diagonal)

    if (maximum == up):
        x -= 1
    elif (maximum == left):
        y -= 1
    else:
        x -= 1
        y -= 1

array.append([0,0])
while(array):
    print(array.pop())
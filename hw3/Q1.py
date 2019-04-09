import time

def countWaysUtil(numMarble, pick): 
    start = time.clock()
    ways = [0 for x in range(numMarble)] 
    ways[0],ways[1] = 1,1

    for i in range(2,numMarble): 
        j = 1
        while j<=pick and j<=i: 
            ways[i] = ways[i] + ways[i-j] 
            # ways[i] = result
            j = j + 1
    print("Time taken is {}s".format(time.clock()-start))
    return ways[numMarble-1] 

def countWays(s, pick): 
    return countWaysUtil(s+1, pick) 
      
# Driver Program 
s,m = 2000000,3
count = countWays(s,m)
print("Nmber of ways =",count)
remainder = count % 65535
print("remainder", remainder)

'''
    4 ->
    1 1 1 1
    1 1 2
    1 2 1
    2 1 1
    2 2 
    1 3
    3 1

    5->
    1 1 1 1 1
    1 1 1 2
    1 1 2 1
    1 2 1 1
    2 1 1 1
    2 1 2
    2 2 1
    1 2 2
    1 1 3
    1 3 1
    3 1 1
    4 1
    1 4
    '''

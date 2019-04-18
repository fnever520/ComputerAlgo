import time
from sys import maxsize

def maxSubArraySum(a,size): 
  
    currentMax = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
        max_ending_here += a[i] 
  
        if currentMax < max_ending_here: 
            currentMax = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
        
    # if the values exceeds 16 bits 
    if abs(currentMax) > (2**15-1):
        currentMax %= 65535
    print("({},{}):{} ".format(start+1, end+1, currentMax))
  
x=0
numInput = int(input("Please input the number of input: "))
data = input("Please enter your input data: ")
a = [None] * numInput
for i in data.split(" "):
    # a.append(int(i))
    a[x] = int(i)
    x+=1

startTime = time.time()
maxSubArraySum(a,len(a))
print("Total elapsed time: %.4f seconds" %(time.time()- startTime))

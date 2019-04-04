# Binary search algo 
def binary_search(array,low,high,x): 
  
    if high >= low: 
        mid = low+(high-low)/2
  
        if array[mid] == x: 
            return mid 
  
        if array[mid] > x: 
            return binary_search(array,low,mid-1,x) 
  
        return binary_search(array,mid+1,high,x) 
  
    return -1
  
# function takes an infinite size array and a key to be 
# searched and returns its position if found else -1. 
# We don't know size of a[] and we can assume size to be 
# infinite in this function. 
# NOTE THAT THIS FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE 
# THEREFORE, THERE IS NO INDEX OUT OF BOUND CHECKING 
def find_position(a, key): 
  
    l, h, val = 0, 1, array[0] 
  
    # Find h to do binary search 
    while val < key: 
        l = h            #store previous high 
        h = 2*h          #double high index 
        val = array[h]       #update new val 
  
    # at this point we have updated low and high indices, 
    # thus use binary search between them 
    return binary_search(a, l, h, key) 
  
array = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] 

target = 9
ans = find_position(array,target) 
if ans == -1: 
    print "Not found"
else: 
    print "Element found at index",ans, "; target : %d" %target
  

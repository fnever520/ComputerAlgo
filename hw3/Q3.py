import math

def main():
    candy = 10
    odd = [None for x in range(20)]
    even = [None for x in range(20)]

    even[2] =2
    possibility = 0
    print(even)
    print(odd)
    for x in range(2,candy,2):
        even = getEvenSets(even, x)
        if (candy -1 ==0):
            possibility += even
        else:
            # odd = getPowerFromSets(odd, candy - x)
            odd = 1
            print(type(even))
            print(type(odd))
            possibility += even * odd * ((candy -x)*x +1)
    print(even)
    print(odd)
    odd = getPowerFromSets(odd, candy)
    possibility+=odd

def getPowerFromSets(odd, power):
    if (power ==0):
        return 0
    if(odd[power] ==0):
        result = math.pow(2, power)
    else:
        result = odd[power]

    return result

def getEvenSets(even, index):
    if (even[index]==0) :
        if ((index/2)%2 ==0):
            even = math.pow(2, index/2)*2
            even[index] = even
        else:
            even = even[index-2] *2
            even[index] = even
    else:
        even = even[index]

    return even

print("Result :", main())
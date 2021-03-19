'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
'''
#date 25.04.2020

def arramgeCoins(num):
    rest = num
    resultCol = 0

    for i in range(num+1):
        if rest >= i:
            rest -= i
        else:
            resultCol = i -1
            break

    return resultCol

num = int(input('please input a integer :'))
print(arramgeCoins(num))



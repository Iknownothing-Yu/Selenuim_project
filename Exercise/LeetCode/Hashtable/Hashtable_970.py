'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once
'''
# date 17.04.2020
import math

def powerInt(x, y, bound):
    result_dic = {}
    for i in range(10):
        for j in range(10):
            sum = pow(x, i) + pow(y, j)
            if sum <= bound and sum not in result_dic:
                result_dic[sum] = True
    return sorted(result_dic.keys())

x = int(input('input3 x :'))
y = int(input('input y :'))
b = int(input('input bound :'))
print(powerInt(x, y, b))


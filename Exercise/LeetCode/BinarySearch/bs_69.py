'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned
'''
# date 19.04.2020

def sqrFunction(num):
    start = 1
    end = num // 2
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 > num:
            end = mid - 1
        elif mid ** 2 < num:
            start = mid + 1
        else: return mid

    return end

num = int(input('input a num :'))
print('%d sqr is :' %(num), sqrFunction(num))





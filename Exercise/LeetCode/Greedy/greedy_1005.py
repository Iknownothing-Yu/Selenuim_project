'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.
'''
# date 22.06.2020
from collections import Counter
def maxSumAfterkNegative(A, k):

    for i in range(k):
        if min(A) != 0:
            temp = -min(A)
            A.remove(min(A))
            A.append(temp)

        else:
            break
    print(A)
    return sum(a for a in A)

A = list(map(int, input('A :').split(',')))
k = int(input('k :'))
print(maxSumAfterkNegative(A, k))
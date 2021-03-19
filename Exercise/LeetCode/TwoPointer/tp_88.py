'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
'''
# date 07.06.2020
def mergeArr(num1, m, num2, n):
    i = m - 1
    j = n - 1
    move = len(num1) - 1

    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[move] = num1[i]
            i -= 1
        else:
            num1[move] = num2[j]
            j -= 1
        move -= 1

    while j >= 0:
        num1[move] = num2[j]
        j -= 1
        move -= 1

    return num1

num1 = list(map(int, input('num1 :').split(',')))
m = int(input('m :'))
num2 = list(map(int, input('num2 :').split(',')))
n = int(input('n :'))
print(mergeArr(num1, m, num2, n))

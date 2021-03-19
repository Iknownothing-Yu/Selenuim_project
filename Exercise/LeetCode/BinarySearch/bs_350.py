'''
Given two arrays, write a function to compute their intersection
include duplicate
'''
# date 23.04.2020
def intersection(arr1, arr2):
    l = []
    arr1 = sorted(arr1)
    start1 = 0
    end1 = len(arr1) - 1

    arr2 = sorted(arr2)
    start2 = 0
    end2 = len(arr2) - 1

    while start1 <= end1 and start2 <= end2:

        if arr1[start1] == arr2[start2]:
            l.append(arr1[start1])
            start1 += 1
            start2 += 1
        elif arr1[start1] > arr2[start2]:  # 如果这里是if，就会出错 index out of range
            start2 += 1
        elif arr1[start1] < arr2[start2]:
            start1 += 1
    return l

arr1 = input('first array :').split(',')
arr2 = input('second array :').split(',')
print(intersection(arr1, arr2))

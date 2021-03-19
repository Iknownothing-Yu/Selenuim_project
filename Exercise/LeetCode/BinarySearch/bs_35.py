'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be
if it were inserted in order.
'''
# date 18.04.2020
'''
线性查找
def searchInsertPosition(arr, target):
    arr_int = list(map(int, arr))
    target = int(target)
    if target < arr_int[0]:
        return 0
    for index, ele in enumerate(arr_int):
        if ele == target or ele > target:
            return index
        if index == (len(arr_int) - 1) and ele < target:
            return len(arr_int)
'''
'''
使用库
from bisect import bisect_left

def searchInsertPosition(arr, target):
    return bisect_left(arr, target)
'''

def searchInsertPosition(arr, target):
    arr = list(map(int, arr))
    target = int(target)
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else: return mid
    print(start, end)
    return start

arr = input('input array :').split(',')
target = input('input target :')
print(searchInsertPosition(arr, target))

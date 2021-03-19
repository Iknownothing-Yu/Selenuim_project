'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to
a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2
'''
# date 20.04.2020
def twoSum(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] > target:
            end -= 1
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            start += 1
            end += 1
            return [start, end]
    return 'no such a pair number'


arr = list(map(int, input('please input num array :').split(',')))
target = int(input('target :'))
print(twoSum(arr, target))

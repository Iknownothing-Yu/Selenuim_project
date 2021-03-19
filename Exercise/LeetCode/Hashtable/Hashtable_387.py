'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''
# date 12.04.2020

import collections

def findFirstUniq(arr):
    arr_list = list(arr)
    arr_dic = collections.Counter(arr)
    for index, ele in enumerate(arr_list):
        if arr_dic[ele] == 1:
            return index
    return -1

arr = input('input array :')
print(findFirstUniq(arr))
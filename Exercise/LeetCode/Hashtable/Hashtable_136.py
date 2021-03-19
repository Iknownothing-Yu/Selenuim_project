'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one
'''
# date 06.04.2020
# defaultdict(type)

from collections import defaultdict
def single_one(arr):
    ele_dict = defaultdict(int)
    for element in arr:
        if element in ele_dict.keys():
            ele_dict[element] -= 1
        else:
            ele_dict[element] += 1
    for key in ele_dict.keys():
        if ele_dict[key] == 1:
            return key

input_arr = input('input an array of int :').split(',')
print(single_one(input_arr))




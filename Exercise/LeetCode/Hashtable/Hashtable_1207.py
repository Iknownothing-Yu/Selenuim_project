'''
Given an array of integers arr
write a function that returns true if and only if the number of occurrences of each value in the array is unique
'''
#date: 04.04.2020
def num_occur(arr):
    ele_occur = {}
    for index, ele in enumerate(arr):
        if ele not in ele_occur.keys():
            ele_occur[ele] = 1
        else:
            ele_occur[ele] += 1

    return ele_occur

def determine_unique(ele_hash):
    li = []
    for key in ele_hash.keys():
        if ele_hash[key] in li:
            return 'false'
        else:
            li.append(ele_hash[key])
    return 'TURE'

input_str = input('input string is :').split(',')
print(determine_unique(num_occur(input_str)))
'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
'''
# date 26.04.2020

def finndElement(numarr, target):
    for index, ele in enumerate(numarr):
        if ele == target:
            return index
    return -1

numarr = input('please input a number array :').split(',')
target = input('target is :')
print(finndElement(numarr, target))
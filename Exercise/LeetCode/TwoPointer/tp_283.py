'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.
'''
# date 01.06.2020
def moveZeros(nums):
    l = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            for j in range(i, l):
                print('j :', j)
                nums[j] = nums[j + 1]
            nums[l] = 0
            l -= 1
    return nums
nums = list(map(int, input('nums :').split(',')))
print(moveZeros(nums))




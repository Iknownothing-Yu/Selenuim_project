'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory
'''
# date 04.06.2020
def removeElement(nums, value):
    '''
    method 1

    i = 0
    while i < len(nums):
        if nums[i] == value:
           nums.remove(nums[i])
        else:
            i += 1

    method 2

    while value in nums:
            nums.remove(value)
        return len(nums)

    method 3
    i = 0
    for j in range(len(nums)):
        if nums[j] != value:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return i
    '''
    # method 4
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == value:
            nums[i] = nums[j]
            j -= 1
        else:
            i += 1
    print(nums)
    print('i :', i, 'j :', j)
    return j + 1

num = list(map(int, input('nums :').split(',')))
value = int(input('value :'))
print(removeElement(num, value))


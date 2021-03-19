'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory
'''
# date 06.06.2020
def removeDuplicate(nums):
    '''
    # method 1
    result = []
        for ele in nums:
            if ele not in result:
                result.append(ele)
        return len(result)
    '''
    # method 2
    length = 1
    if len(nums) == 1:
        return 1
    else:
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                length += 1
        return length

nums = list(map(int, input('num2 :').split(',')))
print(removeDuplicate(nums))
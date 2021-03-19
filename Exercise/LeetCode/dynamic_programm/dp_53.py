'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.
'''
# date 14.06.2020
import sys
def maxSubArr(nums):
    # greedy
    '''
    :param nums: input nums list
    :return: maxSum
     currentSum = 0
    maxSum = -sys.maxsize - 1
    for ele in nums:
        currentSum += ele
        maxSum = max(maxSum, currentSum)
        currentSum = max(0, currentSum)
    '''
    # dymamic
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)

num = list(map(int, input('num list :').split(',')))
print(maxSubArr(num))
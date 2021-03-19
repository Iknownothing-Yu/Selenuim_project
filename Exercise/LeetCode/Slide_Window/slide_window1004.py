'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.
'''
# date 16.08.2020

class Solution():
    def maxContinueOnes(self, nums, k, max_sum):
        current_sum = 0
        j = k
        ms = max_sum
        mark = 0
        ns = 0

        for i in range(len(nums)):
            if nums[i] == 0 and j > 0:
                current_sum += 1
                if j == k - 1:
                    mark = i
                j -= 1
            elif nums[i] == 1:
                current_sum += 1
            else:
                ms = max(ms, current_sum)
                break
        if j > 0 or mark >= len(nums) - 1: # 很重要，是返回值的点
            return ms
        else:
            for index in range(mark - 1, -1, -1):
                if nums[index] == 0:
                    ns = index + 1
                    break
            return self.maxContinueOnes(nums[ns:], k, ms)

ob = Solution()
nums = [0,0,0,1,0,1,0,0]
k = 2
print(ob.maxContinueOnes(nums, k, 0))




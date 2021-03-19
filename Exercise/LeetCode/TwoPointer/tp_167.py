'''
find two numbers such that they add up to a specific target number.
'''
# date 02.06.2020
def twoSum(nums, t):
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] > t:
            end -= 1
        elif nums[start] + nums[end] < t:
            start += 1
        else:
            return [start + 1, end + 1]
nums = list(map(int, input('').split(',')))
t = int(input('t :'))
print(twoSum(nums, t))


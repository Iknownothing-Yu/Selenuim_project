def sumArray(nums):
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result

nums = [3,1,2,10,1]
print(sumArray(nums))

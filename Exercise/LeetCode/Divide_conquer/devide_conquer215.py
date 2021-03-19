'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.
'''
def kLargestEle(nums, k):
    if k > 1:
        nums.remove(max(nums))
        return kLargestEle(nums, k - 1) # 这里return 不可省略，否则无返回值
    else:
        return max(nums)

nums = list(map(int, input('nums :').split(',')))
k = int(input('k :'))
print(kLargestEle(nums, k))

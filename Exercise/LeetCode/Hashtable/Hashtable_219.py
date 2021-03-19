'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
# date 18.04.2020

def findDuplicate(num, k):
    num = list(map(int, num))
    k = int(k)
    num_dic = {}
#  方法1 字典
    for index, ele in enumerate(num):
        if ele not in num_dic:
            num_dic[ele] = index
        elif abs(num_dic[ele] - index) > k:
            num_dic[ele] = index
        else: return True

    return False
# 方法2 列表
'''
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] == num[j] and abs(i-j) <= k:
                    return True
        return False
'''







num = input('please input :').split(',')
k = input('k :')
print(findDuplicate(num, k))

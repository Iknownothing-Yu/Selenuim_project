'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice
'''
# date 13.04.2020

def sumFunc(arr, target):
    arr_dic = {}
# 方法1 若当前ele的补值不在字典key中，则加入，其值为ele在arr的index，
    for index, ele in enumerate(arr):
        # 若ele补值已经在字典key中，则返回ele的index和此key对应的value(也就是此key在arr中的index)
        if (target - ele) in arr_dic:
            return [index, arr_dic[target-ele]]
        else:
            arr_dic[ele] = index
    '''
     for index, ele in enumerate(arr):
        arr_dic[ele] = index

    for ele in arr_dic:
        difference = target - ele
        if difference in arr_dic:
            # if arr[j] == difference:
            return [arr_dic[ele], arr_dic[difference]]
        return 'no such element'
    '''

i = list(map(int, input('').split(',')))
target = 9
print(sumFunc(i, target))



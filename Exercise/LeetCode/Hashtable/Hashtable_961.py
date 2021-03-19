'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.
'''
# date 04.04.2020
def ele_repeate_time(arr):
    hash_repeate = {}
    for index, ele in enumerate(arr):
        if 0 <= int(ele) < 1000:
            if ele not in hash_repeate.keys():
                hash_repeate[ele] = 1
            else:
                hash_repeate[ele] += 1
        else:
            print('input error : please input a valid number!')

    return hash_repeate

def repeate_ele(arr, hash):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        for key in hash.keys():
            if hash[key] == (arr_len / 2):
                return key
    else:
        print('input error: please input a list of even length!')

list = input('please input a list :').split(',')
re_hash = ele_repeate_time(list)
print(repeate_ele(list, re_hash))







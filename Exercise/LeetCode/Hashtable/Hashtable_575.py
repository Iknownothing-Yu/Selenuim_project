'''
Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.
'''
# date 10.04.2020
from collections import defaultdict

def distribute_candies(cand_arr):

    sister_candy_dic = {}
    brother_candy_dic = defaultdict(int)

    if len(cand_arr)%2 != 0:
        print('please input an even number candies!')
    else:
        for candy in cand_arr:
            sister_candy_dic[candy] = cand_arr.count(candy)
        while True:
            sister_candy_num = 0
            for candy_type in sister_candy_dic:
                sister_candy_num += sister_candy_dic[candy_type]
            if sister_candy_num > len(cand_arr) / 2:
                for candy_type, num in sister_candy_dic.items():
                    if num == max(sister_candy_dic.values()):
                        sister_candy_dic[candy_type] -= 1
                        brother_candy_dic[candy_type] += 1
                        break # 很重要，保证每次只从sister中取出一个元素放到brother中
            else: break
    return len(sister_candy_dic)



candy_input = input('input candies :').split(',')
print(distribute_candies(candy_input))

# 方法2
'''
candies = [1,1,1,1,2,3,1,1,5]

print(min(len(set(candies)), len(candies)//2))
'''
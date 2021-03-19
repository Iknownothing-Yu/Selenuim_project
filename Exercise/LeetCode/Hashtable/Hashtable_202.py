'''
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
'''
# date 15-04.2020
def compute_sum(num):
    if int(num) == 1:
        return 'happy number!!'
    else:
        if num in sum_dic:
            return False
        sum_dic[num] = 1
        print('----------sum_dic :', sum_dic)
        num_list = list(str(num))
        sum = 0
        for i in num_list:
            sum += int(i)**2
        return compute_sum(sum)

sum_dic = {}
i = input('please input a number :')
print(compute_sum(i))
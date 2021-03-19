'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented
by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers,
output all of them with no order requirement. You could assume there always exists an answer.
'''
# date 13.04.2020

def common_interest(arr1, arr2):
    arr1_dic = {}
    sum_dic = {}
    for index1, ele1 in enumerate(arr1):
        arr1_dic[ele1] = index1
    for index2, ele2 in enumerate(arr2):
        if ele2 in arr1_dic:
            index = index2 + arr1_dic[ele2]
            sum_dic[index] = ele2
    print('sum_dic :', sum_dic)
    choosed = sum_dic[min(sum_dic.keys())]

    return choosed

arr1 = input('Andy\'s interest :' ).split(',')
arr2 = input('Doris \' interest :' ).split(',')
print('the common interest restaurants are :', common_interest(arr1, arr2))


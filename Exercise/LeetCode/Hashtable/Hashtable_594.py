'''
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
'''
# date 16.04.2020
import collections

def longestHarmoniousSeq(arr):
    s_dic = collections.Counter(arr)
    s_set = sorted(set(arr))
    s_sum = 0
    for i in range(1,len(s_set)):
        if int(s_set[i]) - int(s_set[i-1]) == 1:
            s_sum = max(s_sum, s_dic[s_set[i]] + s_dic[s_set[i-1]])
        else: continue
    return s_sum

arr = input('please input a list :').split(',')
print('the longest length of Harmonious Sequence is : ',longestHarmoniousSeq(arr))



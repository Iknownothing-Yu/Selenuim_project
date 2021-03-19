'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element
in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'
'''
# date 26.04.2020

def findSmallerEle(numarr, target):
    start = 0
    end = len(numarr) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if numarr[mid] == target:
            return numarr[mid +1]
        if numarr[mid] < target:
            start = mid
        if numarr[mid] > target:
            end = mid
    if numarr[end] > target:
        return numarr[end]
    else:
        return numarr[0]


numarr = input('input characters :').split(',')
target = input('target :')
print(findSmallerEle(numarr, target))
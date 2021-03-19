'''
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.
You are guaranteed that the answer is unique.
'''
# date 01.07.2020
def solution(target, n):

    '''
    method1
     j = 1
    result = []

    for ele in target:
        print('ele :', ele)
        if j == ele:
            print('j:', j)
            result.append('push')
            j += 1
        elif j < ele:
            count = ele - j
            for i in range(count):
                result.append('push')
                result.append('pop')
            result.append('push')
            j = ele + 1
    '''
    # method2
    res = []
    result = []
    l = [i for i in range(1, n + 1)]
    i = 0
    while True:
        if res == target:
            return result

        if l[i] in target:
            res.append(l[i])
            result.append("Push")
        else:
            result.append("Push")
            result.append("Pop")
        i += 1

    return result

target = list(map(int, input('target :').split(',')))
n = int(input('n :'))
print(solution(target, n))


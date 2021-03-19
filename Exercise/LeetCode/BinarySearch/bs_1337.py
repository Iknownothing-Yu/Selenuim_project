'''
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows
in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same
number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and
then zeros.
'''
# date 01.05.2020

def kWeakstRow(arrList, k):
    '''
    :param arr:
    :param k:
    :return:
    arrDict = {}
    for liindex, arrele in enumerate(arr):
        soldierNum = arrele.count('1')
        arrDict[liindex] = soldierNum
    return
    '''
    result = []
    for j in range(len(arrList[0])):
        for i in range(len(arrList)):
            if k > 0:
                if arrList[i][j] == 0 and i not in result:
                    k -= 1
                    result.append(i)
            else:
                return result

arrlist = []
k = int(input('please input k :'))
while True:
    arr = input('please insert an arrary :')
    if arr == '':
        break
    else:
        arrlist.append(list(map(int, arr.split(','))))
print(kWeakstRow(arrlist, k))





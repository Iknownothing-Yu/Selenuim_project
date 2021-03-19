'''
Peak Index in a Mountain Array
'''
# date 01.05.2020

def findTop(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        top = (start + end) // 2
        if arr[top+1] > arr[top]:
            start = top + 1
        elif arr[top+1] <= arr[top]:
            end = top

    return arr[start]

arr = input('please insert an array number:').split(',')
print('the top of the array mountain is :', findTop(arr))
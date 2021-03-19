'''
Set Mismatch
'''
# date 16.04.2020

def missingDuplicateNum(arr):
    s = sorted(arr)
    l = []
    for i in range(1, len(s)):
        if int(s[i]) - int(s[i-1]) == 0:
            l.append(int(s[i]))
            l.append(int(s[i]) + 1)
    return l


arr = input('').split(',')
print(missingDuplicateNum(arr))

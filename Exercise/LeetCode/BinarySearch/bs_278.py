'''
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
'''
# date 20.04.2020
def isBadVersion(currentVersion, firstBad):
    if currentVersion < firstBad:
        return False
    else:
        return True


def firstBadVersion(n, fb):
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if isBadVersion(mid, fb) == False:
            start = mid + 1
        if isBadVersion(mid, fb) == True:
            end = mid - 1
    return start


n = int(input('the number of versions :'))
firstBad = int(input('the first bad version :'))
print('I guess the first bad version is :', firstBadVersion(n, firstBad))





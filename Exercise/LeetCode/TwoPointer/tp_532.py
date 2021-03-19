'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.
'''
def kDiffPairs(num, k):
    num.sort()
    count = 0

    for i in range(len(num) - 1):
        j = i + 1
        while j < len(num) and abs(num[i] - num[j]) <= k:
            if k == 0:
                if abs(num[i] - num[j]) == k:
                    count += 1

            else:
                if num[i] != num[i - 1] and num[j] != num[j - 1] and abs(num[i] - num[j]) == k:
                    count += 1

            j += 1

    return count

num = list(map(int, input('num2 :').split(',')))
k = int(input('k :'))
print(kDiffPairs(num, k))


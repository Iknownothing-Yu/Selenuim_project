'''
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
'''
# date 23.08.2020
def longestTurblentSub(nums):
    if len(nums) == 1:
        return 1
    else:
        start, end = 0, 1
        last_signal = '='
        max_num = 1
        current_num = 1

        while end < len(nums):
            current_signal = getComparation(nums[end], nums[end - 1])
            if current_signal == '=' and last_signal != '=':
                max_num = max(max_num, current_num)
                current_num = 1
                last_signal = current_signal
            elif current_signal != '=' and last_signal == '=':
                current_num += 1
                last_signal = current_signal
            else:
                if current_signal == last_signal:
                    if current_num != 1:
                        max_num = max(max_num, current_num)
                        current_num = 1
                else:
                    if current_num == 1:
                        current_num += 2
                    else:
                        current_num += 1

                    last_signal = current_signal

            end += 1

    return max(max_num, current_num)

def getComparation(ele1, ele2):
    if ele1 > ele2:
        return '>'
    if ele1 < ele2:
        return '<'
    if ele1 == ele2:
        return '='

# method 2
'''
def maxTurbulenceSize(A):
    N = len(A)
    ans = 1
    anchor = 0

    for i in range(1, N):
        c = cmp(A[i - 1], A[i])
        if i == N - 1 or c * cmp(A[i], A[i + 1]) != -1:
            if c != 0:
                ans = max(ans, i - anchor + 1)
            anchor = i
    return ans
'''

nums = [3,2,2]
print(longestTurblentSub(nums))
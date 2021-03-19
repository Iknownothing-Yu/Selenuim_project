'''
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
'''
# date 16.06.2020
def deleteMakeSorted(s):
    counter = 0

    for col in range(len(s[0])):
        for row in range(1, len(s)):
            if s[row][col] < s[row - 1][col]:
                counter += 1
                break

    return counter

s = input('A :').split(',')
print(deleteMakeSorted(s))


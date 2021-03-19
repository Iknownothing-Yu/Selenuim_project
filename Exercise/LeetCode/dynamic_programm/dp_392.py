'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of
"abcde" while "aec" is not).
'''
# date 14.06.2020
def isSubquence(s, t):
    i, j = 0, 0

    while True:
        if i < len(s) and j > len(t) - 1:
            return False
        elif i > len(s) - 1:
            return True
        elif s[i] == t[j]:
            i += 1
        j += 1

s = input('s :')
t = input('t :')
print(isSubquence(s, t))


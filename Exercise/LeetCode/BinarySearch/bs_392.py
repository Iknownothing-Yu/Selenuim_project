'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string,
and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
'''
# date 24.04.2020

def isSubsequence(s, t):
    flag = False
    t = list(t)
    current_start = 0
    for letter in s:
        if letter not in t[current_start:len(t)]:
            flag = False
            return flag
        else:
            current_start = t.index(letter)
            flag = True

    return flag


s = list(input('input s :'))
t = list(input('input t :'))
print(isSubsequence(s, t))



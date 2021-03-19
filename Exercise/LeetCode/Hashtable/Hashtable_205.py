'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same character but a character may map to itself.
'''
#date 17.04.2020
def isUniqueMapping(s, t):
    if len(s) != len(t):
        return False
    charMap = dict()
    for i in range(len(s)):
        if s[i] not in charMap:
            charMap[s[i]] = t[i]
        else:
            if t[i] != charMap[s[i]]:
                return False
    return True

def isIsomorphic(s, t):
    return isUniqueMapping(s, t) and isUniqueMapping(t, s)

s = input('s :')
t = input('t :')
print(isIsomorphic(s,t))







'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
'''
# date 01.06.2020
def reserveStr(s):
    i = 0
    j = len(s) - 1
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return s

s = input('s: ').split(',')
print(reserveStr(s))


'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
'''
# date 15.06.2020
def balencedStr(s):
    count, rNum, lNum, i = 0, 0, 0, 0
    while i < len(s):
        if s[i] == 'R':
            rNum += 1
        elif s[i] == 'L':
            lNum += 1

        if rNum == lNum:
            count += 1
            rNum, lNum = 0, 0
        i += 1

    return count

s = input('t :')
print(balencedStr(s))





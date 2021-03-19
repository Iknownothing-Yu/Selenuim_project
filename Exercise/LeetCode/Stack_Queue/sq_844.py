'''
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
# date 04.07.2020
def backspaceCompare(s, t):
    s1, s2 = [], []
    for i in s:
        if i != '#':
            s1.append(i)
        elif s1 and i == '#':
            s1.pop()

    for j in t:
        if j != '#':
            s2.append(j)
        elif s2 and j == '#':
            s2.pop()

    return ''.join(i for i in s1) == ''.join(j for j in s2)

s1 = input('s1 :')
s2 = input('s2 :')
print(backspaceCompare(s1, s2))





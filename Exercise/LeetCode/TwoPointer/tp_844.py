'''
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
# date 07.06.2020
def backspaceCompare(S, T):
    #i = len(S) - 1
    #j = len(T) - 1
    return backspace(S) == backspace(T)


def backspace(arr):
    output_list = []
    for ele in arr:
        output_list.append(ele)
        if ele == '#':
            output_list.pop()
            output_list.pop()
    return output_list

S = input('input S:').split(',')
T = input('input T:').split(',')
print(backspaceCompare(S,T))
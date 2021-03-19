'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
# date 04.07.2020

def validParentheses(s):
    stack = []
    left = ['(', '[', '{']
    for ele in s:
        print('ele :', ele)
        if ele in left:
            stack.append(ele)
        elif (ele == ')' and stack[-1] == '(') or(ele == '}' and stack[-1] == '{') or (ele == ']' and stack[-1] == '['):
            stack.pop()
        else:
            print('i there')
            return False

        print('stack :', stack)

    if not stack:
        return True
    else:

        return False

parentheses = input('p :')
print(validParentheses(parentheses))
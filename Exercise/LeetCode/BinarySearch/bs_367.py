'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
'''
# date 23.04.2020

def validSquare(num):
    num = int(num)
    if num == 0:
        return False
    elif num == 1:
        return True
    else:
        start = 1
        end = num // 2

    while start + 1 < end:
        find = (start + end) // 2
        if find ** 2 == num:
            return find, True
        elif find ** 2 > num:
            end = find
        else: start = find
    return False


num = input('input a number :')
print(validSquare(num))

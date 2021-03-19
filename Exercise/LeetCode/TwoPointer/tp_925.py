'''
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.
'''
# date 06.06.2020
def longPressName(name, press):
    i = 0
    j = 0

    while i < len(name):
        if j > len(press) - 1:
            return False
        elif name[i] == press[j]:
            i += 1
        elif j == 0 or press[j] != press[j - 1]:
            return False
        j += 1

    return True

name = input('name :')
press = input('press :')
print(longPressName(name, press))

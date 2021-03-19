'''
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible
types of commands
'''
# date 28.06.2020

def walkingRobot(cmd, ob):
    print(ob)
    x, y = 0, 0
    direction = 'n'
    for i in cmd:

        if 1 <= i <= 9:
            if direction == 'n':
                while i > 0:
                    if [x, y] not in ob:
                        y += 1
                        i -= 1
                    else:
                        y -= 1
                        break
            if direction == 's':
                while i > 0:
                    if [x, y] not in ob:
                        y -= 1
                        i -= 1
                    else:
                        y += 1
                        break
            if direction == 'w':
                while i > 0:
                    if [x, y] not in ob:
                        x -= 1
                        i -= 1
                    else:
                        x += 1
                        break
            if direction == 'e':
                while i > 0:
                    if [x, y] not in ob:
                        x += 1
                        i -= 1
                    else:
                        x -= 1
                        break
        elif i == -2:
            if direction == 'n':
                direction = 'w'
            elif direction == 's':
                direction = 'e'
            elif direction == 'w':
                direction = 's'
            elif direction == 'e':
                direction = 'n'
        elif i == -1:
            if direction == 'n':
                direction = 'e'
            elif direction == 's':
                direction = 'w'
            elif direction == 'w':
                direction = 'n'
            elif direction == 'e':
                direction = 's'
        print([x, y])

    re = x**2 + y**2

    return re

cmd = list(map(int, input('greedy factor :').split(',')))

ob = []
while True:
    subob = input('obstacle :')
    if subob == '':
        break
    else:
        ob.append(list(map(int, subob.split(','))))

print(walkingRobot(cmd, ob))






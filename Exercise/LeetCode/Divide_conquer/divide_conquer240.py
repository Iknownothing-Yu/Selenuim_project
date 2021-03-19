'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
# date 16.08.2020
def searchTarget(matrix, target):
    if len(matrix) == 0:
        print('I am here')
        return False
    else:
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True

        return False

m = []
target = int(input('target :'))
while True:
    i = input('')
    if i == '':
        break
    else:
        m.append(list(map(int, i.split(','))))

print(searchTarget(m, target))



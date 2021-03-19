'''
Given two arrays, write a function to compute their intersection
'''
# date 01.06.2020
def findIntersection(num1, num2):
    num1 = sorted(set(num1))
    num2 = sorted(set(num2))
    print('num1 :', num1)
    print('num2 :', num2)
    f1, f2 = 0, 0
    result = []
    while f1 < len(num1) and f2 < len(num2):
        if num1[f1] == num2[f2]:
            result.append(num1[f1])
            f1 += 1
            f2 += 1

        else:
           f1, f2 = f1 + (num1[f1] < num2[f2]), f2 + (num1[f1] > num2[f2])
    return result

num1 = list(map(int, input('num1 :').split(',')))
num2 = list(map(int, input('num2 :').split(',')))
print(findIntersection(num1, num2))


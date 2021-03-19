'''
You're now a baseball game point recorder.
Given a list of strings
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
'''
# date 02.07.2020
def solution(s):
    temp = []
    #sum = 0

    for ele in s:
        if temp and ele == '+':
            temp.append(temp[-1] + temp[-2])
            #sum += temp[-1]
        elif temp and ele == 'D':
            temp.append(temp[-1] * 2)
            #sum += temp[-1]
        elif temp and ele == 'C':
            temp.pop()
            #sum -= temp.pop()
        else:
            temp.append(int(ele))
            #sum += temp[-1]
    return sum(temp)

s = input('input string :').split(',')
print(solution(s))







'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
# date 14.06.2020
def climbingStairs(n):
    sumways = [0 for _ in range(n)]
    sumways[0], sumways[1] = 1, 2
    for i in range(2, n):
        sumways[i] = sumways[i - 1] + sumways[i - 2]

    return sumways[n - 1]

n = int(input('s :'))
print(climbingStairs(n))

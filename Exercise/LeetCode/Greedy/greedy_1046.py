'''
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''
# date 18.06.2020
def lastStoneWeight(stones):
    i = len(stones) - 1
    while i > 0:
        stones.sort()
        print(stones)
        if stones[i] == stones[i - 1]:
            stones.pop()
            stones.pop()
            i -= 2
        else:
            stones[i - 1] = stones[i] - stones[i - 1]
            stones.pop()
            i -= 1
    if i == 0:
        return stones[0]
    else:
        return 0

stones = list(map(int, input('num2 :').split(',')))
print(lastStoneWeight(stones))
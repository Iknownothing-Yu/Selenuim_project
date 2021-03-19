'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array
into k non-empty subsets whose sums are all equal.
'''
# date 19.07.2020

class solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.avg = None


    def division(self):
        s = sum(self.nums)
        print('sum :', s)
        if s % self.k == 0:
            self.avg = s // self.k
            print('average :', self.avg)
            self.nums.sort(reverse=True)
            return self.partitialKSub(self.avg, self.nums, self.k)
        else:
            return False

    def partitialKSub(self, currentAvg, currentNums, k, reduced=False):
        print('currentNums:',currentNums)
        print('currentAvg:',currentAvg)
        if k == 0:
            return True
        if reduced == False:
            for currentNum in currentNums:
                if currentNum > currentAvg:
                    return False
                elif currentNum == currentAvg:
                    currentNums.remove(currentNum)
                    reduced = False
                    return self.partitialKSub(self.avg, currentNums, k - 1, reduced)
                else:
                    currentAvg -= currentNum
                    currentNums.remove(currentNum)
                    reduced = True
                    return self.partitialKSub(currentAvg, currentNums, k, reduced)
        elif currentNums[-1] > currentAvg:
            return False
        else:
            for currentNum in currentNums:
                if currentNum == currentAvg:
                    currentNums.remove(currentNum)
                    reduced = False
                    return self.partitialKSub(self.avg, currentNums, k - 1, reduced)
                elif currentNum < currentAvg:
                    currentAvg -= currentNum
                    currentNums.remove(currentNum)
                    reduced = True
                    return self.partitialKSub(currentAvg, currentNums, k, reduced)

li = [7,4,3,2,3,5,2,1,3,2,0]
partitionOb = solution(li, 4)
print(partitionOb.division())






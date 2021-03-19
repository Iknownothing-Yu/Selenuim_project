'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group
numbers and operators. The valid operators are +, - and *
'''
# best solution and tutorial: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/718559/Python3-solution-with-detailed-explanation
class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if input.isdigit():  # 1
            return [int(input)]  # 2
        res = []  # 3
        for i in range(len(input)):  # 4
            if input[i] in "-+*":  # 5
                res1 = self.diffWaysToCompute(input[:i])  # 6
                res2 = self.diffWaysToCompute(input[i + 1:])  # 7
                for j in res1:  # 8
                    for k in res2:  # 9
                        res.append(self.helper(j, k, input[i]))  # 10
        return res  # 11

    def helper(self, m, n, op):  # 12
        if op == "+":  # 13
            return m + n  # 14
        elif op == "-":  # 15
            return m - n  # 16
        else:  # 17
            return m * n  # 18
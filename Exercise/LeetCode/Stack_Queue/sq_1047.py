'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
'''
# date 02.07.2020
def solution(s):
    out = []
    for ele in s:
        if len(out) == 0 or ele != out[len(out) - 1]:
            out.append(ele)

        else:
            out.pop()

    return ''.join(i for i in out)

s = input('s :')
print(solution(s))


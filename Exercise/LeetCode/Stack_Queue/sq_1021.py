'''
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
'''
# date 30.06.2020
def removeOutermost(p):
    count = -1
    result = ''

    for ele in p:
        if ele == '(':
            count += 1
            if count > 0:
                result += ele

        if ele == ')':
            count -= 1
            if count >= 0:
                result += ele

    return result

customers = input('parentheses :')
print(removeOutermost(customers))


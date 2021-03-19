'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child
at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child
will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
and the child i will be content. Your goal is to maximize the number of your content children and output the
maximum number
'''
# date 24.06.2020
def assignCookies(gf, size):
    gf.sort()
    size.sort()
    count, i, j = 0, 0, 0

    while i < len(gf) and j < len(size):
        if gf[i] <= size[j]:
            i += 1
            j += 1
            count += 1
        else:
            j += 1

    return count

gf = list(map(int, input('greedy factor :').split(',')))
size = list(map(int, input('size :').split(',')))
print(assignCookies(gf, size))



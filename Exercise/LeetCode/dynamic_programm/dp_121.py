'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
# date 10.06.2020
def bestSellBuyStock(stock):
    l = len(stock)
    cpt = [[0 for _ in range(l)] for _ in range(l)]

    for i in range(l):
        for j in range(l):
            if i == 0:
                cpt[i][j] = max((stock[j] - stock[i]), cpt[i][j - 1])

            elif j <= i:
                cpt[i][j] = max(cpt[i - 1][j], cpt[i][j - 1])

            else:
                cpt[i][j] = max((stock[j] - stock[i]), cpt[i - 1][j], cpt[i][j - 1])

    return cpt[l - 1][l - 1]

stock = list(map(int, input('stock :').split(',')))
print(bestSellBuyStock(stock))
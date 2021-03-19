'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
# date 18.06.2020
def bestBuySell(stocks):
    sum = 0
    i, j = 0, 1
    while j < len(stocks):
        if stocks[i] > stocks[j]:
            i += 1
            j += 1
        else:
            if j + 1 < len(stocks):
                if stocks[j] > stocks[j + 1]:
                    sum += stocks[j] - stocks[i]
                    i = j + 1
                    j = i + 1
                else:
                    j += 1
            else:
                sum += stocks[j] - stocks[i]
                break
    return sum

stock = list(map(int, input('stocks :').split(',')))
print(bestBuySell(stock))






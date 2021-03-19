'''
At a lemonade stand, each lemonade costs $5.
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
'''
# date 21.06.2020
def lemonadeChange(customers):
    # method 1
    '''
        if customers[0] != 5:
        return False
    else:
        income = []
        for i in range(len(customers)):
            if customers[i] == 5:
                income.append(customers[i])

            else:
                income.sort()
                transaction = customers[i]
                for j in range(len(income) - 1, -1, -1):
                    if transaction - income[j] < 5:
                        j -= 1
                    elif transaction - income[j] > 5:
                        transaction -= income[j]
                        income.pop(j)
                    else:
                        income.pop(j)
                        income.append(customers[i])
                        transaction = 0
                        break
                if transaction != 0:
                    return False
            print('income :', income)
        return True
    '''
    # method2
    five = ten = twenty = 0
    for i in range(len(customers)):
        if customers[i] == 5:
            five += 1
        elif customers[i] == 10:
            if five < 1:
                return False
            five -= 1
            ten += 1
        elif customers[i] == 20:
            if ten >= 1 and five >= 1:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True




customers = list(map(int, input('stocks :').split(',')))
print(lemonadeChange(customers))





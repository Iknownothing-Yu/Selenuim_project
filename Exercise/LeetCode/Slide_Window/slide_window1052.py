'''
 Grumpy Bookstore Owner
'''
# date 18.08.2020

def CustomerMaxSatisfy(customers, grumpy):
    maxSatisfy = 0
    initialCustomer = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0 )
    counter = 2
    g = 0
    while g < len(grumpy) - counter:
        if grumpys[g] == 1:
            temp = sum(customers[t] for t in range(g, g + counter + 1) if grumpys[t] == 1)
            maxSatisfy = max(maxSatisfy, initialCustomer + temp)
        g += 1

    return maxSatisfy

customers = [1,0,1,2,1,1,7,5]
grumpys = [0,1,1,1,0,1,0,0]
print(CustomerMaxSatisfy(customers, grumpys))








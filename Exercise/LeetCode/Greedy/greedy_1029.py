'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
'''
# date 21.06.2020
def twoCityScheduling(costs):
    # variable to store the total cost
    sum = 0
    n= len(costs) // 2
    costs.sort(key=lambda x: x[1] - x[0])
    print(costs)

    # sending first half to city B and remaining to city A
    for row in range(len(costs)):
        if row < n:
            sum += costs[row][1]
        else:
            sum += costs[row][0]

    return sum

costs = []
while True:
    cost = input('costs :')
    if cost == '':
        break
    else:
        costs.append(list(map(int, cost.split(','))))

print(twoCityScheduling(costs))




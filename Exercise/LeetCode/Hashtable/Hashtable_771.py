def output_jewels(jewels):
    hash_J = {}
    if len(jewels) > 50:
        print('over load!')
    else:
        for index, letter in enumerate(jewels):
            if letter not in hash_J.keys():
                hash_J[letter] = index
            else:
                continue
    return hash_J

def output_jewels_num(stones, jewels):
    jewels_number = 0
    if len(stones) > 50:
        print('over load!')
    else:
        for stone in stones:
            if stone in jewels.keys():
                jewels_number+=1
            else:
                continue

    return jewels_number



input_J = input('The jewels are :')
input_S = input('The stones I have :')
j = output_jewels(input_J)
print(output_jewels_num(input_S, j))


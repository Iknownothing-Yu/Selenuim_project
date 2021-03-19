'''
 you provide a hint that indicates how many digits in said guess match your secret number exactly in both
 digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows")
'''
#date 17.04.2020
import collections
def bullCow(secret, guess):
    secret_freq_dic = collections.Counter(secret)
    guess_dic = {}
    result_dic = {'A':0, 'B':0}
    for index, ele in enumerate(guess):
        guess_dic[index] = ele

    for index, ele in enumerate(secret):
        if ele == guess_dic[index]:
            result_dic['A'] += 1
            secret_freq_dic[ele] -= 1
            del(guess_dic[index])

    for ele in guess_dic.values():
        if ele in secret_freq_dic and secret_freq_dic[ele] > 0:
            secret_freq_dic[ele] -= 1
            result_dic['B'] += 1
    return result_dic

secret = list(input('this is secret word :'))
guess = list(input('this is guess word :'))
print(bullCow(secret, guess))

'''
def getHint(self, secret, guess):
        secretStore = {str(i): 0 for i in range(0, 10)}
        guessStore = {str(i): 0 for i in range(0, 10)}
        bullsStore = {str(i): 0 for i in range(0, 10)}

        for i in range(len(secret)):
            secretStore[secret[i]] += 1
            guessStore[guess[i]] += 1

            if guess[i] == secret[i]:
                bullsStore[guess[i]] += 1

        bulls, cows = 0, 0
        for num in bullsStore:
            bulls += bullsStore[num]
            cows += min(secretStore[num], guessStore[num]) - bullsStore[num]

        return str(bulls) + 'A' + str(cows) + 'B'
'''





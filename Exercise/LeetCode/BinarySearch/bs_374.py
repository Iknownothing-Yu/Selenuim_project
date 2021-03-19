def compare(pick, guess):
    if guess > pick:
        return -1
    elif guess < pick:
        return 1
    else: return 0

def guessNum(n, pick):
    start = 1
    end = n
    round = 0

    while start <= end:
        print('----------round :', round, '----------------------')
        print('start', start, 'end : ', end)

        guess = (end + start) // 2
        #print('guess :', guess)

        if compare(pick, guess) == -1:
            end = guess - 1

        elif compare(pick, guess) == 1:
            start = guess + 1

        else: return guess

n = int(input('input n :'))
pick = int(input('pick :'))

print(guessNum(n, pick))



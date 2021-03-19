'''
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.
'''
# date 23.08.2020
def maximumVowel(letters, k):
    vowels = 'aeiou'
    maxNum = 0
    currentNum = 0
    start, end = 0, 0
    counter = k
    while end < len(letters):
        if counter > 0:
            if letters[end] in vowels:
                currentNum += 1
            end += 1
            counter -= 1

        else:
            maxNum = max(maxNum, currentNum)
            start += 1
            counter += 1
            if letters[start] in vowels:
                currentNum -= 1

    return maxNum

letters = 'tryhard'
k = int(input('k :'))
print(maximumVowel(letters, k))








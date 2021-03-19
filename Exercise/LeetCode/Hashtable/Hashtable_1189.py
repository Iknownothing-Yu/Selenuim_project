'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed
'''
# date 11.04.2020

from collections import defaultdict

def count_balloon(arr):
    balloon = 'balloon'
    ba_dict = defaultdict(int)

    for letter in balloon:
        if letter == 'l' or letter == 'o':
            ba_dict[letter] = arr.count(letter)//2
        else:
            ba_dict[letter] = arr.count(letter)

    return min(ba_dict.values())

input_arr = input('input the string :')
print(count_balloon(input_arr))
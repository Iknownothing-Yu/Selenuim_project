'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str
'''
# date 18.04.2020
def isomophWordPattern(pattern, str_arr):
    if len(pattern) != len(str_arr):
        return 'false'
    pattern_dict = {}
    for index, char in enumerate(pattern):
        if char not in pattern_dict:
            pattern_dict[char] = str_arr[index]
        elif pattern_dict[char] != str_arr[index]:
            return 'false'
    return 'true'

def isIsomophic(pattern, str_arr):
    return isomophWordPattern(pattern, str_arr) and isomophWordPattern(str_arr, pattern)

pattern = list(input('input pattern :'))
word_str = input('input a string :').split(' ')
print(isIsomophic(pattern, word_str))

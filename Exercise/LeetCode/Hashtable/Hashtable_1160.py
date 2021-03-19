'''
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6
'''
#date 05.04.2020

# 将characters映射为以每个character为key出现频率为value的字典
def creat_char_freq(chars):
    char_frequency = {}
    for char in chars:
        if char not in char_frequency.keys():
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1
    return char_frequency

# 过滤出输入的string配匹中的word，计算这些word长度加和
def compute_length(arr, chars):
    count = 0
    input_char = chars
    for index, word in enumerate(arr):
        char_freq = creat_char_freq(chars=input_char)
        current_word = ''

        # 把每个word中每个字符和character中每个字符对比，挑出为character的子集的word
        for letter in word:
            if letter in char_freq.keys() and char_freq[letter] > 0:
                char_freq[letter] -= 1
                current_word += letter
            else:
                break

        # 将选中的word长度累加
        if current_word == word:
            count = count + len(word)

    return count

input_words = input('please input words :').split(',')
input_chars = input('please input characters :')

print('the number is :', compute_length(input_words, input_chars))

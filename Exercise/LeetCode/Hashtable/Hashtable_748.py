'''
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate.
Such a word is said to complete the given string licensePlate
'''
# date 11.04.2020
import re

def find_match_words(licenseplate, arr):
    #把licenseplate中字母提取出来
    s_formed = ''.join(re.split(r'[^A-Za-z]', licenseplate)).lower()
    s_dic = {}
    word_dic ={}

    for word in arr:
        word_flag = True
        print('--------current word is :', word, '--------------')

        for ele in s_formed:
            s_dic[ele] = s_formed.count(ele)

        for letter in word:
            if letter in s_dic and s_dic[letter] > 0:
                s_dic[letter] -= 1
            else:
                pass

        for key in s_dic:
            if s_dic[key] > 0:
                word_flag =False
                break
        if word_flag == True:
            word_dic[word] = len(word)

    return word_dic

def chose_word(words_dic):
   return min(words_dic, key=words_dic.get)

licenceplate = '1s3 456'
input_arr = input('').split(',')
print(chose_word(find_match_words(licenceplate,input_arr)))
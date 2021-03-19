'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard .
'''
# date 09.04.2020

class America_keyboard:

    def input_words(self):

        #out_word_list = []

        '''
        for key_board_ele in self.key_board_list:
            key_board_dic[key_board_ele] = 0
        #print('key_board_dic :',key_board_dic)
        for ele in self.words:
            for key in key_board_dic.keys():
                flag = True
                for letter in ele:
                    if letter.lower() not in key:
                        flag = False
                        break
                if flag == True:
                    out_word_list.append(ele)
                    break

        '''

 #  方法2 字典
        self.key_board_dic = {}
        self.word_dic = {}

        for key_board_ele in self.key_board_list:
            self.key_board_dic[key_board_ele] = 0

        for word in self.words:
            self.word_dic[word] = True

        for word in self.words:
            print('current word is :', word)
            for key in self.key_board_dic.keys():
                # print('current key is :', key, key_board_dic.keys())
                for i in word:
                    if i.lower() not in key:
                        print('current letter is: ', i.lower())
                        self.word_dic[word] = False
                        print('word_dic :', self.word_dic)
                        break
                    else:
                        self.word_dic[word] = True
                        continue

                if self.word_dic[word] == True:
                    break
                #print('words[', word, '] :', word_dic[word])
        return self.word_dic

    def  __init__(self, words):
        self.key_board_list = ['qwertzuiop', 'asdfghjkl', 'yxcvbnm']
        self.out_list = []
        self.words = words

input_words = input('input words are :').split(',')
a_keyboard = America_keyboard(input_words)
target_dict = a_keyboard.input_words()
print(target_dict)
target_list = []
for k in target_dict.keys():
    if target_dict[k] == True:
        target_list.append(k)

print(target_list)





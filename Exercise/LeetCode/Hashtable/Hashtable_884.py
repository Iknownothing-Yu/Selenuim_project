'''
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words
'''
#date 10.04.2020
def word_freq(arr1, arr2):

    arr1_list = []
    arr2_list = []

    for word1 in arr1:
        if word1.islower() and arr1.count(word1) == 1 and word1 not in arr2:
            arr1_list.append(word1)

    for word2 in arr2:
        if word2.islower() and arr2.count(word2) == 1 and word2 not in arr1:
            arr2_list.append(word2)
    return arr1_list+arr2_list

s_input_A = input('input the first sentence :').split(' ')
s_input_B = input('input the second sentence :').split(' ')
print(word_freq(s_input_A, s_input_B))

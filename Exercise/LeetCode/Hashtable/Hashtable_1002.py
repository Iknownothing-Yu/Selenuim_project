'''
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the
final answer
不会写！！！
'''
def char_exist(arr):
    chosed_letter = []
    for letter in arr[0]:
        for i in range(1, len(arr)):
            if letter not in arr[i]:
                break
            chosed_letter.append(letter)
    return chosed_letter


input_str = input('this is the input string :').split(',')
print(char_exist(input_str))



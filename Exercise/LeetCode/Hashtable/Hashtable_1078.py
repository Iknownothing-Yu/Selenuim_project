'''
Given words first and second, consider occurrences in some text of the form "first second third",
 where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer
'''
# date 08.04.2020

def out_third(arr, first, second):
    third_list = []
    for i in range(len(arr)):
        if arr[i] == first and arr[i+1] ==second:
            third_list.append(arr[i+2])

    return third_list

input_str = input('please input a sentence :').split(' ')
print(input_str)
firstelememnt = input('first =')
secondelement = input('second =')
print('output is :', out_third(input_str, firstelememnt, secondelement))
'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''
# date 06.06.2020
def reverseVowel(arr):
    i = 0
    j = 1
    vowel = 'aeiou'
    while j < len(arr):
        if arr[i] in vowel and arr[j] in vowel:
            print(arr[i], '-----', arr[j])
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
        elif arr[i] in vowel and arr[j] not in vowel:
            j += 1
        else:
            i += 1
            j += 1

    return ''.join(i for i in arr)

arr = list(input('num2 :'))
print(reverseVowel(arr))


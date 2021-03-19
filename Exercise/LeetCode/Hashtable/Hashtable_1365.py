'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]
'''
def smaller_num(arr):
    input_dic = []
    for index, value in enumerate(arr):
        input_dic.append(0)

        for compare_i in range(len(arr)):
            if value > arr[compare_i]:
                input_dic[index]+=1
            else:
                continue

    return input_dic

input_arr = input('please input one array :')
print(smaller_num(input_arr))





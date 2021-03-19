import re
'''
You are given a data structure of employee information, which includes the employee's unique id,
his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15,
10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]],
and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee
and all his subordinates.
'''
# date 11.04.2020

from collections import defaultdict
def compute_value(arr, emp_ID):
    print('this arr is :', arr)
    emp_dic = {}
    sum_subord_val = 0
    # print('emp_dic[arr[0]] is :', arr[0])
    # print('[arr[1], arr[2]] is :', [arr[1], arr[2]])
    p1 = re.compile(r'[[](.*?)[]]', re.S)
    for employee in arr:
        print('----------------')
        print('employee :', employee)
        pair= re.findall(p1, employee)
        employee_list = employee.split(', [')[0].split(', ')
        employee_list.extend(pair)
        print('employee_list:', employee_list)
        print('employee[1] :', employee_list[1], '--------employee[2] :', employee_list[2])

        emp_dic[employee[0]] = [employee_list[1], employee_list[2]]

    return emp_dic


input_arrs = input('input employee info :')[1:-1].split('], [')
print(compute_value(input_arrs, 1))

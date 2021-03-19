'''
output the number of all subdomains in the input cpdomains
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
'''
#date 04.04.2020
'''
把输入进行几次转化: 
1. 把输入切割成数组['invite_num1 complete domain1', 'invite_num2 complete domain2'...]
2. 把1中每个元素中第二个元素转换成数组，把每级域名都列出来
3. 
'''
def output_domain_hash(domain_str):
    sub_domains = {}# 设置方法内全局的字典按照域名存放访问次数
    for num_domain in domain_str:

        domain = num_domain.split(' ')
        invite_num = int(domain[0])
        # 完整域按照 "." 拆分
        domain_add = domain[1].split('.')
        name_list =[]
        domain_name = ''
        #2. 重新组合拆分掉的部分，把一个完整域名的每级域名放入同一个 name_list
        for name in domain_add[::-1]:
            if name == domain_add[-1]:
                domain_name = name
            else:
                domain_name += name + '.' + domain_name

            name_list.append(domain_name)

        print('name_list :', name_list)

        for name in name_list: # 此循环一定在处理每一个输入字符串的循环内保证 sub_domains 字典记录每个subdomain 的访问次数
            if name not in sub_domains.keys():
                sub_domains[name] = invite_num
            else:
                sub_domains[name] += invite_num
    return sub_domains

'''
接收输入的方法
'''
def inputfunc():
    domain_list =[]
    while True:
        input_str = input('input the domains :')
        if input_str == '':
            break
        else:
            domain_list.append(input_str)
    # print('domain list ist :')
    return domain_list

print(output_domain_hash(inputfunc()))



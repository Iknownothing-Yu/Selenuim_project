import csv
import xlwt
import pandas as pd


data_file = 'C:/Users/yuhan/Downloads/active_data/'
csv_file = pd.read_csv(data_file + '111189754_sale.csv')
csv_file.to_excel(data_file + '1.xlsx', sheet_name='data')

'''
data_file = 'C:/Users/yuhan/Downloads/active_data/111189754_sale.csv'
 with open(csv_file, 'r') as f:
    read = csv.reader(f)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('data')  # 创建一个sheet表格
    l = 0
    for line in read:
        #print(line)
        r = 0
        for i in line:
            #print(i)
            sheet.write(l, r, i)  # 一个一个将单元格数据写入
            r = r + 1
        l = l + 1

  workbook.save('C:/Users/yuhan/Downloads/active_data/1.xlsx')

from request import PandaRequest
 

'''




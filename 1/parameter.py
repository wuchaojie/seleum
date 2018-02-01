#coding=utf-8
'''
Created on 2017��2��21��

@author: fengfan
'''
import xlwt
import xlrd
from datetime import date,datetime
    #指定获取内容必须表格中此行此列此单元数据不全为空
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\configer.xlsx')
    # 获取所有sheet
#     print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[0]
 
    # 根据sheet索引序列进行搜索
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    #根据sheet名称搜索
#     sheet2 = workbook.sheet_by_name('sheet2')
 
    # sheet的名称，行数，列数
#     print sheet1.name,sheet1.nrows,sheet1.ncols
 
    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(3) # 获取第四行内容
    cols = sheet1.col_values(0) # 获取第一列内容
#     print rows
#     print cols
 
    # 获取单元格内容，三种
#     print sheet1.cell(1,0).value.encode('utf-8')
#     print sheet1.cell_value(1,0).encode('utf-8')
#     print sheet1.row(1)[0].value.encode('utf-8')
   
    # 获取单元格内容的数据类型
#     print sheet1.cell(1,0).ctype
#     print sheet1.cell(0,1).value
    #赋值
    maxRobotCount = sheet1.cell(0,1).value
    nlu = sheet1.cell(3,1).value
    broker = sheet1.cell(8,1).value
    db = sheet1.cell(9,1).value
    manager = sheet1.cell(7,1).value
    es = sheet1.cell(4,1).value
    redis = sheet1.cell(5,1).value
    appkey = sheet1.cell(6,1).value
    Move_DB_Count = sheet1.cell(1,1).value
    Move_DB_Time = sheet1.cell(2,1).value
    return maxRobotCount,nlu,broker,db,manager,es,redis,appkey,Move_DB_Count,Move_DB_Time
    
if __name__ == '__main__':
    print read_excel()
    read_excel()    


# maxRobotCount = "20"
# nlu = "10.10.10.193:8880"
# broker = "10.10.10.195:7001"
# db = "10.10.10.195:7001"
# manager = "10.10.10.195:7001"
# es = "10.10.10.192:9200"
# redis = "10.10.10.192;6379;"
# appkey = "2c5d54de"
# Move_DB_Count = "5000"
Move_DB_Time = "5"
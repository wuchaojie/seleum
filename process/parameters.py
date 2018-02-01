#encoding:utf-8  
'''
Created on 2017-3-7

@author: wuchaojie
'''
import xlrd

def read_excel():
    workbook = xlrd.open_workbook(r'D:\configer.xlsx')
    print workbook.sheet_names()#输出获取的shell
    sheet_name = workbook.sheet_names()[0]#获取第一张shell
    print sheet_name
#    sheet = workbook.sheet_by_index(0)   # sheet索引从0开始

    sheet1 = workbook.sheet_by_name("Sheet1")
    print sheet1.name,sheet1.nrows,sheet1.ncols
    rows = sheet1.row_values(4)
    cols = sheet1.row_values(2)
    print rows,cols
   # sheet的名称，行数，列数
#    print sheet.name,sheet.nrow,sheet.nclols
      # 获取单元格内容
    print sheet1.cell(3,1).value.encode('utf-8')
    print sheet1.cell_value(3,1).encode('utf-8')
    print sheet1.row(3)[1].value.encode('utf-8')
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
    read_excel()
    print read_excel()
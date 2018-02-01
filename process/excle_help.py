'''
Created on 2017-3-7

@author: wuchaojie
'''
import xlrd
def read_excel(): 
    workbook = xlrd.open_workbook(r'D:\process.xlsx')
    sheet1 = workbook.sheet_by_name("Sheet1")
    
    domain_name =sheet1.cell(0,1).value
    return domain_name
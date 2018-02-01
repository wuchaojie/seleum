#coding=utf-8
'''
Created on 2017-1-4

@author: wuchaojie
'''
from selenium import webdriver
import time
import unittest
import sys
from excle_help import read_excel

class process(unittest.TestCase):
        
    def setUp(self):
        print '************����֪ʶ����?����****************'
 #       self.browser=webdriver.Chrome(executable_path = 'C:\Windows\SysWOW64\chromedriver.exe')
        self.browser=webdriver.Chrome()
        #self.browser=webdriver.Ie()
        self.browser.get('http://10.10.10.102:8080/sap/#/home/thesaurus')
#         self.browser.find_element_by_id("userName").send_keys("admin")
#         self.browser.find_element_by_id("password").send_keys("123456")
#         self.browser.find_element_by_class_name("loginbtn[type='submit']").click()
#         time.sleep(1)
#         self.browser.browser.find_element_by_link_text("�������").click()
        self.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[1]/div/input").send_keys("admin")
#        self.browser.find_element_by_class_name("username[type='input']").send_keys('admin')
#        self.browser.switch_to_frame("regForm")

#        self.browser.find_element_by_link_text("username").send_keys('admin')

        
    def tearDown(self):
        self.browser.quit()

    def testcase0(self):
           
        print 1


if __name__ == '__main__':
 #   domain_name = read_excel()
    sys.argv = ['','process.testcase0']
    unittest.main()

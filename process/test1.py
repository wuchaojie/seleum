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
        print '************进入知识库管理导航栏****************'
 #       self.browser=webdriver.Chrome(executable_path = 'C:\Windows\SysWOW64\chromedriver.exe')
        self.browser=webdriver.Chrome()
        #self.browser=webdriver.Ie()
        self.browser.get('http://10.10.10.195:8900/CSRManagerWebSite/login')
        self.browser.find_element_by_id("userName").send_keys("admin")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.browser.find_element_by_class_name("loginbtn[type='submit']").click()
#         time.sleep(1)
#         self.browser.browser.find_element_by_link_text("领域管理").click()

    def tearDown(self):
        self.browser.quit()

    def testcase0(self):
           
        print ('''
        checkpoint:验证工具栏中编辑按钮中添加按钮功能
                        第一步：切换到领域管理界面
                        第二步：切换窗口到childIframe0界面
                        第三步：点击工具栏中的编辑按钮
                        第四步：点击编辑按钮中添加按钮跳转到添加界面    
                       第五步：输入要添加的领域名
                       第六步： 点击添加按钮，跳转到添加成功界面                                
        ''')
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(1)
 #       self.browser.quit()
#         self.browser.find_element_by_id("btnAdd").click()
#         time.sleep(1) 
#         self.browser.find_element_by_id("addName").clear()
#        # self.browser.find_element_by_id("addName").send_keys(domain_name)
#         self.browser.find_element_by_id("addName").send_keys("213")
#         time.sleep(1)
#         self.browser.find_element_by_id("sureAdd").click()
#         time.sleep(1)
#      
#         self.browser.find_element_by_link_text("确定").click()
#         time.sleep(1)
#         self.browser.switch_to_default_content()
#         time.sleep(1)
#         self.browser.find_element_by_xpath('//*[@id="itemDiv"]/div[1]/div[3]/ul/li[2]/a[2]').click()
#         self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
#         time.sleep(1)#休眠2秒#  
#         self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#   


if __name__ == '__main__':
 #   domain_name = read_excel()
    sys.argv = ['','process.testcase0']
    unittest.main()

#coding=utf-8

'''
Created on 2017-1-6

@author: zhangyongjie
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import logging
import HTMLTestRunner
import sys


class KnowledgeManageTest(unittest.TestCase):
        #启动浏览器并进入到客服后台
        
    def setUp(self):
        print '************进入知识库管理导航栏****************'
        self.browser=webdriver.Chrome()
        self.browser.get('http://10.0.1.118:28080/CSRManagerWebSite/default')
        self.browser.maximize_window()#将浏览器最大化显示
        #通过get方法获取当前URL打印
        print "now access %s"%('http://10.0.1.118:28080/CSRManagerWebSite/default')
        self.browser.find_element_by_id("userName").send_keys("admin")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.browser.find_element_by_class_name("loginbtn[type='submit']").click()
#         time.sleep(1)
#         self.browser.browser.find_element_by_link_text("领域管理").click()
        time.sleep(1)
        pass

    def tearDown(self):
        
        time.sleep(2)
        self.browser.quit()
        print '************关闭智能客服，并退出浏览器************'
        pass
 

    def testcase1(self):   
        print ('''
                        添加领域                 
        ''')
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(2)
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)
        self.browser.find_element_by_id("addName").send_keys("sssss")
        time.sleep(1)
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()
        time.sleep(1) 

        print 'testcase1完成'
        
    def testcase2(self):  
        print ('''
                        修改领域
        ''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(3)
#        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-9"]/td[3]/div').click()
        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[3]/div').click()

        time.sleep(1)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(1)
        self.browser.find_element_by_id('btnUpdate1').click()
        time.sleep(1) 
        self.browser.find_element_by_id('updateName').send_keys("test")
        time.sleep(1) 
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1) 
        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[3]/a/span/span').click()
        time.sleep(2)#休眠2秒# 
        print 'testcase2完成'
        
    def testcase3(self):  
        print ('''
                        删除 领域                 
        ''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(3)
#        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-9"]/td[3]/div').click()
        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[3]/div').click()
        time.sleep(2)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(3)
        self.browser.find_element_by_id('btnDelete').click()
        time.sleep(2)   
        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
#        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(2)#休眠2秒#  
        print 'testcase3完成'
        
    def testcase4(self):  
        print ('''停用''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(3)
#        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-9"]/td[3]/div').click()
        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[3]/div').click()
        time.sleep(2)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(3)
        self.browser.find_element_by_id('btnStop').click()
        time.sleep(2)   
        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
#        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(2)#休眠2秒#  
        print 'testcase4完成'
        
    def testcase5(self):  
        print ('''启用
        ''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(3)
#        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-9"]/td[3]/div').click()
        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[3]/div').click()
        time.sleep(2)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(3)
        self.browser.find_element_by_id('btnResume').click()
        time.sleep(2)   
        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
#        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(2)#休眠2秒#  
        print 'testcase5完成'
        
    def testcase6(self):  
        print ('''刷新''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        try:
            self.browser.find_element_by_id("reloadData1")
        except Exception, er:
            self.fail("刷新页面失败")
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
#        self.browser.find_element_by_link_text("确定").click()
#        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(2)#休眠2秒#  
        print 'testcase6完成'
        
    def testcase7(self):  
        print ('''挂接''')
        time.sleep(1)#休眠2秒#  btnUpdate1 
        self.browser.find_element_by_xpath("//*[@id='navDiv']/div[1]/div[2]/ul[1]/li/strong/a").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[3]/div').click()
        time.sleep(2)
        self.browser.find_element_by_id('btnLink').click()
        time.sleep(3)
        self.browser.find_element_by_id('btnResume').click()
        time.sleep(2)   
        self.browser.find_element_by_link_text("确定").click()
        self.browser.find_element_by_xpath('/html/body/div[15]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(2)#休眠2秒#  
        print 'testcase7完成'
        
#     def testcase4(self):  
#         #知识审核
#         time.sleep(1)#休眠2秒# 
#         self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
#         time.sleep(1)#休眠2秒#  
#         self.browser.find_element_by_link_text("知识管理").click()
#         time.sleep(1)#休眠2秒#  
#         self.browser.switch_to_frame("childIframe0")
#         time.sleep(1)#休眠2秒#   
#         self.browser.find_element_by_id("btnAudit").click()
#         time.sleep(1)#休眠2秒#  
#         #self.browser.find_element_by_id("btnAuditAll").click()
#         self.browser.find_element_by_xpath('//*[@id="datagrid-row-r1-2-10"]/td[3]/div/input').click()
# 
#         time.sleep(1)#休眠2秒#  
#         #self.browser.switch_to_default_content()
#         #self.browser.switch_to_frame("childIframe2")
#         #self.browser.find_element_by_xpath('/html/body/div[19]/div[2]/div[4]/a[1]/span/span').click()
#         self.browser.find_element_by_link_text("确定").click() 
#         time.sleep(4)#休眠2秒# 

if __name__ == '__main__':     
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mytest.log',
                filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(' %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
         
    testsuite=unittest.TestSuite()
    testsuite.addTest(KnowledgeManageTest("testcase1"))
    testsuite.addTest(KnowledgeManageTest("testcase2"))
    testsuite.addTest(KnowledgeManageTest("testcase3"))
#     testsuite.addTest(KnowledgeManageTest("testcase4"))
#     testsuite.addTest(KnowledgeManageTest("testcase5"))
     
    testReportName = "./testReport.html"
    reportNp=file(testReportName,"wb")
     
    runner = HTMLTestRunner.HTMLTestRunner(stream=reportNp,title='测试报告',description='测试报告')
    runner.run(testsuite)
#    sys.argv = ['', 'KnowledgeManageTest.testcase1','KnowledgeManageTest.testcase2','KnowledgeManageTest.testcase3']
#    sys.argv = ['', 'KnowledgeManageTest.testcase4','KnowledgeManageTest.testcase5']
#    sys.argv = ['', 'KnowledgeManageTest.testcase6']
#     unittest.main()
     

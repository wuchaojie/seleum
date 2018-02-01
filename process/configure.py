#coding=utf-8

'''
Created on 2017-1-6

@author: fengfan
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
import time
import unittest
import logging
import HTMLTestRunner
#import parameter as pra
from parameters import read_excel  



class KnowledgeManageTest(unittest.TestCase):
        
    def setUp(self):
        print '************进入知识库管理导航栏****************'
        #启动浏览器并进入到客服后台
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('http://10.10.10.193:8075/CSRManagerWebSite/login')
        self.browser.find_element_by_id("userName").send_keys("admin")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.browser.find_element_by_class_name("loginbtn[type='submit']").click()
        time.sleep(1)       
        

#         self.browser.find_element_by_link_text("领域管理").click()
#         time.sleep(1)
        pass

    def tearDown(self):
        
        time.sleep(1)
        self.browser.quit()
        print '************关闭智能客服，并退出浏览器************'
        pass
    
    def testDomainManage01(self):
        
        print ('''
                            设置机器人最大数量           
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-0").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys(int(maxRobotCount))
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()

    def testDomainManage02(self):
        
        print ('''
                            设置nlu识别地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-1").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+nlu+"/nlu/recognise")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()
               
    def testDomainManage03(self):
        
        print ('''
                            设置nlu同步地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-2").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+nlu+"/nlu/SyncModel")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()   
    
    def testDomainManage04(self):
        
        print ('''
                            设置broker即时测试地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-3").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+broker+"/CSRBroker/queryAction")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()  
        
    def testDomainManage05(self):
        
        print ('''
                            设置db地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-4").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+db+"/CSRManagerDataBaseInterface/DBInterFace/OperateDataAction")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()  
        
    def testDomainManage06(self):
        
        print ('''
                            设置broker地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-5").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+broker+"/CSRBroker/sync")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 

    def testDomainManage07(self):
        
        print ('''
                            设置manager地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-6").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+manager+"/CSRManagerWebSite/")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage08(self):
        
        print ('''
                            设置es地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-7").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+es+"/csr_anal")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage09(self):
        
        print ('''
                            设置nlu自学习地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-8").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+nlu+"/nlu/train")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage10(self):
        
        print ('''
                            设置redis地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-9").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys(redis)
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage11(self):
        print ('''
                            设置appkey地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-10").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys(appkey)
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage12(self):
        print ('''
                            设置移动对话记录数量
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-15").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys(int(Move_DB_Count))
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage13(self):
        print ('''
                            设置移动对话记录间隔
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r1-2-16").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys(int(Move_DB_Time))
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
    def testDomainManage14(self):
        print ('''
                            设置图片获取地址
        ''')
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[3]/div[1]/div[1]').click()
        time.sleep(1)        
        self.browser.find_element_by_link_text("系统参数").click()
        time.sleep(1)
        clickRtn=self.browser.switch_to_frame("childIframe0")
        self.assertEqual(clickRtn, None)
        time.sleep(1)
        self.browser.find_element_by_id("nextPage").click()
        time.sleep(1)
        self.browser.find_element_by_id("datagrid-row-r2-2-5").click()  
        time.sleep(1)
        implement = self.browser.find_element_by_id('btnUpdate')
        time.sleep(1)
        ActionChains(self.browser).move_to_element(implement).perform()
        time.sleep(1)     
        self.assertEqual(self.browser.find_element_by_id("btnUpdate1").is_displayed(), True)
        time.sleep(1)
        self.browser.find_element_by_id("btnUpdate1").click()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").clear()
        time.sleep(1)
        self.browser.find_element_by_id("updateValueArea").send_keys("http://"+manager+"/CSRManagerWebSite/")
        time.sleep(1)
        self.browser.find_element_by_id("sureUpdate").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click() 
        
if __name__ == '__main__':
    maxRobotCount,nlu,broker,db,manager,es,redis,appkey,Move_DB_Count,Move_DB_Time= read_excel()
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
    testsuite.addTest(KnowledgeManageTest("testDomainManage01"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage02"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage03"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage04"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage05"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage06"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage07"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage08"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage09"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage10"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage11"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage12"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage13"))
    testsuite.addTest(KnowledgeManageTest("testDomainManage14"))
    testReportName = "./testReport.html"
    reportNp=file(testReportName,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=reportNp,title='Result',description='Test_Report')
#     sys.argv = ['', 'KnowledgeManageTest.testDomainManage101']
#     unittest.main()
    runner.run(testsuite)
    
    pass
#coding=utf-8
'''
Created on 2017-1-4

@author: wuchaojie
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HTMLTestRunner
import logging

class process(unittest.TestCase):
        #启动浏览器并进入到客服后台
        
    def setUp(self):
        print '************进入知识库管理导航栏****************'
        self.browser=webdriver.Chrome()
        #self.browser=webdriver.Ie('C:\Windows\System32\IEDriverServer.exe')
        #self.browser=webdriver.Ie()
        self.browser.get('http://10.10.10.195:8999//CSRManagerWebSite/login')
        self.browser.find_element_by_id("userName").send_keys("admin")
        self.browser.find_element_by_id("password").send_keys("123456")
        self.browser.find_element_by_class_name("loginbtn[type='submit']").click()
        time.sleep(1)
        pass

    def tearDown(self):
        
        time.sleep(1)
        self.browser.quit()
        print '************关闭智能客服，并退出浏览器************'
        pass
 
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
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线")
        time.sleep(1)
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)
     
        self.browser.find_element_by_link_text("确定").click()
        time.sleep(1)
#         self.browser.switch_to_default_content()
#         time.sleep(1)
#         self.browser.find_element_by_xpath('//*[@id="itemDiv"]/div[1]/div[3]/ul/li[2]/a[2]').click()
#         self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
#         time.sleep(1)#休眠2秒#  
#         self.browser.find_element_by_link_text("知识管理").click()
        
        time.sleep(1)#休眠2秒#   
        
    def testcase1(self):  
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[6]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("渠道管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u'微信')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addProtocolNum").send_keys('22')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('//*[@id="addDiv"]/div/div/table/tbody/tr[6]/td[2]/span/input[1]').click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id("_easyui_combobox_2").click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id("sureAdd").click()    
            
    def testcase2(self):  
        #添加机器人
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[6]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("渠道管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u'电话')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addProtocolNum").send_keys('3') 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)#休眠2秒# 
        #self.browser.find_element_by_link_text("确定").click() 
        self.browser.find_element_by_xpath('/html/body/div[11]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#  
        
    def testcase3(self):  
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("fileUploadframe")
        #self.browser.switch_to_default_content()
        #self.browser.switch_to_frame("childIframe2")
        self.browser.find_element_by_name("excelFile").send_keys(u'E:\\歌华有线-标准问.xlsx')
        time.sleep(1)
        self.browser.find_element_by_link_text("上传").click()
        time.sleep(20)
        
    def testcase4(self):  
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[6]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("渠道管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u'图文渠道')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addProtocolNum").send_keys('4')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('//*[@id="addDiv"]/div/div/table/tbody/tr[6]/td[2]/span/input[1]').click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id("_easyui_combobox_2").click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)#休眠2秒# 

    def testcase5(self):  
        #添加机器人
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[6]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("机器人管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u'四川地税机器人')
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addHighThreshold").send_keys('60') 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addLowThreshold").send_keys('20')
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)#休眠2秒# 
        #self.browser.find_element_by_link_text("确定").click() 
        self.browser.find_element_by_xpath('/html/body/div[27]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#               /html/body/div[27]/div[2]/div[3]/a/span/span
            
    def testcase6(self):  
        #知识审核
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAudit").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_xpath('//*[@id="btnAuditAll"]/span/span').click()

        time.sleep(1)#休眠2秒#  
        #self.browser.switch_to_default_content()
        #self.browser.switch_to_frame("childIframe2")
        #self.browser.find_element_by_xpath('/html/body/div[19]/div[2]/div[4]/a[1]/span/span').click()
        self.browser.find_element_by_link_text("确定").click() 
        time.sleep(1)#休眠2秒# 
        
    def testcase7(self):  
        #知识审核
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识审核").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAudit").click()
        self.browser.find_element_by_link_text("全部领域审核通过").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_xpath('/html/body/div[13]/div[2]/div[4]/a[1]/span/span').click()
        time.sleep(1)#休眠2秒#  
        #self.browser.switch_to_default_content()
        #self.browser.switch_to_frame("childIframe2")
        #self.browser.find_element_by_xpath('/html/body/div[19]/div[2]/div[4]/a[1]/span/span').click()
        self.browser.find_element_by_link_text("确定").click() 
        time.sleep(1)#休眠2秒#   
          
    def testcase8(self):
        self.browser.find_element_by_link_text("场景定制").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)
        self.browser.find_element_by_id('btnUpdate').click()
        time.sleep(1)
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线场景")
        time.sleep(1)
        self.browser.find_element_by_id("sureAdd").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()
        time.sleep(1)
        
    def testcase9(self):
        self.browser.find_element_by_link_text("场景定制").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)
        self.browser.find_element_by_id('datagrid-row-r1-2-0').click()
        time.sleep(1)
        self.browser.find_element_by_id("btnUploadScene").click()
        time.sleep(1)
        self.browser.find_element_by_name("substanceFile").send_keys(u'E:\\歌华有线场景.zip')
        time.sleep(1)        
        self.browser.find_element_by_id("sureUpload").click()
        time.sleep(1)    
        self.browser.find_element_by_link_text("Ok").click()
        time.sleep(1)    
        
    def testcase10(self):
        self.browser.find_element_by_link_text("实体域管理").click()
        time.sleep(1)
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)
        self.browser.find_element_by_id('btnMulti').click()
        time.sleep(1)
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)
        self.browser.find_element_by_link_text("确定").click()
        time.sleep(1)
        self.browser.switch_to_frame("fileUploadframe")
        
        frame = self.browser.find_element_by_xpath('//*[@id="uploadtd"]/iframe')
        clickRtn=self.browser.switch_to_frame(frame)
#        self.assertEqual(clickRtn, None) 
        time.sleep(1)
        self.browser.find_element_by_name("excelFile").send_keys(u"E:\\实体.xls")
        time.sleep(5)
        self.browser.find_element_by_id("btnrun").click()
        time.sleep(5)
        
    def testcase11(self):  
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("fileUploadframe")
        self.browser.find_element_by_id("rq").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.switch_to_default_content()
        #self.browser.switch_to_frame("childIframe2")
        self.browser.find_element_by_name("excelFile").send_keys(u'E:\\歌华有线-扩展问.xlsx')
        time.sleep(1)
        self.browser.find_element_by_link_text("上传").click()
        time.sleep(15)        

    def testcase12(self):  
        self.browser.find_element_by_link_text("同义词库管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线-同义词")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureAdd").click()        
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[9]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#     
         
    def testcase13(self):  
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("同义词管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_name("excelFile").send_keys(u"E://歌华有线-同义词.xlsx")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureUpload").click()        
        time.sleep(10)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#    
                 
    def testcase14(self):  
        self.browser.find_element_by_link_text("重要词库管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线-重要词")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureAdd").click()        
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[9]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#     
         
    def testcase15(self):  
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("重要词汇管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_name("excelFile").send_keys(u"E://歌华有线-重要词.xlsx")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureUpload").click()        
        time.sleep(10)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#   
    def testcase16(self):  
        self.browser.find_element_by_link_text("停用词库管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线-停用词")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureAdd").click()        
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[9]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#     
         
    def testcase17(self):  
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("停用词管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_name("excelFile").send_keys(u"E://歌华有线-停用词.xls")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureUpload").click()        
        time.sleep(10)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒# 
                  
    def testcase18(self):  
        self.browser.find_element_by_link_text("敏感词库管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnAdd").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("addName").send_keys(u"歌华有线-敏感词")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureAdd").click()        
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[9]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#          
    def testcase19(self):  
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("敏感词管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0") 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnMulti").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpload").click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_name("excelFile").send_keys(u"E://歌华有线-敏感词.xls")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("sureUpload").click()        
        time.sleep(10)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a/span/span').click()
        time.sleep(1)#休眠2秒#           
    def testcase20(self):  
        #文本问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("question1").send_keys(u"标准问题") 
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id("pluginTextAnswer1").send_keys(u"标准答案")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#   
        self.browser.find_element_by_link_text('确定').click()
        time.sleep(1)#休眠2秒#   
        
    def testcase21(self):  
        #模式问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        self.browser.find_element_by_id('_easyui_combobox_6').click()
        time.sleep(1)
        self.browser.find_element_by_id('partternName').send_keys(u"文本模式问题")

        self.browser.find_element_by_id('partternCode').send_keys(u"文本模式问题")
        time.sleep(1)
        self.browser.find_element_by_id('pluginTextAnswer1').send_keys(u"文本模式答案")
        time.sleep(1)
        self.browser.find_element_by_id('btnAdd').click()
        time.sleep(1) 
        self.browser.find_element_by_link_text('确定').click()
        time.sleep(1) 
        
    def testcase22(self):  
        #图文渠道纯文本问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        self.browser.find_element_by_id('_easyui_combobox_7').click()
        time.sleep(1)
        self.browser.find_element_by_id('question1').send_keys(u"纯文本导航问题1")
        time.sleep(1) 
        self.browser.find_element_by_id('seleNaviKnoBtn1').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="knowNaviWin"]/div/div[2]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id('startWord1').send_keys(u"纯文本导航问题引导语")
        time.sleep(1)
        self.browser.find_element_by_id('overWord1').send_keys(u"纯文本导航问题结束语") 
        time.sleep(1) 
        self.browser.find_element_by_id('selectKnoDoneBtn').click()
        time.sleep(1) 
        self.browser.find_element_by_id('btnAdd').click()
        time.sleep(1)
        self.browser.find_element_by_link_text('确定').click()
        time.sleep(1)#休眠2秒#  
                  
    def testcase23(self):  
        #图文渠道导航问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[1]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_9').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_8').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_7').click()
        time.sleep(1)
        self.browser.find_element_by_id('question1').send_keys(u'图文渠道导航问题')
        time.sleep(1)
        self.browser.find_element_by_id('seleNaviKnoBtn191772639').click() 
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="knowNaviWin"]/div/div[2]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_id('selectKnoDoneBtn').click()
        time.sleep(1)
        self.browser.find_element_by_id('startWord191772639').send_keys(u"图文渠道导航问题引导语")
        time.sleep(1)
        self.browser.find_element_by_id('overWord191772639').send_keys(u"图文渠道导航问题结束语") 
        time.sleep(1) 
        self.browser.find_element_by_id('btnAdd').click()
        time.sleep(1)
        self.browser.find_element_by_link_text('确定').click()
        time.sleep(1)#休眠2秒#   
    def testcase24(self):  
        #图文渠道模式问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[1]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_9').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_8').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
#         self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/span/input[1]').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_6').click()
        time.sleep(1) 
        self.browser.find_element_by_id('pluginWechatisPicture191772639').click()
        time.sleep(1)
        self.browser.find_element_by_id('partternName').send_keys(u'图文渠道模式问题')
        time.sleep(1)
        self.browser.find_element_by_id('partternCode').send_keys(u'图文渠道模式问题')
        time.sleep(1)
        self.browser.find_element_by_id('pluginWechatwordAnswer191772639').send_keys(u'图文渠道模式答案')
        time.sleep(1)
        self.browser.find_element_by_id('btnAdd').click()
        time.sleep(1)
        self.browser.find_element_by_link_text('确定').click()
        time.sleep(1)#休眠2秒#  
        
    def testcase25(self):  
        #图文渠道模式问题
        time.sleep(1)#休眠2秒# 
        self.browser.find_element_by_xpath('//*[@id="navDiv"]/div[2]/div[1]/div[2]/a[2]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_link_text("知识管理").click()
        time.sleep(1)#休眠2秒#  
        self.browser.switch_to_frame("childIframe0")
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id("btnUpdate").click()
        time.sleep(1)#休眠2秒#  
        #self.browser.find_element_by_id("btnAuditAll").click()
        self.browser.find_element_by_id('btnAdd').click() 
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[1]/td[2]/span/input[1]').click()
        time.sleep(1)#休眠2秒#  
        self.browser.find_element_by_id('_easyui_combobox_9').click()
        time.sleep(1)
        self.browser.find_element_by_id('_easyui_combobox_8').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[1]').click()
        time.sleep(1)
        self.browser.find_element_by_id('question1').send_keys(u'图文渠道图文问题')
        time.sleep(1)
        self.browser.find_element_by_id('pluginWechattitpic191772639').send_keys(u'图文标题')
        time.sleep(1)
        self.browser.find_element_by_id('pluginWechatabstext191772639').send_keys(u'图文摘要')
        time.sleep(1) 
        self.browser.find_element_by_id('pluginWechatsuperCon191772639').send_keys(u'www.baidu.com')
        time.sleep(1)
        self.browser.find_element_by_id('pluginWechatInputFile191772639').send_keys(u'E:\壁纸候选\pixiv.png')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="pluginWechatPicArea191772639"]/div[7]/a/span/span').click()
        time.sleep(1)
        self.browser.find_element_by_id('btnAdd').click()
        time.sleep(1)
        self.browser.find_element_by_link_text('确定').click() 
        time.sleep(1)#休眠2秒#         
                                
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
    testsuite.addTest(process("testcase0"))
    testsuite.addTest(process("testcase1"))
    testsuite.addTest(process("testcase2"))
    testsuite.addTest(process("testcase3"))
    testsuite.addTest(process("testcase4"))
    testsuite.addTest(process("testcase5"))
#    testsuite.addTest(process("testcase6")) 
#    testsuite.addTest(process("testcase7"))                                                                                                                                                                                                                                                                                                      
    testsuite.addTest(process("testcase8"))
    testsuite.addTest(process("testcase9"))
    testsuite.addTest(process("testcase10"))
    testsuite.addTest(process("testcase11"))
    testsuite.addTest(process("testcase12"))
    testsuite.addTest(process("testcase13"))
    testsuite.addTest(process("testcase14"))
    testsuite.addTest(process("testcase15"))
    testsuite.addTest(process("testcase16"))
    testsuite.addTest(process("testcase17"))          
    testsuite.addTest(process("testcase18"))          
    testsuite.addTest(process("testcase19"))    
    testsuite.addTest(process("testcase20"))          
    testsuite.addTest(process("testcase21"))   
    testsuite.addTest(process("testcase22"))   
    testsuite.addTest(process("testcase23"))   
    testsuite.addTest(process("testcase24"))   
    testsuite.addTest(process("testcase25"))   
#    testsuite.addTest(process("testcase26"))   
    
    testReportName = "./testReport.html"
    reportNp=file(testReportName,"wb")
       
    runner = HTMLTestRunner.HTMLTestRunner(stream=reportNp,title='测试报告',description='测试报告')
    runner.run(testsuite)
#     sys.argv = ['', 'process.testcase7']
#     unittest.main()

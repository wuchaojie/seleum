#encoding=utf-8
'''
Created on 2016-11-14

@author: libin
'''
import uuid
import time
import unittest
from xml.etree import ElementTree as ETree
from hci_http_test_kit import HttpHelper, Logger

#url1=r"http://10.0.0.223:8090/1.wav"
url1=r"http://10.0.1.68:8090/1.wav"
#url2=r"http://10.0.0.223:8090/1.wav"
url2=r"http://10.0.1.68:8090/1.wav"
url_str=url1+";"+url2
same_url_str=url1+";"+url1

# url_str="rtsp://10.0.1.15/a1.aac;rtsp://10.0.1.15/a2.aac"
# same_url_str="rtsp://10.0.1.15/a1.aac;rtsp://10.0.1.15/a1.aac"

def get_xml(**kw):
    root = ETree.Element("RequestInfo")
    for keyword in kw:
        sub = ETree.SubElement(root, keyword)
        sub.text = kw[keyword]

    tree = ETree.ElementTree(root)
    tree.write("./temp", "utf-8")
    xml_str = open("./temp", "rb").read()
    #xml_str += "\n"
    
    
#     print len(xml_str)
    return xml_str

def analyze_xml(str_input):
    result = {}
    root = ETree.fromstring(str_input)
    for children in root:
        result[children.tag] = children.text
    return result

class tingshen_func_test(unittest.TestCase):
    
#     def setUp(self):
#         func_helper._logger.debug()
    
    def test_0(self):
        '''
        正常: 初始化
        '''
        func_helper._logger.info("test_0")
        body = get_xml(
                       Command="Init",
#                     Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_normal_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_normal_"+str(identify)
                       )
         
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
         
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Idle;Idle")
        
    def test_0_1(self):
        '''
    重复调用Init
        '''
        func_helper._logger.info("test_0_1")
        #第一次
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_repeat_init_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #第二次
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_repeat_init_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Already init")
        self.assertEquals(analyze_result["ErrorNo"], "2")
        
        body = get_xml(
                       Command="End",
                       Identify="test_repeat_init_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_1(self):
        '''
        正常: 开始
        '''
        func_helper._logger.info("test_1")
        body = get_xml(
                       Command="Start",
                       Identify="test_normal_"+str(identify)
#                        Identify="test_normal_",
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(1)
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_normal_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        
        
    def test_1_1(self):
        '''
        重复调用开始
        '''
        func_helper._logger.info("test_1_1")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_repeat_start_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #start 1
        body = get_xml(
                       Command="Start",
                       Identify="test_repeat_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(1)
        #start 2
        body = get_xml(
                       Command="Start",
                       Identify="test_repeat_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Busy")
        self.assertEquals(analyze_result["ErrorNo"], "7")
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        
        #清理工作
        body = get_xml(
                       Command="Stop",
                       Identify="test_repeat_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_repeat_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
    def test_1_2(self):
        '''
        未初始化直接调用start
        '''
        func_helper._logger.info("test_1_2")
        body = get_xml(
                       Command="Start",
                       Identify="test_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")
        
    def test_1_3(self):
        '''
        在Stop后再次Start
        '''
        func_helper._logger.info("test_1_3")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #start 1
        body = get_xml(
                       Command="Start",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(1)
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        
        #stop
        body = get_xml(
                       Command="Stop",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        try:
            self.assertEquals(analyze_result["Status"], "Stoped;Stoped")
        except :
            self.assertEquals(analyze_result["Status"], "Idle;Idle")
        
#        time.sleep(3)
        
        #start 2
        body = get_xml(
                       Command="Start",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        #该位置有可能为Failed,Stoped后不会立即变为Idle
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(3)
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        
        #清理工作
        body = get_xml(
                       Command="Stop",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_after_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
    def test_2(self):
        '''
        正常: 停止
        '''
        func_helper._logger.info("test_2")
        body = get_xml(
                       Command="Stop",
                       Identify="test_normal_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_normal_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Stoped;Stoped")

    def test_2_1(self):
        '''
        重复Stop
        '''
        func_helper._logger.info("test_2_1")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       #Url="rtsp://10.0.1.15:8554/1.aac;rtsp://10.0.1.15:8554/2.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #start
        body = get_xml(
                       Command="Start",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(5)
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        
        #stop 1
        body = get_xml(
                       Command="Stop",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#         time.sleep(3)
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        #有可能为Idle;Idle
        self.assertEquals(analyze_result["Status"], "Stoped;Stoped")
        
#        time.sleep(5)
        
        #stop 2
        body = get_xml(
                       Command="Stop",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Idle;Idle")
        
        #清理
        body = get_xml(
                       Command="End",
                       Identify="test_repeat_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")

    def test_2_2(self):
        '''
        未初始化直接调用stop
        '''
        func_helper._logger.info("test_2_2")
        body = get_xml(
                       Command="Stop",
                       Identify="test_stop_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_2_3(self):
        '''
        未start直接调用stop
        '''
        func_helper._logger.info("test_2_3")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_stop_without_start_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #stop
        body = get_xml(
                       Command="Stop",
                       Identify="test_stop_without_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #GetStatus
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_stop_without_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Idle;Idle")
        
        #End
        body = get_xml(
                       Command="End",
                       Identify="test_stop_without_start_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")

    def test_3(self):
        '''
        正常: 结束
        '''
        func_helper._logger.info("test_3")
        body = get_xml(
                       Command="End",
                       Identify="test_normal_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_normal_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_3_1(self):
        '''
        重复end
        '''
        func_helper._logger.info("test_3_1")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_repeat_end_"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #start
        body = get_xml(
                       Command="Start",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(5)
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
#         self.assertEquals(analyze_result["Status"], "Stoped;Stoped")
        
        #stop 
        body = get_xml(
                       Command="Stop",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #get status
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Stoped;Stoped")
        
        
        #End 1
        body = get_xml(
                       Command="End",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
#         
        body = get_xml(
                       Command="End",
                       Identify="test_repeat_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_3_2(self):
        '''
        未初始化直接end
        '''
        func_helper._logger.info("test_3_2")
        body = get_xml(
                       Command="End",
                       Identify="test_end_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_3_3(self):
        '''
        未Start直接End
        '''
        func_helper._logger.info("test_3_3")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_end_without_start"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #End
        body = get_xml(
                       Command="End",
                       Identify="test_end_without_start"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #GetStatus
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_end_without_start"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 


    def test_3_4(self):
        '''
        未Stop进行End
        '''
        func_helper._logger.info("test_3_4")
        #Init
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                       MicIndex="1;2",
                       Identify="test_end_without_stop"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")

        #Start
        body = get_xml(
                       Command="Start",
                       Identify="test_end_without_stop"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
#        time.sleep(3)
        
        #GetStatus
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_end_without_stop"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
#         self.assertEquals(analyze_result["Status"], "Working;Working") 
        
        #End
        body = get_xml(
                       Command="End",
                       Identify="test_end_without_stop"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)   
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        #GetStatus
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_end_without_stop"+str(identify)
                       )
        
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 


    def test_4(self):
        '''
        Init : 不传入url
        '''
        func_helper._logger.info("test_4")
        body = get_xml(
                       Command="Init",
                       MicIndex="1;2",
                       Identify="test_init_no_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")

        
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_no_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

   
    def test_4_1(self):
        '''
        Init : Url传入错误值
        '''
        func_helper._logger.info("test_4_1")
        body = get_xml(
                       Command="Init",
                       Url="abc123!@#;abc123!@#",
                       MicIndex="1;2",
                       Identify="test_init_wrong_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_wrong_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Idle;Idle")
        
        body = get_xml(
                       Command="Start",
                       Identify="test_init_wrong_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")

#        time.sleep(5)

        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_wrong_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Error;Error")
        
        body = get_xml(
                       Command="End",
                       Identify="test_init_wrong_url"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)

    
    def test_4_2(self):
        '''
        Init : Url传入与MicIndex数量不等的值
        ''' 
        func_helper._logger.info("test_4_2")
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac",
                       Url=url1,
                       MicIndex="1;2",
                       Identify="test_init_micindex_dismatch"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_micindex_dismatch"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")
    
    def test_4_3(self):
        '''
        Init : Url为小写
        '''
        func_helper._logger.info("test_4_3")
        body = get_xml(
                       Command="Init",
                       #url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       url=url_str,
                       MicIndex="1;2",
                       Identify="test_init_lower_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_lower_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")
   
    def test_4_4(self):
        '''
        Init : Url传入同一个值
        '''
        func_helper._logger.info("test_4_4")
        body = get_xml(
                       Command="Init",
                       Url=same_url_str,
                       MicIndex="1;2",
                       Identify="test_init_same_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_same_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"],"Idle;Idle")

        body = get_xml(
                       Command="Start",
                       Identify="test_init_same_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")

        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_same_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        self.assertEquals(analyze_result["Status"], "Working;Working")
        self.assertEquals(analyze_result["Url"], same_url_str)
        
        body = get_xml(
                       Command="End",
                       Identify="test_init_same_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_4_5(self):
        '''
        Init : Url传入空值
        '''
        func_helper._logger.info("test_4_5")
        body = get_xml(
                       Command="Init",
                       Url="",
                       MicIndex="1;2",
                       Identify="test_init_empty_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_empty_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_4_6(self):
        '''
        Init : Url传入空格
        '''
        func_helper._logger.info("test_4_3")
        body = get_xml(
                       Command="Init",
                       Url=" ",
                       MicIndex="1;2",
                       Identify="test_init_space_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_space_url_"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")


   
    def test_5(self):
        '''
        Init : 不传入MicIndex
        '''
        func_helper._logger.info("test_5")
        body = get_xml(
                       Command="Init",
                       Url=url_str,
                       Identify="test_init_no_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_no_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")     

    def test_5_1(self):
        '''
        Init : MicIndex传入非数字
        '''
        func_helper._logger.info("test_5_1")
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                        MicIndex="asd;abns",
                       Identify="test_init_micindex_asd123"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_micindex_asd123"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 


    def test_5_2(self):
        '''
        Init : MicIndex传入相同值
        '''
        func_helper._logger.info("test_5_2")
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                        MicIndex="1;1",
                       Identify="test_init_micindex_same"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_micindex_same"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 
        
    def test_5_3(self):
        '''
        Init : MicIndex传入空值
        '''
        func_helper._logger.info("test_5_3")
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                        MicIndex="",
                       Identify="test_init_empty_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_empty_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 
        
    def test_5_4(self):
        '''
        Init : MicIndex传入空格
        '''
        func_helper._logger.info("test_5_4")
        body = get_xml(
                       Command="Init",
                       #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                       Url=url_str,
                        MicIndex=" ",
                       Identify="test_init_spcae_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_spcae_micindex"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1") 
        
    def test_5_5(self):
        '''
        Init : MicIndex传入很大的值
        '''
        func_helper._logger.info("test_5_5")
        body = get_xml(
                       Command="Init",
                       Url=url_str,
                        MicIndex="30000;1",
                       Identify="test_init_mixindex_too_long"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_mixindex_too_long"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0") 
        self.assertEquals(analyze_result["Status"], "Idle;Idle") 
        
        body = get_xml(
                       Command="Start",
                       Identify="test_init_mixindex_too_long"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0") 

        body = get_xml(
                       Command="End",
                       Identify="test_init_mixindex_too_long"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)

    def test_6(self):
        '''
        Init : 不传入Identify
        '''
        func_helper._logger.info("test_6")
        body = get_xml(
                        Command="Init",
                        Url=url_str,
                        MicIndex="1;2",
#                         Identify="test_init_no_identify"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_no_identify"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_6_1(self):
        '''
        Identify 传入带空格和;的值
        '''
        func_helper._logger.info("test_6_1")
        body = get_xml(
                        Command="Init",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify=" test_identify_a with;"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify=" test_identify_a with;"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       Identify=" test_identify_a with;"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify=" test_identify_a with;"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify=" test_identify_a with;"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_6_2(self):
        '''
        Identify 传入空格
        '''
        func_helper._logger.info("test_6_2")
        body = get_xml(
                        Command="Init",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify=" "
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify=" "
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        



    def test_6_3(self):
        '''
        Identify 传入空值
        '''
        func_helper._logger.info("test_6_3")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify=""
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify=""
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")



    def test_7(self):
        '''
        Init : 不传入command
        '''
        func_helper._logger.info("test_7")
        body = get_xml(
#                         Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_init_no_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_no_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_7_1(self):
        '''
        Init : command传入非法值
        '''
        func_helper._logger.info("test_7_1")
        body = get_xml(
                        Command="abc123!@#",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_init_command_invalid"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_command_invalid"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")

    def test_7_2(self):
        '''
        Init : command传入空值
        '''
        func_helper._logger.info("test_7_2")
        body = get_xml(
                        Command="",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_init_empty_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_empty_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")
        
        
    def test_7_3(self):
        '''
        Init : command传入空格
        '''
        func_helper._logger.info("test_7_3")
        body = get_xml(
                        Command=" ",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_init_space_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Param error")
        self.assertEquals(analyze_result["ErrorNo"], "3")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_init_space_command"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Failed")
        self.assertEquals(analyze_result["ResMessage"], "Not init")
        self.assertEquals(analyze_result["ErrorNo"], "1")


    def test_8(self):
        "AddPunc"
        func_helper._logger.info("test_8")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_addpunc"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       AddPunc="yes",
                       Identify="test_start_addpunc"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_addpunc"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_8_1(self):
        "AddPunc"
        func_helper._logger.info("test_8_1")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_addpunc_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       AddPunc="no",
                       Identify="test_start_addpunc_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_addpunc_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_8_2(self):
        "AddPunc"
        func_helper._logger.info("test_8_2")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_addpunc_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       AddPunc="abc231!@#",
                       Identify="test_start_addpunc_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_addpunc_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_8_3(self):
        "AddPunc"
        func_helper._logger.info("test_8_3")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_addpunc_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       AddPunc="",
                       Identify="test_start_addpunc_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_addpunc_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_addpunc_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_9(self):
        "VadHead"
        func_helper._logger.info("test_9")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadHead"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="10",
                       Identify="test_start_VadHead"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadHead"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_10(self):
        "VadSeg"
        func_helper._logger.info("test_9")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadSeg"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="1",
                       Identify="test_start_VadSeg"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadSeg"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_9_1(self):
        "VadHead"
        func_helper._logger.info("test_9_1")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadHead_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="",
                       Identify="test_start_VadHead_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadHead_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_9_2(self):
        "VadHead"
        func_helper._logger.info("test_9")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadHead_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="abc123!@#",
                       Identify="test_start_VadHead_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadHead_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_9_3(self):
        "VadHead"
        func_helper._logger.info("test_9_3")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadHead_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="99999999999999999999999999999999999999999999999999999999999999999",
                       Identify="test_start_VadHead_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadHead_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_9_4(self):
        "VadHead"
        func_helper._logger.info("test_9_4")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadHead_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadHead_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="0",
                       Identify="test_start_VadHead_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadHead_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_10_1(self):
        "VadSeg"
        func_helper._logger.info("test_10_1")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadSeg_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="",
                       Identify="test_start_VadSeg_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadSeg_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_10_2(self):
        "VadSeg"
        func_helper._logger.info("test_10_2")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadSeg_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="abc123!@#",
                       Identify="test_start_VadSeg_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadSeg_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_10_3(self):
        "VadSeg"
        func_helper._logger.info("test_10_3")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadSeg_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="99999999999999999999999999999999999999999999999999999999999999999",
                       Identify="test_start_VadSeg_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadSeg_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_10_4(self):
        "VadSeg"
        func_helper._logger.info("test_10_4")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_VadSeg_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       VadHead="0",
                       Identify="test_start_VadSeg_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_VadSeg_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_VadSeg_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        

    def test_11(self):
        "MaxSecond"
        func_helper._logger.info("test_11")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_MaxSecond"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       MaxSecond="1",
                       Identify="test_start_MaxSecond"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_MaxSecond"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_11_1(self):
        "MaxSecond"
        func_helper._logger.info("test_11_1")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_MaxSecond_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       MaxSecond="",
                       Identify="test_start_MaxSecond_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_MaxSecond_1"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
    def test_11_2(self):
        "MaxSecond"
        func_helper._logger.info("test_11_2")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_MaxSecond_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       MaxSecond="abc123!@#",
                       Identify="test_start_MaxSecond_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_MaxSecond_2"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_11_3(self):
        "MaxSecond"
        func_helper._logger.info("test_11_3")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_MaxSecond_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       MaxSecond="99999999999999999999999999999999999999999999999999999999999999999",
                       Identify="test_start_MaxSecond_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_MaxSecond_3"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        
        
    def test_11_4(self):
        "MaxSecond"
        func_helper._logger.info("test_11_4")
        body = get_xml(
                        Command="Init",
                        #Url="rtsp://10.0.1.168/1.aac;rtsp://10.0.1.168/4.aac",
                        Url=url_str,
                        MicIndex="1;2",
                        Identify="test_start_MaxSecond_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="Start",
                       MaxSecond="0",
                       Identify="test_start_MaxSecond_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="GetStatus",
                       Identify="test_start_MaxSecond_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)
        self.assertEquals(analyze_result["ResCode"], "Success")
        self.assertEquals(analyze_result["ResMessage"], "Success")
        self.assertEquals(analyze_result["ErrorNo"], "0")
        
        body = get_xml(
                       Command="End",
                       Identify="test_start_MaxSecond_4"+str(identify)
                       )
        func_helper._logger.debug(body)
        response = func_helper.do_request(None, body.encode("utf-8"))[1]
        analyze_result = analyze_xml(response)


if __name__ == "__main__":
    func_helper = HttpHelper(url='10.0.1.216', 
                             port='8099', 
                             http_path="/asr", 
                             head_model=None, 
                             logger=Logger("./log/Func_" + "tingshen" + ".log"), 
                             analyze_error = False,
                             timeout = 40)
    identify = ""
                       
    identify = uuid.uuid1()
    import sys
#     sys.argv = ['', 'tingshen_func_test.test_0', 'tingshen_func_test.test_1', 'tingshen_func_test.test_2', 'tingshen_func_test.test_3']
#    sys.argv = ['', 'tingshen_func_test.test_1_3']
    
                       
    unittest.main()


 
#     func_helper = HttpHelper(url='10.0.1.125', 
#                              port='8080', 
#                              http_path="/asr", 
#                              head_model=None, 
#                              logger=Logger("../log/Func_" + "tingshen" + ".log"), 
#                              analyze_error = False,
#                              timeout = 40)
#     identify = ""
#                         
#     identify = uuid.uuid1()
#     import sys; sys.argv = ['', 'tingshen_func_test.test_4_1']
#                        
#     unittest.main()

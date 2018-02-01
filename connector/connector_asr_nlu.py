#coding=utf-8
'''
Created on 2016-11-17


'''

import httplib
import time
import random
import hashlib
from httplib import HTTPResponse


url= "10.0.1.10"
method ="POST"  
#body = open("../Data/TestData/8k16bit.pcm","rb").read()
audibody = open("../Data/TestData/8k16bit.pcm","rb").read()
# grammarbody = open("../Data/Grammar/wordlist.txt" , 'rb').read()
# body = audibody + grammarbody
#body = "我的个人信息安全吗"

postUrl = "/v2/asr/freetalk/chinese_8k_common"
# postUrl = "/v2/asr/grammar/chinese_8k_common"
#postUrl = "/v2/nlu/recog/cn_common"

identify = str(random.randint(1,20000))
request_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
config = "task=recognise,aufmt=pcm8k16bit"
# task_config= config + ",identify="+identify
headers = {
               "x-app" : "ac5d5452",
               "x-sdk" : 8.0,
               "x-date": time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
#               "x-cfg" :"task=recognise,robotid=robot3"+",identify="+identify ,
               "x-cfg" : config ,
               "x-sess" :hashlib.md5(str(request_date) + "40ff7ebfb952b623149688eac84cc68b").hexdigest(),
               "x-udid" :"101:1234567890",  
               "x-tid" :"49652372",
               "x-eid" :"42072569"
                    }
print "IP:"+url
httpClient = httplib.HTTPConnection(url+":8880")
#test=str(body)
httpClient.request(method, postUrl, audibody, headers)
respose = httpClient.getresponse()
respose_body =respose.read().decode("utf-8")
print headers
print "-----------------------------------------------------------------------------------------------------------------------------------------------"
print respose_body

#coding=utf-8
'''
Created on 2016-12-1

@author: wuchaojie
'''
import json
import httplib
headers = {
           "Content-Type" : "application/json",
                      }
body ={ "protocolId": 5,
          "robotHashCode": "289e8c27f4eab4838bd5d50441193b09",
          "platformConnType":2,
          "userId": "100031",
          "talkerId": "10021",
          "receiverId":"20021",
          "query":"五娃有什么本领",
          "appKey":"ac5d5452",
          "sendTime":56000,
          "type":"text",
          "isNeedClearHistory": 0,
          "msgId": "asdasd",
          "isQuestionQuery": 0
          }

conn = httplib.HTTPConnection("10.10.10.195:8900")
#conn.request("GET", "/CSRManagerWebSite/ccbSceneData?CCBAppHashCode=f029c8f9f575e7936f229b240134c140")
conn.request("POST", "/CSRBroker/queryAction",json.dumps(body),headers)
response = conn.getresponse()
response_body = response.read()
print type(response_body)
print response_body
print 
print json.dumps(json.loads(response_body),indent=4,ensure_ascii=False)

with open("result.jsn", "wb") as result_file:
    result_file.write(json.dumps(response_body,indent=4))

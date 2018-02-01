#coding=utf-8
'''
Created on 2016-12-1

@author: wuchaojie
'''
import json
import httplib

conn = httplib.HTTPConnection("10.10.10.195:7001")
conn.request("GET", "/CSRManagerWebSite/ccbSceneData?CCBRobotHashCode=baac43d762969b5346529bc26356d682")
#conn.request("POST", "/CSRBroker/queryAction")
response = conn.getresponse()
response_body = response.read()
print type(response_body)
print response_body
print 
print json.dumps(json.loads(response_body),indent=4,ensure_ascii=False)

with open("result.jsn", "wb") as result_file:
    result_file.write(json.dumps(response_body,indent=4))
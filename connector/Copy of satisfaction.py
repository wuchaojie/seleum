# coding=utf-8
'''
Created on 2016-12-1

@author: wuchaojie
'''
import json
import httplib
headers = {
           "Content-Type" : "application/json",
                      }
body = {  
        "startTime": "2017-02-02 00:00:00",
        "endTime": "2017-05-30 00:00:00",
        "robotId": "191765064",
        "domainId":"191757085",
         "size": 30
        }

conn = httplib.HTTPConnection("10.10.10.195:8900")

print json.dumps(body, ensure_ascii=False, indent=4)

# conn.request("GET", "/CSRManagerWebSite/ccbSceneData?CCBAppHashCode=f029c8f9f575e7936f229b240134c140")
conn.request("POST", "/CSRBroker/hotQuestion", json.dumps(body, ensure_ascii=False), headers)

response = conn.getresponse()

response_body = response.read()

print type(response_body)
print response_body
print 
print json.dumps(json.loads(response_body), indent=4, ensure_ascii=False)

with open("result.jsn", "wb") as result_file:
    result_file.write(json.dumps(response_body, indent=4))

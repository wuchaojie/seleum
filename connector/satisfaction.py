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
        "protocolId": 7501,
        "sendtime":1492482635955,
        "records":[
                   {           
                    "service_log_id":"8dc28d124020cbf4a4af948517b3258b",
                    "annotation":"0418",
                    "satisfaction": -1 
                    }
                   ]
        }

conn = httplib.HTTPConnection("10.10.10.195:8900")

print json.dumps(body, ensure_ascii=False, indent=4)

# conn.request("GET", "/CSRManagerWebSite/ccbSceneData?CCBAppHashCode=f029c8f9f575e7936f229b240134c140")
conn.request("POST", "/CSRBroker/commit", json.dumps(body, ensure_ascii=False), headers)

response = conn.getresponse()

response_body = response.read()

print type(response_body)
print response_body
print 
print json.dumps(json.loads(response_body), indent=4, ensure_ascii=False)

# with open("result.jsn", "wb") as result_file:
#     result_file.write(json.dumps(response_body, indent=4))

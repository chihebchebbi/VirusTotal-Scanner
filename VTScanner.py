#!/usr/bin/env python 

import time
import requests
import json


#Post Request

params = {'apikey': 'apikey here'}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
print(json_response["permalink"])
print(json_response["scan_id"])

#Retrieve Report - Get Request 

params = {'apikey': 'apikey here', 'resource': '7657fcb7d772448a6d8504e4b20168b8'}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
response1 = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
json_response1 = response1.json()

#print (json_response1["scans"])


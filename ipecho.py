#!/usr/bin/env python3

import requests
import json

req = requests.get('https://ipecho.io/my')
parseMe = req.content

#print(parseMe)

ipDict = json.loads(parseMe)
print("ip: " + ipDict['ip'])
print("internet service provider: " + ipDict['isp'])
print("city: " + ipDict['city'])
print("region: " + ipDict['region'])
print("country: " + ipDict['country'])
print("latitude: " + ipDict['latitude'])
print("longitude: " + ipDict['longitude'])

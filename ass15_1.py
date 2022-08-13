import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1591340.json'
address = urllib.request.urlopen(url)
data = address.read()

info = json.loads(data)
info = info["comments"]

temp = 0
for item in info:
    temp=temp+int(item["count"])
    
print(temp)
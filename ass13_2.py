# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
posit= 18
rep_time=7
flag=1
cnt=0

# Retrieve all of the anchor tags
while(flag):
    if cnt == rep_time:
        break
    else: 
        name = ' '
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    name = tags[posit-1].string
    url= tags[posit-1]['href']
    cnt=cnt+1
    
print(name)    
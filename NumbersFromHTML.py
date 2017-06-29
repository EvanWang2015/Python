import urllib.request
import re
from bs4 import BeautifulSoup
html = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_379442.html').read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
total = 0
#concise version of my loop
for tag in tags: total = total + sum([int(x) for x in re.findall('[0-9]+',str(tag))])
print (total)
#the original version of my loop

#for tag in tags:
	#data = re.findall('[0-9]+',str(tag))	
	#data = [int(x) for x in data]
	#print(data, type(data))
	#total = total + sum(data)
#print (total)
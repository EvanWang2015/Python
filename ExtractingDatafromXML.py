import urllib.request
import xml.etree.ElementTree as ET
url = 'http://python-data.dr-chuck.net/comments_379439.xml'
data = urllib.request.urlopen(url).read()
#print (data)
tree = ET.fromstring(data)

#results = tree.finall('comment')
counts = tree.findall('comments/comment')
total = 0
names = list()
index = 0
for item in counts:
	total = total + int(item.find('count').text)
	names.append(item.find('name').text)
print (total)
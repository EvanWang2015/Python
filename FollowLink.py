import urllib.request
#from urllib.request import urlopen
from bs4 import BeautifulSoup
count = input("Enter count: ")
position = input("Enter position: ")
url = 'http://python-data.dr-chuck.net/known_by_Tasha.html'
for i in range(int(count)+1):
	print('Retrieving: ',url)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,"html.parser")
	tags = soup('a')
	count = 0
	for tag in tags:
		#print(tag.get('href',None))
		count = count + 1
		if count == int(position):
			url = tag.get('href',None)
			break	

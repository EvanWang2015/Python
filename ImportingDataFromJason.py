import json
import urllib.request
url = 'http://python-data.dr-chuck.net/comments_379443.json'
data = urllib.request.urlopen(url).read()

try: js = json.loads(data.decode("utf-8"))
except: js = None
if js is None:
	print("Failure to retrieve")
else:
	total = 0
	for item in js["comments"]:
		#print(item['name'], '', item['count'])
		total = total + item['count']
	print(total)
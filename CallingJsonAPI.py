import json
import urllib.request
import urllib.parse
serviceurl ='http://python-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
url = serviceurl  + urllib.parse.urlencode({'sensor': 'false', 'address': address})
print ('Retrieving', url)
js = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
print ('Received ', len(urllib.request.urlopen(url).read()), 'characters')
print('Place id', js['results'][0]['place_id'])
target = open("output.txt", 'w')
target.write(js['results'][0]['place_id'])
target.close()
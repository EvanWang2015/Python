import urllib.parse
import urllib.request
import json
serviceurl ='http://maps.googleapis.com/maps/api/geocode/json?'
ParsedData = []
notParsed =[]
#while True:
address = "Gainesville, FL" #input('Enter location: ')
#if len(address) < 1: break
url = serviceurl  + urllib.parse.urlencode({'sensor': 'false', 'address': address})
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', type(data))
js = json.loads(data.decode("utf-8"))
#
# print('Couldn\'t parse: ', len(notParsed))	
# target = open("output.txt", 'w')
# target.write(str(notParsed))
# target.close()

if 'status' not in js or js['status'] !='ok':
	print('===failure to retrieve ===')
	target = open("output.txt", 'w')
	target.write(json.dumps(js, indent=4))
	target.close()
print (json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print (location)
	
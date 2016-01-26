import urllib, json


def main():
	serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
	location = raw_input('Enter location:')
	url = serviceurl + urllib.urlencode({'sensor':'false','address':location})
	print 'Retrieving', url
	
	data = urllib.urlopen(url).read()
	print 'Retrieved', len(data), 'characters'
	
	info = json.loads(str(data))
	# View json response in pretty format
	print json.dumps(info, indent=4)


if __name__ == "__main__":
	main()


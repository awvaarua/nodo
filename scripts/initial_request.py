import urllib2, json, time, sys

url = "http://192.168.1.135/pendiente/add/req"

while 1:
	try:
		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		break
	except Exception, e:
		print(e)
		time.sleep(60)
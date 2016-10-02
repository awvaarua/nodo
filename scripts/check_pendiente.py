import urllib2, json, time, sys

url = "http://192.168.1.135:8080/pendiente/req"

try:
	check = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
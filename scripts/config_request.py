import urllib2, json, time, sys

url = "http://192.168.1.135:8080/nodo/req/scripts"

try:
	config = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
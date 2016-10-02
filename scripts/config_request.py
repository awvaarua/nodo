import urllib2, json, time, sys

url = "http://localhost:8080/nodo/192.168.1.143/scripts"

try:
	config = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
import urllib2, json, time, sys

url = "http://localhost:8080/pendiente/192.168.1.143"

try:
	check = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
import urllib2, json, time, sys
from uuid import getnode as get_mac

url = "http://192.168.1.132:8080/pendiente/"+str(get_mac())

try:
	check = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
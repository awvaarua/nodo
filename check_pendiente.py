import urllib2, json, time, sys
from uuid import getnode as get_mac
with open('ip') as f:
    ip = f.readline()
url = "http://"+ip+"/pendiente/"+str(get_mac())

try:
	check = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)
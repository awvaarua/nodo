import urllib2, json, time, sys
from uuid import getnode as get_mac
with open('ip') as f:
    ip = f.readline()
url = "http://"+ip+"/pendiente/add/"+str(get_mac())

while 1:
	try:
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		break
	except Exception, e:
		time.sleep(60)
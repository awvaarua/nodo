import urllib2, json, time, sys, os
from uuid import getnode as get_mac
with open(os.path.dirname(os.path.abspath(__file__))+'/ip') as f:
    ip = f.readline().strip('\n')
url = "http://"+ip+"/pendiente/add/"+str(get_mac())

while 1:
	try:
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		break
	except Exception, e:
		time.sleep(60)

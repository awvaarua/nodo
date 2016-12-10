import urllib2, json, time, sys, os
from uuid import getnode as get_mac
with open(os.path.dirname(os.path.abspath(__file__))+'/ip') as f:
    ip = f.readline().strip('\n')
url = "http://"+ip+"/nodo/"+str(get_mac())+"/starting"

while 1:
	try:
		config = json.loads(urllib2.urlopen(url).read())
		break
	except Exception, e:
		time.sleep(20)

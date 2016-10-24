import urllib2, json, time, sys
from uuid import getnode as get_mac
with open('ip') as f:
    ip = f.readline().strip('\n')
url = "http://"+ip+"/nodo/"+str(get_mac())+"/starting"

while 1:
	try:
		config = json.loads(urllib2.urlopen(url).read())
		break
	except Exception, e:
		print e
		time.sleep(60)

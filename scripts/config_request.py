import urllib2, json, time, sys
from uuid import getnode as get_mac
with open('ip') as f:
    ip = f.readline()
url = "http://"+ip+"/nodo/"+str(get_mac())+"/scripts"

while 1:
	try:
		config = json.loads(urllib2.urlopen(url).read())
		break
	except Exception, e:
		time.sleep(60)
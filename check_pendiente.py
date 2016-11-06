import urllib2, json, time, sys, os
from uuid import getnode as get_mac
with open(os.path.dirname(os.path.abspath(__file__))+'/ip') as f:
    ip = f.readline().strip('\n')
url = "http://"+ip+"/pendiente/"+str(get_mac())

try:
	check = json.loads(urllib2.urlopen(url).read())
except Exception, e:
	print(e)

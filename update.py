import urllib2, json, time, sys
from uuid import getnode as get_mac
with open('ip') as f:
    ip = f.readline().strip('\n')
def Update(pid):
	url = "http://"+ip+"/nodo/"+str(get_mac())+"/script/"+str(pid)+"/start"
	r = urllib2.urlopen(url).read()

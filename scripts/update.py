import urllib2, json, time, sys
from uuid import getnode as get_mac

def Update(pid):
	url = "http://192.168.1.132:8080/nodo/"+str(get_mac())+"/script/"+str(pid)+"/start"
	json.loads(urllib2.urlopen(url).read())
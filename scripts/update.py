import urllib2, json, time, sys, json
from uuid import getnode as get_mac

def Update(oldpid, newpid):
	url = "http://192.168.1.132:8080/nodo/"+str(get_mac())+"/script/"+str(oldpid)+"/update"
	data = {"cambio":{"tipo":"pid","valor":newpid}}
	r = requests.post(url, data=data)
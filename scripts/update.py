import urllib2, json, time, sys, requests
from uuid import getnode as get_mac

def Update(oldpid, newpid):
	url = "http://192.168.1.132:8080/nodo/"+str(get_mac())+"/script/"+str(oldpid)+"/update"
	data = {"cambio":{"tipo":"pid","valor":newpid}}
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
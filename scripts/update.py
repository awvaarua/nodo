import urllib2, json, time, sys

def Update(oldpid, newpid):
	url = "http://localhost:8080/nodo/script/"+oldpid+"/update"
	data = {cambio:{tipo:"pid", valor:newpid}}
	try:
		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		break
	except Exception, e:
		print(e)
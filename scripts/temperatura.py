import urllib2, json, time, sys

url = "http://192.168.1.142:8080/nodos/data/add"
data = {"tipo":"Temperatura","datos":{"ip": '192.168.1.142', "val": '30C', "date": '06/10/2016'}}
frec = sys.argv[len(sys.argv)-1]
print(float(frec))

while 1:
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	time.sleep(float(frec))
import json, pprint, config_request, time

time.sleep(5);

config = config_request.config['data']

if config == None:
	import check_pendiente
	pendiente = check_pendiente.check.get('pendiente',None)
	if pendiente == None:
		import initial_request
else:
	scripts = config.get('scripts', [])
	import update
	for script in scripts:
		update.Update(script.get("pid", "0"))
	print "fin"

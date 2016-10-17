import json, pprint, config_request

config = config_request.config['data']

if config == None:
	import check_pendiente
	pendiente = check_pendiente.check.get('pendiente',None)
	if pendiente == None:
		import initial_request
else:
	scripts = config.get('scripts', [])
	import init_script
	import update
	for script in scripts:
		pid = init_script.Init(script)
		print pid
		update.Update(script.get("pid", "0"), pid)
	print "fin"
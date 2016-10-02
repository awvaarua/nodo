import json
import pprint
import config_request

config = config_request.config['data']

if config == None:
	import check_pendiente
	pendiente = check_pendiente.check.get('data','false')
	if pendiente == None:
		import initial_request
else:
	initialized = config.get('initialized', 'false')
	if initialized == "true":
		scripts = config.get("scripts",[])
		import init_script
		import update
		for script in scripts:
		    pid = init_script.Init(script)
		    update.Update(script.get("pid", "0"), pid);
		    print pid
		    
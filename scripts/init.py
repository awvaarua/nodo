import json
import pprint

#Read json
with open('info.json', 'r') as f:
     data = json.load(f)

initialized = data.get("initialized", "false")

if initialized == "false":
        import initial_request
        data["initialized"] = "true"
else:
        scripts = data.get("scripts",[])
        import init_script
        for script in scripts:
                old_pid = script.get('pid','')
                script['pid'] = init_script.Init(script)
                #ActualizarPid(old, new)
        data['scripts'] = scripts

#Save json
with open('info.json', 'w') as f:
     json.dump(data, f)
     
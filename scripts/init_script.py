from subprocess import Popen

def Init(script):
		str_arg = ""
		argumentos = script.get('argumentos', [])
		for arg in argumentos:
				str_arg = str_arg + arg.get('valor', "") + " "
		output = Popen(["python", "temperatura.py", str_arg, "&"])
		return output.pid
import subprocess

def Init(script):
		str_arg = ""
		argumentos = script.get('argumentos', [])
		for arg in argumentos:
				str_arg = str_arg + arg.get('valor', "") + " "
		output = subprocess.Popen(["python", "/home/pi/Scripts/temperatura.py", str_arg])
		return output.pid
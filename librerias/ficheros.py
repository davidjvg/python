import os

def version():
	return 1.0

def creadir(dir):
	if os.access(dir,0):
		print 'el directorio ya existe'	
	else:
		os.mkdir(dir)
		print 'directorio ' (dir)+str 'creado'

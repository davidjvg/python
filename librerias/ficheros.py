import os

def version():
	return 1.0

def creadir(dir):
	if os.access(dir,0):
		print 'el directorio ya existe'	
	else:
		os.mkdir(dir)
#		print 'directorio ' (dir)+str 'creado'


#que nos devuelva user y path

def entorno():
	for variable, valor in os.environ.iteritems():
		if variable=='USER' or variable=='PATH':
			print "%s: %s" % (variable, valor)

#funcion que recupera los ficheros que ocupan ms de
#os.getsize
#os.listdir
def gordos(dir,size):
	for x in os.listdir(dir):
		tamano=os.path.getsize(x)
		if tamano > (size):
			print x
				

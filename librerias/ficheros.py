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
#os.listdir
def gordos(path,size,tipo):
	for x in os.listdir(path):
		tamano=os.path.getsize(x)
		if tamano > int(size):
			print x
#sigue..
			
def visualizar(path):
	archivo=open(path,'a')
	while True:
		linea =	f.readline()
                if not linea: break
		print line

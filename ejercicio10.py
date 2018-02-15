import librerias.ficheros
import sys
if len(sys.argv)<> 2:
	print 'error, introduzca directorios'
else:
	librerias.ficheros.creadir(sys.argv[1])

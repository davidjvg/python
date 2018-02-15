def imprimir():
	print 'programa que imprime'
	
def par_impar(numero):
	if numero%2==0:
		return "par"
	else:
		return "impar"
		
#función que recibe DNI, nombre y apellidos

def alta_cliente (DNI, nombre, *apellidos):
	print DNI
	print '///////--'
	print nombre
	print '///////--'
	print "Tienes " +str(len(apellidos))+" apellidos"
	for i in apellidos:
		print i
		
def iniciales (nombre, *apellidos):
	nom=nombre[0]
	print nom +'.'
	for i in apellidos:
		print str (i[0])+'.'
		
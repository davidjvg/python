


letra=(raw_input('introduce una letra /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////--') )
import os

z=os.listdir('c:/Windows/system32')
for x in z:
#	print (x)
	if x.count(letra) > 0:
		print x
	
	